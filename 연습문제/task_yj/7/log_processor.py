# 나중에 자세히 공부할 것
import logging
import os

def setup_logging(log_file="my_application.log", level=logging.INFO):
    """
    Args:
        log_file (str): The name of the log file.
        level (int): The minimum logging level to capture (e.g., logging.INFO, logging.DEBUG).
    """
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def generate_sample_logs(logger):

    logger.debug('디버깅 메시지')
    logger.info('정보 메시지')
    logger.warning('경고 메시지')
    logger.error('에러 메시지')
    logger.critical('심각한 오류 메시지')

def read_and_filter_log(log_file, filter_level_name):
    """
    Args:
        log_file (str): The path to the log file.
        filter_level_name (str): The name of the log level to filter by (e.g., "INFO", "WARNING").
    """
    print(f"\n--- Filtering log for level: {filter_level_name} ---")
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if f" - {filter_level_name} - " in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")

if __name__ == "__main__":
    log_filename = "my_application.log"

    # Clean up previous log file if it exists
    if os.path.exists(log_filename):
        os.remove(log_filename)

    my_logger = setup_logging(log_file=log_filename, level=logging.INFO)
    print(f"Generating logs to '{log_filename}' and console with INFO level and above...")
    generate_sample_logs(my_logger)

    read_and_filter_log(log_filename, "INFO")
    read_and_filter_log(log_filename, "WARNING")
    read_and_filter_log(log_filename, "ERROR")
    read_and_filter_log(log_filename, "DEBUG")