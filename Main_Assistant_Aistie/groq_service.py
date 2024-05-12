from groq import Groq

client = Groq()

def execute(prompt):
        
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ''
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
        
    return response

if __name__ == '__main__':
    print(execute("What is your purpose?"))
