from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1/',
    api_key='', # ModelScope Token
)

def llm(prompt,enable_thinking=False):
    response = client.chat.completions.create(
        model='Qwen/Qwen3-32B',
        messages=[
            {'role':'user','content':prompt}
        ],
        stream=True if enable_thinking else False,
        extra_body={
            "extra_thinking": enable_thinking
        }
    )

    if enable_thinking:
        full_content = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_content+=chunk.choices[0].delta.content
        return full_content.strip()
    else:
        return response.choices[0].message.content.strip()