import os
import json
from openai import OpenAI
from dotenv import load_dotenv

fixed_prompt = """
请将输入文本转化为结构化的脚本输出，输出格式如下：
[
  {
    "scene_number": 1,
    "backgrounds": "airport",
    "meme":"崩溃"
    "text": "周一早上7:00",
    "duration":3
  }
  // ...
]
backgrounds严格从以下选择：["concert", "fantacy", "others", "rooftop", "stage", "airport", "amusementpark", "bank", "cinema", "classroom", "grassland", "gym", "home", "hospital", "kitchen", "library", "museum", "park", "playground", "pool", "restaurant", "school", "shop", "station", "theater", "village"]；
meme严格从以下选择：["哀求", "崩溃", "吃惊", "大笑", "呆滞", "得瑟", "得意", "烦躁", "害羞", "坏笑", "欢呼", "饥饿", "焦急", "教训", "惊讶", "可怜", "蔑视", "努力", "其他", "傻笑", "痛苦", "威严", "无辜", "无奈", "无助", "兴奋", "勇敢", "愉快", "震惊","愉快"]
输入文本如下：
"""

def init_client():
    load_dotenv()
    api_key = os.environ.get('SCRIPT_API_KEY')
    if not api_key:
        raise ValueError("SCRIPT_API_KEY 未设置，请检查.env文件")
    return OpenAI(
        api_key=api_key,
        base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
    )

def read_input_file(file_path='text.txt'):
    """读取输入文本文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        if not content:
            raise ValueError(f"文件 {file_path} 为空")
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"找不到输入文件: {file_path}")
    except Exception as e:
        raise Exception(f"读取文件时出错: {e}")

def save_to_jsonl(data, output_file="script.jsonl"):
    """将数据保存为JSONL格式"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # 如果返回的是JSON字符串，先解析为Python对象
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except json.JSONDecodeError:
                    # 如果不是标准JSON，直接作为文本保存
                    f.write(json.dumps({"content": data}, ensure_ascii=False) + '\n')
                    return
            
            # 如果是列表，每条记录单独一行
            if isinstance(data, list):
                for item in data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
            else:
                # 如果是单个对象，直接写入
                f.write(json.dumps(data, ensure_ascii=False) + '\n')
        
        print(f"输出已保存到文件: {output_file}")
    except Exception as e:
        print(f"保存JSONL文件时出错: {e}")

def get_script(input_file='text.txt', output_file="script.jsonl"):
    """主函数：读取输入文件，生成脚本并保存为JSONL"""
    try:
        # 读取输入文件
        input_text = read_input_file(input_file)
        print(f"成功读取输入文件: {input_file}")
        print(f"输入内容: {input_text[:100]}...")  # 只显示前100个字符
        
        # 初始化客户端并调用API
        client = init_client()
        full_prompt = fixed_prompt + input_text
        
        response = client.chat.completions.create(
            model="qwen3-max", 
            messages=[{"role": "user", "content": full_prompt}],
            stream=False
        )
        res = response.choices[0].message.content
        
        # 打印结果到控制台
        print("\n生成的脚本内容:")
        print(res)
        
        # 保存为JSONL文件
        save_to_jsonl(res, output_file)
        
        return res
        
    except Exception as e:
        print(f"处理过程中出错: {e}")
        return None

if __name__ == "__main__":
    get_script()