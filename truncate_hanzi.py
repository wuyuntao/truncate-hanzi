# -*- coding: UTF-8 -*-

import re
from django.utils.encoding import force_unicode
from django.utils.functional import allow_lazy

# Set up regex for alphanumeric characters
# \u00c0-\u02af: Latin
# \u0370-\u1fff: Greek and other language alphabet characters
re_alnum = re.compile(ur'[a-zA-Z0-9_\-\u00c0-\u02af\u0370-\u1fff]+', re.U)
# Set up regex for hanzi
# \u3040-\ufaff: CJK characters
re_hanzi = re.compile(ur'[\u3040-\ufaff]+', re.U)

def len_hanzi(s):
    s = force_unicode(s)
    length = 0
    # Length of alphanumeric characters
    length += len(re_alnum.findall(s))
    # Length of CJK characters
    for h in re_hanzi.findall(s):
        length += len(h)
    return length
len_hanzi = allow_lazy(len_hanzi, unicode)

def truncate_hanzi(s, num):
    s = force_unicode(s)
    length = int(num)
    if length <= 0:
        return u'...'
    hanzi = u''
    hanzi_len = 0
    word_temp = u''
    for char in s:
        # Check for alphabet characters
        if re_alnum.match(char):
            word_temp += char
            continue
        # Check for word temp
        if word_temp:
            hanzi += word_temp
            hanzi_len += 1
            word_temp = ''
        # Check for length
        if hanzi_len >= length:
            if not hanzi.endswith('...'):
                hanzi += '...'
                break
        # Check for hanzi
        if re_hanzi.match(char):
            hanzi_len += 1
        hanzi += char
    hanzi += word_temp
    return hanzi
truncate_hanzi = allow_lazy(truncate_hanzi, unicode)

def demo():
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 6)
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 11)
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 20)

if __name__ == '__main__':
    demo()
