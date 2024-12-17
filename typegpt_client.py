import json
import requests
from typing import Optional, List, Dict, Any, Generator
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

class TypeGPTError(Exception):
    """Base exception for TypeGPT-related errors."""
    pass

class ConnectionError(TypeGPTError):
    """Raised when there are connection-related issues."""
    pass

class ResponseParsingError(TypeGPTError):
    """Raised when there are issues parsing the API response."""
    pass

class ModelType(Enum):
    """Enumeration of supported model types."""
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    # Can add more models as they become available

@dataclass
class ChatMessage:
    """Represents a chat message with role and content."""
    role: str
    content: str

@dataclass
class ChatCompletionConfig:
    """Configuration for chat completion request."""
    temperature: float = 0.7
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    top_p: float = 1.0
    stream: bool = True
    model: ModelType = ModelType.GPT_3_5_TURBO

class TypeGPTClient:
    """Client for interacting with the TypeGPT API."""
    
    _BASE_URL = "https://chat.typegpt.net/api/openai/v1/chat/completions"
    _DEFAULT_HEADERS = {
        "Content-Type": "application/json",
        "origin": "https://chat.typegpt.net",
        "accept": "application/json, text/event-stream"
    }

    def __init__(self, system_prompt: str = "You are a helping assistant named Jarvis."):
        """
        Initialize the TypeGPT client.
        
        :param system_prompt: Initial system prompt for context setting
        """
        self._system_prompt = system_prompt
        self._session = requests.Session()

    def chat(
        self, 
        query: str, 
        config: Optional[ChatCompletionConfig] = None
    ) -> str:
        """
        Send a chat completion request to TypeGPT.
        
        :param query: User's message
        :param config: Optional configuration for the request
        :return: Complete response from the API
        :raises ConnectionError: For network-related issues
        :raises ResponseParsingError: For response parsing problems
        """
        # Use default config if not provided
        config = config or ChatCompletionConfig()
        
        # Prepare messages
        messages = [
            {"role": "system", "content": self._system_prompt},
            {"role": "user", "content": query}
        ]

        # Prepare payload
        payload = {
            "messages": messages,
            "stream": True,
            "model": config.model.value,
            "temperature": config.temperature,
            "presence_penalty": config.presence_penalty,
            "frequency_penalty": config.frequency_penalty,
            "top_p": config.top_p
        }

        try:
            # Send request
            response = self._session.post(
                self._BASE_URL, 
                headers=self._DEFAULT_HEADERS, 
                json=payload, 
                stream=True
            )
            response.raise_for_status()

            # Process streaming response
            return self._process_streaming_response(response, config.stream)

        except requests.RequestException as e:
            raise ConnectionError(f"API request failed: {e}") from e

    def _process_streaming_response(
        self, 
        response: requests.Response, 
        should_stream: bool
    ) -> str:
        """
        Process the streaming response from the API.
        
        :param response: API response object
        :param should_stream: Whether to print streamed content
        :return: Complete response string
        :raises ResponseParsingError: For parsing issues
        """
        full_response = ""
        
        try:
            for value in response.iter_lines(decode_unicode=True):
                if value.startswith('data:'):
                    try:
                        parsed_json = json.loads(value[5:])
                        content = parsed_json['choices'][0]['delta'].get('content', '')
                        
                        if should_stream:
                            print(content, end="", flush=True)
                        
                        full_response += content
                    except:continue
        
        except Exception as e:
            raise ResponseParsingError(f"Unexpected error processing response: {e}") from e

        return full_response

if __name__ == "__main__":
    """Example usage of the TypeGPT client."""
    try:
        # Create client with default system prompt
        client = TypeGPTClient()
        
        # Create a custom configuration if needed
        config = ChatCompletionConfig(
            temperature=0.7,
            stream=True
        )
        
        # Send a chat request
        response = client.chat("Hi, how are you?", config)
        print(f"\nResponse: {response}")
    
    except TypeGPTError as e:
        print(f"TypeGPT Error: {e}")