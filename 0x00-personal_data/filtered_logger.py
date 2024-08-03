import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Filters a log line."""
    return re.sub(
        r'({}=)[^{}]+'.format('|'.join(fields), separator),
        r'\1' + redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"

    def __init__(self, fields):
        """Constructor init"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format Method"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), ";")
