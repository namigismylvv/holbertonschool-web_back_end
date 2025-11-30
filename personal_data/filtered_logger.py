#!/usr/bin/env python3
"""
Module to redact sensitive data from logs.

This module contains a formatter and logger setup for securely
obfuscating Personally Identifiable Information (PII) in logs.
"""

import os
from typing import List
import re
import logging
import mysql.connector
from mysql.connector import connection


# Define PII_FIELDS constant
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class.

    This formatter obfuscates specific fields in log messages to
    protect sensitive data.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor method."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redacting Formatter method."""
        original_message = super().format(record)
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): Fields to redact.
        redaction (str): Redaction string to use.
        message (str): Log message to process.
        separator (str): Separator for fields.

    Returns:
        str: Obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message
    )


def get_logger() -> logging.Logger:
    """
    Configures and returns a logger for user data.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a handler with RedactingFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger


def get_db() -> connection.MySQLConnection:
    """
    Returns a connector to the database.

    Uses environment variables for database credentials.
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main():
    """Main function."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    [print(user) for user in cursor]
    logger = get_logger()
    for user in cursor:
        user_info = (
            f"name={user[0]}; email={user[1]}; phone={user[2]}; "
            f"ssn={user[3]}; password={user[4]}; ip={user[5]}; "
            f"last_login={user[6]}; user_agent={user[7]};"
        )
        logger.info(user_info)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
