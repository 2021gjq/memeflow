import os
import tempfile
from creativity import get_text
from script import get_script
from movie import process_jsonl_story

def generate_video_from_input(input_text):
    """整合的视频生成流程"""
    
    # 创建临时目录存放中间文件
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            print("开始视频生成流程...")
            
            # 步骤1: 生成创意文本
            print("步骤1: 生成创意文本...")
            text_file = os.path.join(temp_dir, "text.txt")
            creative_text = get_text(input_text, text_file)
            
            # 步骤2: 生成脚本
            print("步骤2: 生成脚本...")
            script_file = os.path.join(temp_dir, "script.jsonl")
            script_content = get_script(text_file, script_file)
            
            if not script_content:
                print("脚本生成失败")
                return False
            
            # 步骤3: 生成视频
            print("步骤3: 生成视频...")
            success = process_jsonl_story(script_file)
            
            if success:
                print(f"视频生成成功！")
            else:
                print("视频生成失败")
            
            return success
            
        except Exception as e:
            print(f"视频生成流程出错: {e}")
            import traceback
            traceback.print_exc()
            return False

# 独立运行测试
if __name__ == "__main__":
    # 测试代码
    test_input = "不想上班"
    generate_video_from_input(test_input)