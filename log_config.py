import logging

# Create a handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create a formatter
default_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the handler
handler.setFormatter(default_formatter)

def get_root_logger():
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def get_game_logger():
    """Not Implemented Yet"""
    raise NotImplementedError()