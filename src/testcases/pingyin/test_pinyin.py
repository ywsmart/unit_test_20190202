# -*- coding: utf-8 -*-
# Created by yawa1hz1 on 2019/2/2 15:46.
# 执行命令：pytest -v src\testcases\pingyin\test_pinyin.py --cov=src/xpinyin

from src.xpinyin import Pinyin
import pytest


class TestPinyin:
    p = Pinyin()

    data_get_pinyin = [(u'杭州', '', 'hang-zhou'), (u'杭州', 'marks', 'háng-zhōu'), (u'杭州', 'numbers', 'hang2-zhou1'),
                       ('hangzhou', '', 'hangzhou'), ]
    data_get_initial = [(u'杭', 'H')]
    data_get_initials = [(u'杭州', 'H-Z')]

    @pytest.mark.parametrize('chars,tone_marks,expected', data_get_pinyin)
    def test_pinyin(self, chars, tone_marks, expected):
        assert self.p.get_pinyin(chars=chars, tone_marks=tone_marks) == expected

    @pytest.mark.parametrize('char,expected', data_get_initial)
    def test_pinyin2(self, char, expected):
        assert self.p.get_initial(char=char) == expected

    @pytest.mark.parametrize('chars,expected', data_get_initials)
    def test_pinyin3(self, chars, expected):
        assert self.p.get_initials(chars=chars) == expected
