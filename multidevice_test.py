import tkinter as tk
import subprocess
import time
import random
from threading import Thread

def adb_shell(command, device=None):
    """执行 adb shell 命令并返回输出"""
    adb_command = ['adb']
    if device:
        adb_command += ['-s', device]
    adb_command += ['shell', command]
    result = subprocess.run(adb_command, capture_output=True, text=True)
    return result.stdout.strip()

def tap_screen(device, x, y):
    """模拟屏幕点击事件"""
    adb_shell(f'input tap {x} {y}', device)
    print(f"设备 {device} ---点击屏幕：({x}, {y})")

def swipe_screen(device, start_x, start_y, end_x, end_y, duration_ms):
    """模拟屏幕滑动事件"""
    adb_shell(f'input swipe {start_x} {start_y} {end_x} {end_y} {duration_ms}', device)
    print(f"设备 {device} ---滑动屏幕：从 ({start_x}, {start_y}) 到 ({end_x}, {end_y})，持续时间：{duration_ms} 毫秒")

def process_events(device):
    """Define a loop to continuously execute a sequence of events"""
    while True:
        # Example sequence of events
        tap_screen(device, 400, 666)  # Example tap at (100, 200)
        time.sleep(6)  # Delay between events

         # Randomly select one of 10 operations with equal probability (1/10 chance for each)
         #999  1266 1658
        # tap_screen(device, 999, 1266)  # 点赞
        # tap_screen(device, 999, 1658)  # 收藏

        operation = random.randint(1, 10)
        # Switch-like structure to execute different operations based on random selection
        if operation == 1:
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(10)  # Delay between events
        elif operation == 2:
            time.sleep(3)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(12)  # Delay between events
        elif operation == 3:
            time.sleep(3)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(12)  # Delay between events
        elif operation == 4:
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(12)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(10)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(5)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(20)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(25)  # Delay between events
        elif operation == 5:
            pass
        elif operation == 6:
            pass
        elif operation == 7:
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(12)  # Delay between events
            time.sleep(3)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(10)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(5)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(11)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(12)  # Delay between events
            randint_like = random.randint(1, 10)
            if randint_like == 6:
                tap_screen(device, 999, 1266)  # 点赞

            time.sleep(3)  # Delay between events
        elif operation == 8:
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(5)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(4)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(5)  # Delay between events
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(7)  # Delay between events
            randint_collect = random.randint(1, 10)
            if randint_collect == 9:
                tap_screen(device, 999, 1658)  # 收藏            
            swipe_screen(device, 400, 999, 400, 666, 200)  # 下一个
            time.sleep(3)  # Delay between events
        elif operation == 9:
            # 点击输入框
            # 点击键盘
            # 点击键盘
            # 点击键盘文本
            # 回车发送
            # 然后下一个或者返回
            # 回头写评论
            pass
        elif operation == 10:
            # 回头写评论
            pass
        time.sleep(1)  # Delay between events
        tap_screen(device, 150, 150)  # 返回
        random_number = random.randint(3, 25) # 随机数字
        time.sleep(random_number)  # Delay between events
        swipe_screen(device, 400, 999, 400, 666, 200) # 滚动
        time.sleep(1)  # Delay between events
        swipe_screen(device, 400, 999, 400, 666, 200) # 滚动
        time.sleep(5)  # Delay between events

        # Add more events here as needed...
def only_roll_events(device):
    while True:
        randint_begin = random.randint(3, 20)
        time.sleep(randint_begin)  # Delay between events

        randint_zan = random.randint(1, 50)# 是否点赞概率
        if randint_zan == 66:
            tap_screen(device, 999, 1080)  # 点赞
            randint_zan_delay = random.randint(3, 10)
            time.sleep(randint_zan_delay)  # Delay between events

        randint_shou = random.randint(1, 150)# 是否收藏概率
        if randint_shou == 66:
            tap_screen(device, 999, 1480)  # 点赞
            randint_shou_delay = random.randint(3, 10)
            time.sleep(randint_shou_delay)  # Delay between events

        swipe_screen(device, 400, 999, 400, 666, 200) # 滚动

def on_start_button_click(devices):
    """点击开始按钮后，为每台设备启动一个新线程执行事件处理循环"""
    threads = []
    for device in devices:
        thread = Thread(target=process_events, args=(device,))
        thread.start()
        threads.append(thread)

    # 等待所有线程结束
    for thread in threads:
        thread.join()
def on_start_roll_click(devices):
    """点击开始按钮后，为每台设备启动一个新线程执行事件处理循环"""
    threads = []
    for device in devices:
        thread = Thread(target=only_roll_events, args=(device,))
        thread.start()
        threads.append(thread)

    # 等待所有线程结束
    for thread in threads:
        thread.join()
def main():
    # 获取已连接的设备列表
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    devices = [line.split('\t')[0] for line in result.stdout.splitlines()[1:] if line.strip() != '']

    if not devices:
        print("未检测到已连接的安卓设备。")
        return

    # 创建 GUI 界面
    root = tk.Tk()
    root.title("手机操作模拟器")

    # 添加设备选择多选框
    selected_devices = []
    for device in devices:
        device_var = tk.BooleanVar(value=False)
        checkbox = tk.Checkbutton(root, text=device, variable=device_var)
        checkbox.pack(anchor=tk.W)
        selected_devices.append((device, device_var))

    def start_button_click():
        selected = [device for device, var in selected_devices if var.get()]
        if selected:
            on_start_button_click(selected)
        else:
            print("请选择要操作的设备。")

    # 添加开始按钮
    start_button = tk.Button(root, text="首页开始自动操作", command=start_button_click)
    start_button.pack(pady=20)

    def start_roll_click():
        selected = [device for device, var in selected_devices if var.get()]
        if selected:
            on_start_roll_click(selected)
        else:
            print("请选择要操作的设备。")
    # 添加滚动按钮
    roll_button = tk.Button(root, text="精选开始自动操作", command=start_roll_click)
    roll_button.pack(pady=20)
    # 运行 GUI 主循环
    root.mainloop()

if __name__ == '__main__':
    main()
