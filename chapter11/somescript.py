# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter11/somescript.py
# Author:Zheng Jun
# Date:2018/9/17 23:19
# E-mail:zhengjun1987@outlook.com

import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)
# zhengjuns-MacBook-Pro:PythonBeginning zhengjun$ cat files/somefile.txt | python3 chapter11/somescript.py
# Wordcount: 11