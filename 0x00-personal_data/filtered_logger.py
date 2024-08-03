#!/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """Filters a log line.
    """
    pattern = f"{separator}({separator.join(fields)}=[^;]*)"
    return re.sub(
                pattern,
                lambda m: f"{separator}{m.group(1).split('=')[0]}={redaction}",
                message
    )
