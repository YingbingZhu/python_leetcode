#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/18
"""
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design a class to encode a URL and decode a tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Implement the Solution class:
#
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl.
# It is guaranteed that the given shortUrl was encoded by the same object.

from random import randint

class Codec:
    def __init__(self):
        self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.cache = {}


    def get_key(self):
        key = ''
        for _ in range(6):
            index = randint(len(self.charset))
            key += self.charset[index]
        return key

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = self.get_key()
        while key in self.cache:
            key = self.get_key()
        self.cache[key] = longUrl
        return "http://tinyurl.com/" + key


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[shortUrl.rindex('/') + 1:]
        if key in self.cache:
            return self.cache[key]
        else:
            return ""


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))