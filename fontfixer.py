#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 zlsun <zlsun1995@gmail.com>
#
# Distributed under terms of the MIT license.

from __future__ import print_function
import config


def field(name):
    return '"/*[[{}]]*/"'.format(name)


def with_region(f, r):
    return '{}-{}'.format(f, r) if r else f


def ur(b, e):
    return 'U+{:04x}-{:04x}'.format(b, e)


def holder(f, r):
    return field(with_region(f, r))


def force_holder(f):
    return field(f + '-force')


def split(s):
    s = [i.strip() for i in s.splitlines()]
    while '' in s:
        s.remove('')
    return s

ranges = {k: ur(*v) for k, v in config.ranges.items()}
pref = {}
keep = {}
for k, v in config.__dict__.items():
    if '__' not in k and '_' in k:
        a, b = k.split('_')
        globals()[a][b] = split(v)

fonts = sum(pref.values(), [])
base = pref.keys()
regions = keep.keys()
weights = ['', 'bold', 'italic']


def font_face(font, region, holder, weight=None):
    font_family = 'font-family: {};'.format(font)
    unicode_range = 'unicode_range: {};'.format(ranges[region])
    src = 'src: local({});'.format(holder)
    l = [font_family, unicode_range, src]
    if weight:
        font_weight = 'font-weight: {};'.format(weight)
        l.append(font_weight)
    n = [35, 30, 35, 20]
    l = ['{{:{}}}'.format(i).format(j) for i, j in zip(n, l)]
    print('@font-face {{ {} }}'.format(' '.join(l)))


def selector(name, f):
    font_family = ', '.join(holder(f, r) for r in regions)
    print('{:8} {{ font-family: {} {}; }}'
          .format(name, font_family, force_holder(f)))


def hr():
    print()


def prefer(font, region):
    if font in keep[region]:
        return font
    for p, fs in pref.items():
        if font in fs:
            return holder(p, region)
    return font


if __name__ == '__main__':
    for f in fonts:
        for r in regions:
            for w in weights:
                p = prefer(f, r)
                if p != f:
                    font_face(f, r, p, w)
    hr()
    for s in 'PRE TEXTAREA CODE'.split():
        selector(s, 'mono')
