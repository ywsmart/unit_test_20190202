# -*- coding: utf-8 -*-
# Created by yawa1hz1 on 2019/2/2 15:46.
from xpinyin import Pinyin
import pytest

p = Pinyin()


def test_pinyin():
    assert p.get_pinyin(u"杭州") == "hang-zhou"


def test_pinyin2():
    assert p.get_pinyin(u"杭州", '') == "hangzhou"
