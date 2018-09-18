# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter12/text_editor.py
# Author:Zheng Jun
# Date:2018/9/18 10:49
# E-mail:zhengjun1987@outlook.com

import tkinter as tk

top = tk.Tk()   # 充当主窗口的顶级组件
btn = tk.Button()
btn.pack()      # 布局管理器（几何管理器）组织控件的位置
btn['text'] = 'Click me!'
tk.mainloop()   # 调用函数mainloop进入Tkinter主事件循环