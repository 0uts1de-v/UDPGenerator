# -*- coding:utf-8 -*-

import time
import socket
import tkinter as tk


def udp_send():
    sent = True  # 送れたか
    msg = DataBox.get()  # 送るメッセージ
    try:
        num = int(NumBox.get())  # 送る数
    except:
        Send["text"] = "Wrong Num"
        return

    try:
        delay_time = float(DelayBox.get())  # 遅延時間
    except:
        Send["text"] = "Wrong Delay"
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    Send["text"] = "Sending..."
    Send["command"] = ""

    for i in range(0, num):
        try:
            client.sendto(msg.encode(), (IpBox.get(), int(PortBox.get())))
            sent = True
        except:
            sent = False
            break
        Send.update()
        time.sleep(delay_time)

    if sent == True:
        Send["text"] = "Send!"
    else:
        Send["text"] = "Wrong IP"
    Send["command"] = udp_send


# UDP送信関数


root = tk.Tk()  # ウィンドウ作成
root.title("UDP Packet Generator")  # ウィンドウタイトル
root.geometry("640x480")  # ウィンドウサイズ

Ip = tk.Label(root, text="IP:", font=("Consolas", "13"))
Port = tk.Label(root, text="Port:", font=("Consolas", "13"))
Delay = tk.Label(root, text="Delay:", font=("Consolas", "13"))
Data = tk.Label(root, text="Data:", font=("Consolas", "13"))
Num = tk.Label(root, text="Num:", font=("Consolas", "13"))

IpBox = tk.Entry(font=("Consolas", "30"))
PortBox = tk.Entry(font=("Consolas", "30"))
DelayBox = tk.Entry(font=("Consolas", "30"))
DataBox = tk.Entry(font=("Consolas", "30"))
NumBox = tk.Entry(font=("Consolas", "30"))

IpBox.insert(tk.END, "192.168.1.1")
PortBox.insert(tk.END, "9998")
DelayBox.insert(tk.END, "0")
NumBox.insert(tk.END, "1")
# 部品の作成


Ip.place(height=60, y=30)
Port.place(height=60, y=150)
Delay.place(height=60, y=270)
Data.place(height=60, y=390)
Num.place(height=60, x=440, y=390)

IpBox.place(height=60, width=360, x=60, y=30)
PortBox.place(height=60, width=360, x=60, y=150)
DelayBox.place(height=60, width=360, x=60, y=270)
DataBox.place(height=60, width=360, x=60, y=390)
NumBox.place(height=60, width=120, x=500, y=390)
# 部品の配置


Send = tk.Button(root, text="Send!", font=("Consolas", "20"))
Send["command"] = udp_send
Send.place(height=300, width=185, x=440, y=30)
# 送信ボタン

root.mainloop()
