import logging


def get_logger(name, level=logging.WARNING):
    """Get logger with predefined formatter set"""

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a handler
    handler = logging.StreamHandler()
    handler.setLevel(level)
    logger.addHandler(handler)

    # Create a formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    return logger