#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 98 and ord(c) <= 106:
        return True
    else:
        return False

