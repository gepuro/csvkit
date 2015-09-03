#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv

POSSIBLE_DELIMITERS = [',', '\t', ';', ' ', ':', '|']

def sniff_dialect(sample):
    """
    A functional version of ``csv.Sniffer().sniff``, that extends the
    list of possible delimiters to include some seen in the wild.
    """
    try:
        dialect = csv.Sniffer().sniff(sample, POSSIBLE_DELIMITERS)
    except:
        dialect = None

    return dialect

