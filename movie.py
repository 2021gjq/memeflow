import os
import json
import numpy as np
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import textwrap

# 确保results文件夹存在
output_folder = f"results"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def create_text_clip_pil(text, duration, width=1000, fontsize=60):
    """使用PIL创建带透明背景的文字视频片段"""
    
    # 计算文字高度
    try:
        # 尝试加载中文字体
        font = ImageFont.truetype("simhei.ttf", fontsize)  # 黑体
    except:
        try:
            font = ImageFont.truetype("msyh.ttc", fontsize)  # 微软雅黑
        except:
            try:
                font = ImageFont.truetype("simsun.ttc", fontsize)  # 宋体
            except:
                # 使用默认字体（可能不支持中文）
                font = ImageFont.load_default()
                print("警告: 使用默认字体，可能不支持中文显示")
    
    # 文字换行处理
    char_width = fontsize * 0.6  # 估算字符宽度
    max_chars_per_line = int(width / char_width)
    
    # 使用textwrap进行智能换行
    wrapped_text = textwrap.fill(text, width=max_chars_per_line)
    
    # 计算文字区域大小
    lines = wrapped_text.split('\n')
    line_height = int(fontsize * 1.3)
    text_height = len(lines) * line_height + 20  # 增加一些边距
    
    # 创建透明背景图像
    img = Image.new('RGBA', (width, text_height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制文字（带黑色描边效果）
    y_position = 10  # 顶部边距
    
    for line in lines:
        # 估算文字宽度
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_position = (width - text_width) // 2
        
        # 绘制文字描边（多个方向偏移创建描边效果）
        offsets = [(-2, -2), (-2, 2), (2, -2), (2, 2), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for offset_x, offset_y in offsets:
            draw.text((x_position + offset_x, y_position + offset_y), 
                     line, font=font, fill=(0, 0, 0, 255))
        
        # 绘制主要文字（白色）
        draw.text((x_position, y_position), line, font=font, fill=(255, 255, 255, 255))
        
        y_position += line_height
    
    # 转换为numpy数组
    img_array = np.array(img)
    
    # 创建视频片段（带透明通道）
    text_clip = ImageClip(img_array, duration=duration, ismask=False)
    
    return text_clip

def BgVideo(text, place, num, duration):
    # 创建一个空白视频，时长为指定duration，分辨率为1080x1080
    width, height = 1080, 1080
    blank_clip = ColorClip((width, height), color=(0, 0, 0), duration=duration)

    # 在指定时间点添加图片
    image_path = f"backgrounds/{place}.jpg"
    if not os.path.exists(image_path):
        print(f"警告: 背景图片 {image_path} 不存在，使用默认背景")
        image_path = f"backgrounds/home.jpg"  # 使用默认背景
    
    image_clip = ImageClip(image_path).resize(width=1080)
    image_clip = image_clip.set_position(('center', 'top')).set_start(0).set_end(duration)

    # 使用PIL创建透明背景文字片段
    txt_clip = create_text_clip_pil(text, duration, width=1000, fontsize=60)
    
    # 设置文字位置在视频上方（距离顶部50像素）
    txt_clip = txt_clip.set_position(('center', 50)).set_start(0).set_end(duration)

    # 合成视频：先背景，再文字（文字在最上层）
    final_clip = CompositeVideoClip([blank_clip, image_clip, txt_clip])

    # 保存最终视频
    final_clip.write_videofile(f'{output_folder}/backgrounds{num}.mp4', codec='libx264', fps=24, verbose=False, logger=None)
    print(f"已生成背景视频: backgrounds{num}.mp4")

def chroma_key_composite(green_frame, bg_frame):
    """绿幕抠图合成函数"""
    # 将帧转换为float类型以便处理
    green_frame = green_frame.astype('float32')
    bg_frame = bg_frame.astype('float32')
    
    # 提取RGB通道
    r, g, b = green_frame[:,:,0], green_frame[:,:,1], green_frame[:,:,2]
    
    # 计算绿色强度
    green_intensity = g - (r + b) / 2
    
    # 创建mask (绿色区域为0，非绿色区域为1)
    mask = np.where(green_intensity > 50, 0.0, 1.0)  # 调整阈值以适应您的绿幕
    
    # 将mask扩展到3个通道
    mask_3d = np.stack([mask, mask, mask], axis=2)
    
    # 应用mask合成
    result = green_frame * mask_3d + bg_frame * (1 - mask_3d)
    
    return result.astype('uint8')

def AddMeme(emo, num, duration):
    """使用MoviePy实现绿幕抠图，并确保文字在最上层"""
    try:
        green_screen_video_path = f'meme/{emo}.mp4'
        replacement_video_path = f'{output_folder}/backgrounds{num}.mp4'
        output_video_path = f'{output_folder}/{num}.mp4'
        
        # 检查文件是否存在
        if not os.path.exists(green_screen_video_path):
            print(f"错误: 表情视频 {green_screen_video_path} 不存在")
            return False
        if not os.path.exists(replacement_video_path):
            print(f"错误: 背景视频 {replacement_video_path} 不存在")
            return False
        
        # 加载视频
        green_clip = VideoFileClip(green_screen_video_path)
        bg_clip = VideoFileClip(replacement_video_path)
        
        # 确保视频长度一致
        if green_clip.duration < duration:
            green_clip = green_clip.loop(duration=duration)
        else:
            green_clip = green_clip.subclip(0, duration)
        
        if bg_clip.duration < duration:
            bg_clip = bg_clip.loop(duration=duration)
        else:
            bg_clip = bg_clip.subclip(0, duration)
        
        # 调整大小
        green_clip = green_clip.resize(height=1080)
        bg_clip = bg_clip.resize(height=1080)
        
        # 创建合成函数 - 绿幕抠图合成背景和猫meme
        def make_frame(t):
            try:
                green_frame = green_clip.get_frame(t)
                bg_frame = bg_clip.get_frame(t)
                # 先合成绿幕抠图（猫meme + 背景）
                composite_frame = chroma_key_composite(green_frame, bg_frame)
                return composite_frame
            except Exception as e:
                print(f"处理帧时出错 (t={t}): {e}")
                return np.zeros((1080, 1080, 3), dtype=np.uint8)
        
        # 创建绿幕合成视频（猫meme + 背景）
        meme_bg_composite = VideoClip(make_frame, duration=duration)
        meme_bg_composite = meme_bg_composite.set_fps(24)
        
        # 重新加载背景视频以提取文字层
        bg_with_text_clip = VideoFileClip(replacement_video_path)
        
        # 创建一个函数来提取文字层（通过比较原始背景和带文字的背景）
        def extract_text_mask(t):
            # 获取带文字的帧
            text_frame = bg_with_text_clip.get_frame(t)
            # 获取原始背景帧（通过重新合成但不加文字）
            bg_frame = bg_clip.get_frame(t)
            
            # 计算差异来提取文字区域
            diff = np.mean(np.abs(text_frame.astype('float32') - bg_frame.astype('float32')), axis=2)
            # 创建文字mask（文字区域为1，其他为0）
            text_mask = np.where(diff > 10, 1.0, 0.0)  # 调整阈值
            
            return text_mask
        
        # 创建文字mask剪辑
        text_mask_clip = VideoClip(extract_text_mask, duration=duration)
        text_mask_clip = text_mask_clip.set_fps(24)
        
        # 最终合成：在绿幕合成视频上添加文字
        def final_composite_frame(t):
            # 获取绿幕合成帧（猫meme + 背景）
            meme_bg_frame = meme_bg_composite.get_frame(t)
            # 获取带文字的原始帧
            text_frame = bg_with_text_clip.get_frame(t)
            # 获取文字mask
            text_mask = text_mask_clip.get_frame(t)
            
            # 将mask扩展到3个通道
            text_mask_3d = np.stack([text_mask, text_mask, text_mask], axis=2)
            
            # 最终合成：使用文字mask将文字区域从原始帧复制到合成帧
            final_frame = meme_bg_frame * (1 - text_mask_3d) + text_frame * text_mask_3d
            
            return final_frame.astype('uint8')
        
        # 创建最终视频
        final_clip = VideoClip(final_composite_frame, duration=duration)
        final_clip = final_clip.set_fps(24)
        
        # 保存结果
        final_clip.write_videofile(output_video_path, codec='libx264', fps=24, verbose=False, logger=None)
        
        # 关闭剪辑
        green_clip.close()
        bg_clip.close()
        meme_bg_composite.close()
        bg_with_text_clip.close()
        text_mask_clip.close()
        final_clip.close()
        
        print(f"已生成表情视频: {num}.mp4")
        return True
        
    except Exception as e:
        print(f"处理表情视频时出错: {e}")
        import traceback
        traceback.print_exc()
        return False

def AddNewline(text):
    punctuations = ['，', '。', '！', '？', '；', '：', ',', '.', '?', '!', ';', ':']
    result = ''
    buffer = ''
    for char in text:
        buffer += char
        if char in punctuations:
            if len(buffer.strip()) > 7:
                result += buffer + '\n'
                buffer = ''
    result += buffer  # 添加最后一部分文本
    if result.endswith('\n'):
        return result[:-1]
    else:
        return result

def concatenate_videos(folder_path, video_names, output_file):
    video_clips = []
    for video_name in video_names:
        video_path = os.path.join(folder_path, video_name)
        if os.path.exists(video_path):
            try:
                video_clip = VideoFileClip(video_path)
                video_clips.append(video_clip)
            except Exception as e:
                print(f"警告: 无法加载视频文件 {video_path}: {e}")
        else:
            print(f"警告: 视频文件 {video_path} 不存在，跳过")

    if video_clips:
        try:
            final_clip = concatenate_videoclips(video_clips)
            final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', verbose=False, logger=None)
            print(f"已生成最终视频: {output_file}")
        except Exception as e:
            print(f"视频合并错误: {e}")
    else:
        print("错误: 没有可用的视频片段进行合并")

def add_audio_to_video(video_file, audio_file, output_file):
    if not os.path.exists(video_file):
        print(f"错误: 视频文件 {video_file} 不存在")
        return False
    if not os.path.exists(audio_file):
        print(f"警告: 音频文件 {audio_file} 不存在，生成无音频视频")
        import shutil
        shutil.copy(video_file, output_file)
        return True
    
    try:
        video = VideoFileClip(video_file)
        audio = AudioFileClip(audio_file)
        
        if audio.duration > video.duration:
            audio = audio.subclip(0, video.duration)
        
        video_with_audio = video.set_audio(audio)
        video_with_audio.write_videofile(output_file, codec='libx264', audio_codec='aac', verbose=False, logger=None)
        
        video.close()
        audio.close()
        video_with_audio.close()
        
        print(f"已添加音频到视频: {output_file}")
        return True
    except Exception as e:
        print(f"添加音频错误: {e}")
        return False

def cleanup_intermediate_files(scene_numbers):
    """清理中间生成的多余视频文件"""
    print("\n清理中间文件...")
    files_to_delete = []
    
    for scene_number in scene_numbers:
        bg_video = f"{output_folder}/backgrounds{scene_number}.mp4"
        if os.path.exists(bg_video):
            files_to_delete.append(bg_video)
        
        video_file = f"{output_folder}/{scene_number}.mp4"
        if os.path.exists(video_file):
            files_to_delete.append(video_file)
        
        out_video = f"{output_folder}/out{scene_number}.mp4"
        if os.path.exists(out_video):
            files_to_delete.append(out_video)
    
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"已删除: {os.path.basename(file_path)}")
        except Exception as e:
            print(f"删除文件 {file_path} 时出错: {e}")
    
    print(f"清理完成，共删除 {len(files_to_delete)} 个中间文件")

def process_jsonl_story(jsonl_file):
    """处理JSONL文件并生成视频"""
    
    story = []
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                try:
                    scene_data = json.loads(line.strip())
                    story.append(scene_data)
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}，跳过该行: {line}")
    
    print(f"成功读取 {len(story)} 个场景")
    
    video_names = []
    scene_numbers = []
    
    for i, scene in enumerate(story):
        scene_number = scene.get("scene_number", i + 1)
        place = scene.get("backgrounds", "home")
        text = scene.get("text", "")
        emo = scene.get("meme", "其他")
        duration = scene.get("duration", 3)
        
        print(f"\n处理场景 {scene_number}: {place} - {emo} - {duration}秒")
        
        scene_numbers.append(scene_number)
        processed_text = AddNewline(text)
        print(f"文本内容: {processed_text}")
        
        # 生成背景视频（包含透明文字）
        BgVideo(processed_text, place, scene_number, duration)
        
        # 添加表情（文字已经在最上层）
        if not AddMeme(emo, scene_number, duration):
            print(f"警告: 场景 {scene_number} 的表情视频生成失败")
            continue
        
        # 添加音频到视频
        audio_file = f"meme_audio/{emo}.mp3"
        video_file = f"{output_folder}/{scene_number}.mp4"
        output_video_file = f"{output_folder}/out{scene_number}.mp4"
        
        add_audio_to_video(video_file, audio_file, output_video_file)
        video_names.append(f"out{scene_number}.mp4")
    
    if video_names:
        folder_path = f"results"
        output_file = f"results/Final_Story.mp4"
        concatenate_videos(folder_path, video_names, output_file)
        cleanup_intermediate_files(scene_numbers)
        print("\n视频生成完成！最终视频: Final_Story.mp4")
        return True
    else:
        print("错误: 没有成功生成任何视频片段")
        return False

# 使用示例
if __name__ == "__main__":
    jsonl_file = "script.jsonl" 
    process_jsonl_story(jsonl_file)