#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 zlsun <zlsun1995@gmail.com>
#
# Distributed under terms of the MIT license.

from __future__ import unicode_literals

ranges = {
    '': (0, 0x2e7f),
    'cjk': (0x2e80, 0xffff),
}

pref_sans = '''
    sans
    sans-serif
    arial
    Arial
    Arial Black
    Calibri
    Comic Sans MS
    Candara
    Constantia
    Corbel
    Helvetica
    Impact
    Lucida Sans
    Lucida Console
    Lucida Grande
    Palatino Linotype
    Segoe UI
    Tahoma
    Tahoma
    Trebuchet MS
    Verdana
    Verdana

    Simhei
    simsun Arial
    Arial SimSun
    STHeiti
    microsoft yahei
    黑体
    微软雅黑
    瀹嬩綋
'''

pref_serif = '''
    serif
    Cambria
    Georgia
    Liberation Serif
    Linux Libertine
    Linux Libertine 0
    Times New Roman
    Times
    Times CY

    Simsun
    Simsun
    NSimsun
    NSimsun
    MingLiU
    PMingLiU
    PMingLiU-ExtB
    MingLiU_HKSCS
    MingLiU_HKSCS-ExtB
    MingLiU-ExtB
    宋体
    宋體
    新宋体
    細明體
    新細明體
    细明体
    新细明体
'''

pref_mono = '''
    monospace
    Courier New
    Andale Mono
    Consolas
    Monaco
'''

keep_ = '''
    Arial Black
    Candara
    Comic Sans MS
    Trebuchet MS
    Verdana
'''

keep_cjk = '''
'''
