#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

def sam_is_a_nonce():
    print("\n\nSam is a nonce\n\n")
    return True

def test_if_sam_is_a_nonce():
    assert sam_is_a_nonce() == True
