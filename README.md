# slack_webhook

A simple slack webhook caller for Python project.
It has SlackWebhookHandler for logging and a simple message post static method.

## Adding custom handler

```python
import logging

from slack_webhook import SlackWebhookHandler


my_logger = logging.getLogger(__name__)

# add handler
slack_formatter = logging.Formatter(
    '@channel\n%(asctime)s - %(levelname)s : %(message)s')

slack_handler = SlackWebhookHandler('https://set_your_webhook',
                                    'test send',
                                    ':your_icon:')

slack_handler.setLevel(logging.WARNING)
slack_handler.setFormatter(slack_formatter)
my_logger.addHandler(slack_handler)

# log
my_logger.critical('critical message')
```

## Simple message post

```python
from slack_webhook import SlackWebhookHandler

# call static method
SlackWebhookHandler.notify(
    'https://set_your_webhook',
    'main message',
    'dummy username',
    ':your_icon:',
    True)
```

## LICENSE

I inherited Apache License 2.0 from [requests](https://requests.readthedocs.io/en/latest/).
