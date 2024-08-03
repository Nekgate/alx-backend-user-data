import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Filters a log line by redacting specified fields."""
    return re.sub(
        r'({}=)[^{}]+'.format('|'.join(fields), separator),
        r'\1' + redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class that hides PII fields in logs."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"

    def __init__(self, fields):
        """Initialize with a list of fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record and redact PII fields."""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), ";")


# Define PII_FIELDS as a tuple of fields considered PII
PII_FIELDS = ("email", "phone", "ssn", "password", "last_login")


def get_logger() -> logging.Logger:
    """Create and configure a logger with RedactingFormatter."""
    from filtered_logger import RedactingFormatter

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler and set the RedactingFormatter
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger
