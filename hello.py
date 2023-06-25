# Import openai
import openai

# Set your API key
openai.api_key = "TEST_KEY"

# Create a request to the Completion endpoint
response = openai.Completion.create(
  # Specify the correct model
  model="text-davinci-003",
  prompt="Tell me something about India?"
)

print(response)

"""

{
  "id": "SOME_ID",
  "object": "text_completion",
  "created": 1,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nIndia is the world's largest democracy and the second-most populous country",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  }
}

"""
