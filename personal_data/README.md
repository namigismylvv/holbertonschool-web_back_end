# Personal Data Management

This project demonstrates how to handle personal data securely in a web backend environment. It includes examples of logging, database management, and password encryption.

## Files

- `main.sql`: SQL script to set up the database and insert sample data.
- `user_data.csv`: CSV file containing sample user data.
- `1-main.py`: Script demonstrating the use of a custom logging formatter to redact sensitive information.
- `2-main.py`: Script demonstrating the use of a custom logger.
- `3-main.py`: Script demonstrating database connection and querying.
- `4-main.py`: Script demonstrating password hashing.
- `5-main.py`: Script demonstrating password validation.
- `filtered_logger.py`: Module containing the custom logging formatter and logger setup.
- `encrypt_password.py`: Module containing functions for password hashing and validation.

## Setup

1. **Database Setup**:
    - Run the `main.sql` script to set up the database and insert sample data.

2. **Environment Variables**:
    - Set the following environment variables for database connection:
      - `PERSONAL_DATA_DB_USERNAME`: Database username (default: `root`)
      - `PERSONAL_DATA_DB_PASSWORD`: Database password (default: empty)
      - `PERSONAL_DATA_DB_HOST`: Database host (default: `localhost`)
      - `PERSONAL_DATA_DB_NAME`: Database name

## Usage

- **Logging**:
  - Use the `RedactingFormatter` class from `filtered_logger.py` to redact sensitive information in logs.
  - Example usage can be found in `1-main.py` and `2-main.py`.

- **Database**:
  - Use the `get_db` function from `filtered_logger.py` to connect to the database.
  - Example usage can be found in `3-main.py`.

- **Password Encryption**:
  - Use the `hash_password` and `is_valid` functions from `encrypt_password.py` for password hashing and validation.
  - Example usage can be found in `4-main.py` and `5-main.py`.

## License

This project is licensed under the MIT License.