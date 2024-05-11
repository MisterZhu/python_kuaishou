import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import time
import pyperclip
import random
import tkinter as tk
from tkinter import messagebox

# 定义要循环粘贴的文本内容列表
text_list = [
    "[色][色][色][色][色][色][色][害羞][害羞][害羞][害羞]",
    "[色][色][色][色][色][色][色][害羞][害羞][害羞][害羞]",
    "🔞 🔞 🔞 🔞 🔞 🔞 🔞 🔞",
    "6666666",
    "123456",
    "喜欢",
    "非常棒",
    "1111111111111",
    "😊😊😊😊😊😊😊😊😊",
    "👍👍👍👍👍👍👍👍👍👍"
]

# 全局变量，用于控制循环停止
stop_flag = False
paste_completed = threading.Event()  # 用于表示粘贴操作是否完成的事件

def simulate_paste():
    global stop_flag
    global paste_completed
    
    for text in text_list:
        if stop_flag:
            break  # 如果停止标志为True，则退出循环
        # random_number = random.uniform(0.1, 0.2)
        random_number = 0.1

        print("开始模拟粘贴操作...")
        pyperclip.copy(text)
        time.sleep(random_number)
        
        # 模拟按下 Command/Ctrl + V
        pyautogui.hotkey('command', 'v')  # 在 Mac 上使用 'command'，在 Windows 上可以使用 'ctrl'
        print(f"模拟按下 Command/Ctrl + V，粘贴文本：{text}")
        time.sleep(random_number)
        
        # 模拟按下 Return/Enter 键
        pyautogui.press('enter')  # 模拟按下 Enter 键
        print("模拟按下 Enter")
        
    paste_completed.set()  # 设置粘贴操作完成的事件

def start_once_task(entries):
    message = "开始执行半自动评论，执行一轮评论"
    show_message_box(message)
    global text_list
    text_list = [entry.get() for entry in entries]  # 获取输入框的值并赋值给text_list
    global stop_flag
    stop_flag = False  # 确保停止标志为False
    time.sleep(3)
    start_simulation()

def start_simulation():
    # 创建一个新线程来执行模拟键盘操作
    threading.Thread(target=simulate_paste).start()

def start_task(entries):
    message = "开始执行全自动评论"
    show_message_box(message)
    global text_list
    text_list = [entry.get() for entry in entries]  # 获取输入框的值并赋值给text_list
    global stop_flag
    stop_flag = False  # 确保停止标志为False
    threading.Thread(target=continuous_task).start()

def stop_task():
    global stop_flag
    stop_flag = True  # 设置停止标志为True
    message = "开始停止执行。几秒钟后结束。。。"
    show_message_box(message)
def continuous_task():
    global paste_completed
    
    while not stop_flag:
        time.sleep(4)
        print("模拟鼠标点击坐标（216，216）")
        pyautogui.click(216, 216)
        time.sleep(10)
        print("模拟鼠标点击坐标（881，671）")
        pyautogui.click(881, 671)
        time.sleep(1)
        
        # 启动模拟粘贴操作
        start_simulation()
        
        # 等待粘贴操作完成
        paste_completed.wait()
        paste_completed.clear()  # 重置粘贴操作完成的事件
        
        print("模拟鼠标点击坐标（140，58）")
        pyautogui.click(140, 58)
        time.sleep(1)
        print("模拟鼠标向下移动100")
        pyautogui.move(0, 100)
        time.sleep(1)
        print("滑动滚轮向上滚动255")
        pyautogui.scroll(-255)

def add_entry(entries, scrollable_frame):
    entry = tk.Entry(scrollable_frame)
    entry.pack(pady=5)
    entries.append(entry)
# 创建提示框并设置隐藏时间
def show_message_box(message):
    msg_window = tk.Toplevel(root)
    msg_window.title("提示")
    msg_label = tk.Label(msg_window, text=message)
    msg_label.pack(padx=20, pady=10)
    root.after(1000, msg_window.destroy) 

# 创建 GUI 界面
root = tk.Tk()
root.title("dy自动评论")

# 创建一个框架来放置输入框，并添加垂直滚动条
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

entries = []
for i, text in enumerate(text_list):
    entry = tk.Entry(scrollable_frame)
    entry.insert(0, text)  # 设置输入框的默认值为text_list中的对应值
    entry.pack(pady=5)
    entries.append(entry)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# 添加新增按钮
add_button = tk.Button(root, text="新增", command=lambda: add_entry(entries, scrollable_frame))
add_button.pack(pady=10)

# 添加开始按钮
start_button = tk.Button(root, text="半自动执行一轮评论", command=lambda: start_once_task(entries))
start_button.pack(pady=10)

# 添加开始任务按钮
task_button = tk.Button(root, text="开始全自动评论", command=lambda: start_task(entries))
task_button.pack(pady=10)

# 添加停止任务按钮
stop_button = tk.Button(root, text="停止", command=stop_task)
stop_button.pack(pady=10)

# 运行 GUI 主循环
root.mainloop()
