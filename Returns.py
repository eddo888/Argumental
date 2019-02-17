#!/usr/bin/env python3


class Returns(object):
    """
    defines the return settings for a method
    """
    def __init__(self, _help=None, _type=str):
        self.help = _help
        self.type = _type
