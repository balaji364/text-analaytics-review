pip install openai
pip install azure-ai-ml
python -m pip install azure-identity

from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url=f"{endpoint.rstrip('/')}/openai/v1/"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of India?"}
    ]
)

print(response.choices[0].message.content)
