import os
from openai import AzureOpenAI

azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")

if azure_openai_endpoint is None or azure_openai_key is None:
    raise Exception(
        "Please set the environment variables AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY to your Azure OpenAI endpoint and API key."
    )

client = AzureOpenAI(azure_endpoint=azure_openai_endpoint, api_key=azure_openai_key, api_version="2023-05-15")

response = client.chat.completions.create(
    model="hjmr_gpt35",
    messages=[
        {"role": "system", "content": "You are a helpful assistant answering in Japanese."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "はい。Azure OpenAIではカスタマー管理キーがサポートされます。"},
        {"role": "user", "content": "Do other Azure AI services support this too?"},
    ],
)

print(response.choices[0].message.content)
