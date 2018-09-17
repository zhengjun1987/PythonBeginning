# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter10/hello.py #  1
# Author:Zheng Jun                                 #  2
# Date:2018/9/16 07:31                             #  3
# E-mail:zhengjun1987@outlook.com                  #  4
                                                   #  5
import sys, pprint                                 #  6
                                                   #  7
                                                   #  8
def say():                                         #  9
    print("Hello, world!")                         # 10
    pprint.pprint(sys.path)                        # 11
    print(f"say : sys.platform = {sys.platform}")  # 12
                                                   # 13
                                                   # 14
def test():                                        # 15
    print(f"test() running!")                      # 16
    say()                                          # 17
                                                   # 18
                                                   # 19
if __name__ == '__main__':                         # 20
    test()                                         # 21
                                                   # 22
__all__ = [test, say]                              # 23
                                                   # 24
# test()                                           # 25
                                                   # 26
# import sys, pprint                               # 27
# pprint.pprint(sys.path)                          # 28
# ['/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', # 29
#  '/Applications/PyCharm '                        # 30
#  'CE.app/Contents/plugins/python-ce/helpers/third_party/thriftpy', # 31
#  '/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev', # 32
#  '/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', # 33
#  '/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9', # 34
#  '/usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', # 35
#  '/usr/local/lib/python3.9/site-packages',       # 36
#  '/Users/zhengjun/Desktop/PythonBeginning']      # 37
                                                   # 38
# zhengjuns-MacBook-Pro:PythonBeginning zhengjun$ python3 hello.py # 39
# test() running!                                  # 40
# Hello, world!                                    # 41
# ['/Users/zhengjun/Desktop/PythonBeginning',      # 42
#  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', # 43
#  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', # 44
#  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', # 45
#  '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/site-packages'] # 46
# say : sys.platform = darwin                      # 47
