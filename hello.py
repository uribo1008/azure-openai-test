import os
from openai import AzureOpenAI

azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_model = os.getenv("AZURE_OPENAI_MODEL")

if azure_openai_endpoint is None or azure_openai_api_key is None or azure_openai_api_version is None:
    raise Exception(
        "Please set the environment variables AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_API_VERSION."
    )

client = AzureOpenAI(
    azure_endpoint=azure_openai_endpoint, api_key=azure_openai_api_key, api_version=azure_openai_api_version
)

# AIのパラメータ
parameters = {
    "model": azure_openai_model,  # AIモデル
    "max_tokens": 100,  # 返信メッセージの最大トークン数
    "temperature": 0.5,  # 生成の多様性（0: 最も確実な回答、1: 最も多様な回答）
    "frequency_penalty": 0,  # 同じ単語を繰り返す頻度（0: 小さい）
    "presence_penalty": 0,  # すでに生成した単語を再度生成する頻度（0: 小さい）
    "stop": ["\n"],
    "stream": False,
}

response = client.chat.completions.create(
    # fmt:off
    messages=[
        {"role": "system",    "content": [{"type": "text", "text": "You are a helpful assistant answering in Japanese."}]},
        {"role": "user",      "content": [{"type": "text", "text": "Does Azure OpenAI support customer managed keys?"}]},
        {"role": "assistant", "content": [{"type": "text", "text": "はい。Azure OpenAIではカスタマー管理キーがサポートされます。"}]},
        {"role": "user",      "content": [{"type": "text", "text": "Which of GPT-4, GPT-4 Turbo, or GPT-4o are you?"}]},
    ],
    # fmt:on
    **parameters
)

print(response.choices[0].message.content)
