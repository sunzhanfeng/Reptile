import random
import threading
import tkinter
import time
from pynput.keyboard import Controller, Key, Listener
import easygui as g


class helpthread(threading.Thread):
    def run(self):
        self.help()

    def help(self):
        # 创建对象
        win = tkinter.Tk()
        screen_height = win.winfo_screenheight()
        screen_width = win.winfo_screenwidth()
        # print("你电脑的屏幕的高度是：", screen_height)
        # print("你电脑的屏幕的宽度度是：", screen_width)
        # 设置窗体的大小（300x300），与出现的位置距离窗体左上角（+150+150）
        h = random.randint(0, screen_width-500)
        w = random.randint(0, screen_height-100)
        win.geometry("300x50+{}+{}".format(h, w))
        # frm1 = tkinter.Frame(win)
        # frm1.pack_propagate(0)
        # frm_l = tkinter.Frame(win)
        
        # win：父窗体
        # text：显示的文本内容
        # bg：背景色
        # fg：字体颜色
        # font：字体
        # wraplength：指定text文本中多宽之后换行
        # justify：设置换行后的对齐方式
        # anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
        label = tkinter.Label(win,
                              text="HELLO IDIOT！！！",
                              bg="pink", fg="red",
                              font=("黑体", 20),
                              # width=30,
                              # height=10,
                              wraplength=300,
                              justify="left",
                              anchor="center")
        # 显示
        label.pack()
        # 进入消息循环，显示窗体
        win.mainloop()


def xianshi():
    a = g.integerbox(msg="输入次数10-100000", title="显示", lowerbound=10, upperbound=100000)
    # print(type(a))
    return a


def xuhaun(i):
    for a in range(i):
        time.sleep(0.1)
        a = helpthread()
        a.start()


# 监听释放
def on_release(key):
    # print("已经释放:", format(key))

    if key == Key.esc:
        # 停止监听
        return False


def start_listen():
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    kb = Controller()
    i = xianshi()
    thred1 = threading.Thread(target=xuhaun, args=(i,), daemon=True)
    thred1.start()
    start_listen()
    print('end')


