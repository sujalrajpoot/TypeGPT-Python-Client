# TypeGPT Python Client

## Overview

TypeGPT Client is a professional, object-oriented Python library for interacting with the TypeGPT API. It provides a robust and flexible interface for sending chat completion requests with advanced configuration options.

## Features

- 🚀 Easy-to-use API client
- 🔒 Comprehensive error handling
- 🌈 Flexible configuration
- 📦 Typed and structured design
- 🔧 Supports streaming and non-streaming responses

## Installation

### Prerequisites

- Python 3.8+
- `requests` library

### Install Dependencies

```bash
pip install requests
```

## Quick Start

### Basic Usage

```python
from typegpt_client import TypeGPTClient, ChatCompletionConfig

# Create a client with default settings
client = TypeGPTClient()

# Send a simple chat request
response = client.chat("Hello, how are you?")
print(response)
```

### Advanced Configuration

```python
from typegpt_client import TypeGPTClient, ChatCompletionConfig, ModelType

# Create a custom configuration
config = ChatCompletionConfig(
    temperature=0.7,
    model=ModelType.GPT_3_5_TURBO,
    stream=True
)

# Initialize client with a custom system prompt
client = TypeGPTClient(system_prompt="You are a helpful coding assistant.")

# Send a request with custom configuration
response = client.chat("Help me write a Python function", config)
```

## Configuration Options

The `ChatCompletionConfig` class allows you to customize your API requests:

- `temperature`: Controls randomness (0.0 - 1.0)
- `presence_penalty`: Reduces repetition of tokens
- `frequency_penalty`: Reduces repeated token sequences
- `top_p`: Nucleus sampling threshold
- `stream`: Enable/disable streaming responses
- `model`: Select the language model

## Error Handling

The library provides custom exceptions for robust error management:

- `TypeGPTError`: Base exception
- `ConnectionError`: Network-related issues
- `ResponseParsingError`: API response parsing problems

### Example Error Handling

```python
try:
    response = client.chat("Your query")
except TypeGPTError as e:
    print(f"An error occurred: {e}")
```

## Supported Models

Currently supported:
- `GPT_3_5_TURBO`

*More models will be added in future updates.*

## Disclaimer ⚠️

**IMPORTANT: EDUCATIONAL PURPOSE ONLY**

This is an unofficial library and is not affiliated with OpenAI or TypeGPT.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For questions or support, please open an issue or reach out to the maintainer.

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the project repository.
