import os
from openai import OpenAI
from dotenv import load_dotenv

fixed_prompt = """
请根据输入文本生成一段富有戏剧性和梗文化的视频文案小剧本，输入文本如下：
"""

def init_client():
    load_dotenv()
    api_key = os.environ.get('CREATIVITY_API_KEY')
    if not api_key:
        raise ValueError("CREATIVITY_API_KEY 未设置，请检查.env文件")
    return OpenAI(
        api_key=api_key,
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
    )

def get_text(input_text='不想上班', output_file="text.txt"):
    client = init_client()
    response = client.chat.completions.create(
        model="qwen3-max", 
        messages=[{"role": "user", "content": fixed_prompt + input_text}],
        stream=False
    )
    res = response.choices[0].message.content

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(res)
        print(f"\n输出已保存到文件: {output_file}")
    except Exception as e:
        print(f"保存文件时出错: {e}")
    
    return res

if __name__ == "__main__":
    get_text()