import os
import sys
import threading
import time
import webbrowser
from flask import Flask, render_template, request, jsonify, send_file
from video_generator import generate_video_from_input

app = Flask(__name__)

class VideoGeneratorApp:
    def __init__(self):
        self.is_running = True
        self.generation_status = "idle"  # idle, generating, success, error
        self.generation_message = ""
        self.video_path = "results/Final_Story.mp4"

    def shutdown_server(self):
        """关闭服务器"""
        self.is_running = False
        print("正在关闭服务器...")
        # 强制退出
        os._exit(0)

app_state = VideoGeneratorApp()

@app.route('/')
def index():
    """主页面"""
    return render_template('index.html')

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """生成视频的API接口"""
    try:
        data = request.get_json()
        input_text = data.get('text', '').strip()
        
        if not input_text:
            return jsonify({
                "success": False,
                "message": "请输入文本内容"
            })
        
        # 更新状态
        app_state.generation_status = "generating"
        app_state.generation_message = "视频生成中，请稍候..."
        
        # 调用视频生成函数
        success = generate_video_from_input(input_text)
        
        if success:
            app_state.generation_status = "success"
            app_state.generation_message = "视频生成成功！"
            return jsonify({
                "success": True,
                "message": "视频生成成功！",
                "video_path": app_state.video_path
            })
        else:
            app_state.generation_status = "error"
            app_state.generation_message = "视频生成失败，请重试"
            return jsonify({
                "success": False,
                "message": "视频生成失败，请重试"
            })
            
    except Exception as e:
        app_state.generation_status = "error"
        app_state.generation_message = f"生成过程中出现错误: {str(e)}"
        return jsonify({
            "success": False,
            "message": f"生成过程中出现错误: {str(e)}"
        })

@app.route('/video/<filename>')
def serve_video(filename):
    """提供视频文件访问"""
    if filename == "Final_Story.mp4":
        video_path = "results/Final_Story.mp4"
        if os.path.exists(video_path):
            return send_file(video_path, as_attachment=False)
    return "Video not found", 404

@app.route('/check-video')
def check_video():
    """检查视频是否存在"""
    video_path = "results/Final_Story.mp4"
    exists = os.path.exists(video_path)
    return jsonify({"exists": exists})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """关闭服务器"""
    print("收到关闭请求...")
    # 在新线程中关闭，避免请求阻塞
    threading.Thread(target=app_state.shutdown_server).start()
    return jsonify({"message": "服务器正在关闭..."})

def open_browser():
    """自动打开浏览器"""
    time.sleep(1.5)  # 等待服务器启动
    webbrowser.open('http://127.0.0.1:5000')

def main():
    """主函数"""
    print("启动视频生成工具...")
    print("服务器将在 http://127.0.0.1:5000 运行")
    print("关闭浏览器窗口将自动退出程序")
    
    # 确保results目录存在
    os.makedirs("results", exist_ok=True)
    
    # 在单独的线程中打开浏览器
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        # 启动Flask应用
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    finally:
        app_state.is_running = False
        print("程序退出")

if __name__ == '__main__':
    main()