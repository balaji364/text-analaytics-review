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
            "content": "You are a sentiment analysis assistant. Analyze the given text and classify its sentiment as Positive, Negative, or Neutral. Also provide a short explanation."
        },
        {
            "role": "user",
            "content": "The food was delicious and the service was excellent. I really enjoyed my experience."
        }
    ]
)

print("Sentiment Analysis:")
print(response.choices[0].message.content)