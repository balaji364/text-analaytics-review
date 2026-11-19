from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url=f"{endpoint.rstrip('/')}/openai/v1/"
)

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": "You are a key phrase extraction assistant. Extract the most important key phrases from the given text. Return only the key phrases as a comma-separated list."
        },
        {
            "role": "user",
            "content": "Artificial Intelligence is transforming healthcare by improving disease diagnosis, medical imaging, and patient care."
        }
    ],
    temperature=0
)

print(response.choices[0].message.content)