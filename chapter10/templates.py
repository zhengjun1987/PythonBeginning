# FileName: /Users/zhengjun/Desktop/PythonBeginning/chapter10/templates.py
# Author:Zheng Jun
# Date:2018/9/17 20:49
# E-mail:zhengjun1987@outlook.com

import fileinput, re

field_pat = re.compile(r'\\[(.+?)\\]')

scope = {}

def replacement(match):
    """
    用于调用re.sub
    :param match:
    :return:
    """
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        return ''

lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print(field_pat.sub(replacement, text))
# re.compile('\\[([^\\]]+)\\]').sub(lambda mat: str(eval(mat.group(1),{})),"The sum of 7 and 9 is [7+9]")
# 'The sum of 7 and 9 is 16'