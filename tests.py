# -*- coding: UTF-8 -*-

import unittest
from truncate_hanzi import truncate_hanzi 

class TruncateHanziTestCase(unittest.TestCase):
    def testChinese(self):
        self.assertEqual(truncate_hanzi('公共的模' ,4), u'公共的模')
        self.assertEqual(truncate_hanzi('公共的模' ,3), u'公共的...')
        self.assertEqual(truncate_hanzi('公共的模' ,1), u'公...')
        self.assertEqual(truncate_hanzi('公共的模' ,0), u'...')

    def testEnglish(self): 
        self.assertEqual(truncate_hanzi('WOW! We Say ENGLISH!!!', 4), u'WOW! We Say ENGLISH...')
        self.assertEqual(truncate_hanzi('WOW! We Say ENGLISH!!!', 3), u'WOW! We Say...')
        self.assertEqual(truncate_hanzi('WOW! We Say ENGLISH!!!', 2), u'WOW! We...')
        self.assertEqual(truncate_hanzi('WOW! We Say ENGLISH!!!', 1), u'WOW...')

    def testWestern(self): 
        self.assertEqual(truncate_hanzi('αέβ Λğ Ґєʯ', 3), u'αέβ Λğ Ґєʯ')
        self.assertEqual(truncate_hanzi('αέβ Λğ Ґєʯ', 2), u'αέβ Λğ...')
        self.assertEqual(truncate_hanzi('αέβ Λğ Ґєʯ', 1), u'αέβ...')
        self.assertEqual(truncate_hanzi('αέβ Λğ Ґєʯ', 0), u'...')

    def testMixedText(self):
        self.assertEqual(truncate_hanzi(' 公 模asdf! hello 你好', 6), u' 公 模asdf! hello 你好')
        self.assertEqual(truncate_hanzi(' 公 模asdf! hello 你好', 5), u' 公 模asdf! hello 你...')
        self.assertEqual(truncate_hanzi(' 公 模asdf! hello 你好', 4), u' 公 模asdf! hello...')
        self.assertEqual(truncate_hanzi(' 公 模asdf! hello 你好', 3), u' 公 模asdf...')

        self.assertEqual(truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 11), u'截取段落工具，支持English、Γρεεκ等...')
        self.assertEqual(truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 10), u'截取段落工具，支持English、Γρεεκ...')
        self.assertEqual(truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 9), u'截取段落工具，支持English...')

if __name__ == '__main__':
    unittest.main()
