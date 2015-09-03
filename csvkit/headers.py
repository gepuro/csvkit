#!/usr/bin/env python
# -*- coding:utf-8 -*-

def make_default_headers(n):
    """
    Make a set of simple, default headers for files that are missing them.
    """
    return ['column%i' % (i + 1) for i in range(n)]
