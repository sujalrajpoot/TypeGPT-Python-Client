# Basic Usage
from typegpt_client import TypeGPTClient, ChatCompletionConfig

# Create a client with default settings
client = TypeGPTClient()

# Send a simple chat request
response = client.chat("Hello, how are you?")
print(response)

# Advanced Configuration
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