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
            "content": "You are a text summarization assistant. Summarize the given text in simple and clear English. Include only the important points."
        },
        {
            "role": "user",
            "content": """
            Artificial Intelligence (AI) is a rapidly growing technology
            that enables machines to perform tasks that normally require
            human intelligence. AI is used in healthcare, education,
            banking, transportation, and many other industries.
            It helps doctors diagnose diseases, supports students in
            learning, detects fraud in banking, and improves self-driving
            vehicles. AI saves time, reduces human effort, and increases
            efficiency. However, it also creates challenges related to
            privacy, security, and employment.
            """
        }
    ]
)

print("Summary:")
print(response.choices[0].message.content)