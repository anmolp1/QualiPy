import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    """Set up the application logging configuration."""
    # Create logger
    logger = logging.getLogger('QualiPyLogger')
    logger.setLevel(logging.INFO)  # Set the logging level to INFO

    # Create file handler which logs even debug messages
    fh = RotatingFileHandler('qualipy.log', maxBytes=1024*1024*5, backupCount=5)  # 5 MB per file, max 5 files
    fh.setLevel(logging.INFO)  # Set file handler level

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)  # Set console handler level

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logging()
    logger.info('Starting the QualiPy application...')
    logger.error('This is an error message (will appear in both log file and console)')
    logger.info('Performing an operation...')
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        logger.exception('Exception occurred: Division by zero')
    logger.info('Finished operation.')
