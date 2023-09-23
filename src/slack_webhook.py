# coding:utf-8
# ---------------------------------------------------------------------------
# __author__ = 'Satoshi Imai'
# __credits__ = ['Satoshi Imai']
# __version__ = '0.9.0'
# ---------------------------------------------------------------------------

import json
import logging

import requests


class SlackWebhookHandler(logging.Handler):
    def __init__(self, hook_url: str = None,
                 username: str = None, icon: str = None, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)

        self.username = 'SlackWebhookHandler'
        self.icon = ':envelope_with_arrow:'

        if hook_url:
            self._set_hook_url(hook_url)
            # end if

        if username:
            self._set_username(username)
            # end if

        if icon:
            self._set_icon(icon)
            # end id
        # end def

    # hook_url
    def _get_hook_url(self):
        return self._hook_url
        # end def

    def _set_hook_url(self, value):
        self._hook_url = value
        # end def

    hook_url = property(
        fget=_get_hook_url,
        fset=_set_hook_url
    )

    # username
    def _get_username(self):
        return self._username
        # end def

    def _set_username(self, value):
        self._username = value
        # end def

    username = property(
        fget=_get_username,
        fset=_set_username
    )

    # icon
    def _get_icon(self):
        return self._icon
        # end def

    def _set_icon(self, value):
        self._icon = value
        # end def

    icon = property(
        fget=_get_icon,
        fset=_set_icon
    )

    def emit(self, record):
        try:
            msg = self.format(record)
            fs = '%s\n'

            requests.post(self.hook_url,
                          data=json.dumps({
                              'text': fs % msg,
                              'username': self.username,
                              'icon_emoji': self.icon,
                              'link_names': 1,
                          }))

            # print(fs % msg)
        except Exception:
            self.handleError(record)
            # end try
        # end def

    @staticmethod
    def notify(hook_url: str, message: str, username: str,
               icon: str, link_names: bool = True):
        fs = '%s\n'

        param = {
            'text': fs % message,
            'username': username,
            'icon_emoji': icon
        }

        if link_names:
            param['link_names'] = 1
            # end if

        requests.post(hook_url,
                      data=json.dumps(param))
        # end def
