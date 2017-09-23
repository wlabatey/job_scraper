#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

def example():
    print("\n\nThis is just an example test\n\n")
    return True

def test_example():
    assert example() == True
