import tkinter as tk
import subprocess
import time
import random
from queue import Queue
from threading import Thread

# 定义要循环输入的文本内容列表
text_list = [
    "123",
    "456",
    "789",
]

def adb_shell(command):
    """执行 adb shell 命令并返回输出结果"""
    result = subprocess.run(['adb', 'shell', command], capture_output=True, text=True)
    return result.stdout.strip()

def copy_and_paste_text(text_to_copy):
    """复制并粘贴指定文本"""
    try:
        time.sleep(0.5)
        screen_width, screen_height = get_screen_size()
        # 点击输入框坐标
        tap_screen(int(screen_width * 0.2177), int(screen_height * 0.9458))
        time.sleep(1)

        # 将文本复制到剪贴板文件
        clipboard_path = '/sdcard/clipboard.txt'
        command_copy = f'echo "{text_to_copy}" > {clipboard_path}'
        adb_shell(command_copy)
        time.sleep(0.5)

        # 从剪贴板文件读取内容并粘贴
        command_paste = f'input text "$(cat {clipboard_path})"'
        adb_shell(command_paste)

        print(f"成功复制并粘贴文本：{text_to_copy}")
        time.sleep(0.5)

        # 模拟回车键（KEYCODE_ENTER）
        adb_shell('input keyevent 66')  # KEYCODE_ENTER，模拟回车
        print("执行回车操作")
    except Exception as e:
        print(f"操作失败：{e}")

def process_queue(queue):
    """从队列中获取任务并顺序执行"""
    while True:
        text = queue.get()
        if text is None:
            break
        copy_and_paste_text(text)
        queue.task_done()

def on_start_button_click():

    """处理开始按钮点击事件"""
    # 创建任务队列
    task_queue = Queue()

    # 将文本任务放入队列
    for text in text_list:
        task_queue.put(text)

    # 启动线程处理队列任务
    worker_thread = Thread(target=process_queue, args=(task_queue,))
    worker_thread.start()
def get_screen_size():
    """获取连接设备的屏幕尺寸信息"""
    command = "adb shell wm size"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    output = result.stdout.strip()

    # 解析屏幕尺寸信息
    size_str = output.split()[-1]  # 提取屏幕尺寸部分
    width, height = map(int, size_str.split('x'))
    print(f"屏幕宽高：{width}：{height}")

    return width, height
def tap_screen(x, y):
    """模拟屏幕点击事件"""
    command = f'input tap {x} {y}'
    adb_shell(command)
    print(f"点击屏幕：({x}, {y})")

def main():
    # 创建 GUI 界面
    root = tk.Tk()
    root.title("手机操作模拟器")

    # 添加开始按钮
    start_button = tk.Button(root, text="开始模拟操作", command=on_start_button_click)
    start_button.pack(pady=20)

    # 运行 GUI 主循环
    root.mainloop()

if __name__ == '__main__':
    main()
