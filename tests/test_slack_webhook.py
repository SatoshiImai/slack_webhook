# coding:utf-8
# ---------------------------------------------------------------------------
# __author__ = 'Satoshi Imai'
# __credits__ = ['Satoshi Imai']
# __version__ = "0.9.0"
# ---------------------------------------------------------------------------

import logging
from logging import Logger, StreamHandler
from typing import Generator
from unittest.mock import patch

import pytest

from src import slack_webhook
from src.slack_webhook import SlackWebhookHandler


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown():
    # setup

    yield

    # teardown
    # end def


@pytest.fixture(scope='module')
def logger() -> Generator[Logger, None, None]:
    log = logging.getLogger(__name__)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
    s_handler = StreamHandler()
    s_handler.setLevel(logging.INFO)
    s_handler.setFormatter(formatter)
    log.addHandler(s_handler)

    yield log
    # end def


@pytest.mark.run(order=10)
def test_init_and_handling(logger: Logger):
    logger.info('test_init_and_handling')

    slack_formatter = logging.Formatter(
        '@channel\n%(asctime)s - %(levelname)s : %(message)s')

    slack_handler = SlackWebhookHandler('https://dummy_url',
                                        'dummy username',
                                        ':skull_and_crossbones:', logging.WARNING)
    slack_handler.setFormatter(slack_formatter)
    logger.addHandler(slack_handler)

    with patch.object(slack_webhook.requests, 'post'):
        logger.critical('test')
        # end with
    # end def


@pytest.mark.run(order=20)
@pytest.mark.parametrize('property', [('hook_url'),
                         ('username'), ('icon')])
def test_get_property(property: str, logger: Logger):
    logger.info('test_get_property')

    slack_handler = SlackWebhookHandler('https://dummy_url',
                                        'dummy username',
                                        ':your_icon:', logging.WARNING)

    logger.info(getattr(slack_handler, property))
    # end def


@pytest.mark.run(order=30)
def test_notify(logger: Logger):
    logger.info('test_notify')

    with patch.object(slack_webhook.requests, 'post'):
        SlackWebhookHandler.notify(
            'https://dummy_url',
            'main message',
            'dummy username',
            ':your_icon:',
            True)
        # end with
    # end def


@pytest.mark.run(order=40)
def test_catch_exception(logger: Logger):
    logger.info('test_catch_exception')

    slack_formatter = logging.Formatter(
        '@channel\n%(asctime)s - %(levelname)s : %(message)s')

    slack_handler = SlackWebhookHandler('this is not url',
                                        'dummy username',
                                        ':skull_and_crossbones:', logging.WARNING)
    slack_handler.setFormatter(slack_formatter)
    logger.addHandler(slack_handler)

    logger.critical('test')
    # end def
