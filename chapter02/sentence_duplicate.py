#! /usr/bin/env python3
sentence = input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width +2
left_margin = (screen_width - box_width) // 2
print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '|' + sentence + '|')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print()
# zhengjuns-MacBook-Pro:chapter02 zhengjun$ /Users/zhengjun/Desktop/PythonBeginning/chapter02/sentence_duplicate.py
# Sentence:Fake News!
#
#                                   +----------+
#                                   |          |
#                                   |Fake News!|
#                                   |          |
#                                   +----------+
#