#!/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """Filters a log line.
    """
    return re.sub(
        r'({}=)[^{}]+'.format('|'.join(fields),
                              separator), r'\1' + redaction, message
    )
