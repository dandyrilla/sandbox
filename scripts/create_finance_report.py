"""
A cron job script for creating a finance report.
"""

import logging
import os

from sandbox.utils.logging import get_logger

logger = get_logger(__name__, level=logging.INFO)


def main():

    logger.info('Environment variables:')
    for k, v in os.environ.items():
        logger.info(f'- {k}: {v}')


if __name__ == '__main__':
    main()
