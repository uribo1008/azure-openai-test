import os
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), api_key=os.getenv("AZURE_OPENAI_KEY"), api_version="2023-05-15"
)

response = client.chat.completions.create(
    model="hjmr_gpt35",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Answer in Japanese."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "はい。Azure OpenAIではカスタマー管理キーがサポートされます。"},
        {"role": "user", "content": "Do other Azure AI services support this too?"},
    ],
)

print(response.choices[0].message.content)
