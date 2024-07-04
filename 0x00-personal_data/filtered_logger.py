#!/usr/bin/env python3
"""A module for filtering logs.
"""
import re

def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join([f'{field}=[^ {separator}]+' for field in fields])
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}", message)


if __name__ == "__main__":
    main()