# https://leetcode.com/problems/encode-and-decode-tinyurl/submissions/1404722903/
from pickle import dumps, loads


class Codec:
    def encode(self, longUrl):
        return dumps(longUrl)

    def decode(self, shortUrl):
        return loads(shortUrl)
