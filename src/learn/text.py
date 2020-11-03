#! /usr/bin/env python3
# -*- code: utf-8 -*-

TEXT = input('value')

SCREEN_WIDTH = 80
TEXT_LENGTH = len(TEXT)
BOX_WIDTH = TEXT_LENGTH + 6
LEFT_MARGIN = (SCREEN_WIDTH - BOX_WIDTH) // 2

print()
print(' ' * LEFT_MARGIN + '+' + '-' * BOX_WIDTH + '+')
print(' ' * LEFT_MARGIN + '|' + '-' * BOX_WIDTH + '|')
print(' ' * LEFT_MARGIN + '|' + TEXT + '|')
print(' ' * LEFT_MARGIN + '|' + '-' * BOX_WIDTH + '|')
print(' ' * LEFT_MARGIN + '+' + '-' * BOX_WIDTH + '+')
print()
