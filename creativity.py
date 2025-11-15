import os
from openai import OpenAI
from dotenv import load_dotenv
from prompt import PromptTemplate,query2script_prompt

load_dotenv()
def init_client():
    api_key = os.environ.get('CREATIVITY_API_KEY')
    BASE_URL = os.environ.get('BASE_URL')
    if not api_key:
        raise ValueError("CREATIVITY_API_KEY 未设置，请检查.env文件")
    return OpenAI(
        api_key=api_key,
        base_url=BASE_URL,
    )

def get_text(input_text='帮我按照格式生成一个HKU校园爽剧，要翻转打脸', output_file="text.txt"):
    client = init_client()
    MODEL = os.environ.get('MODEL')
    q2s = PromptTemplate(
        system_template=(query2script_prompt),
        user_template=("这是一段用户输入文本，请按照要求生成脚本：{user_input}")
    )
    q2s_prompt = q2s.format_messages(user_input=input_text)
    response = client.chat.completions.create(
        messages=q2s_prompt,
        stream=False,
        model=MODEL,
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