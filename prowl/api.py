from urllib import request, parse
# import xml.etree.ElementTree as ET


class Prowl(object):

    def __init__(self, api_key, application=None):
        self.api_key = api_key
        self.application = application
        self.end_point = "https://api.prowlapp.com/publicapi/"

    def verify(self):
        resp = request.urlopen(
            "{ep}/verify?{key}".format(
                ep=self.end_point,
                key=parse.urlencode({"apikey": self.api_key}))
        )

        return resp.read().decode("utf-8")

    def send_message(self, title, message, priority=0, url=None):

        data = {
            "apikey": self.api_key,
            "event": title,
            "description": message,
            "priority": priority,
            "application": self.application,
            "url": url
        }

        req = request.Request(
            "{}/add".format(self.end_point),
            data=parse.urlencode(data).encode(),
            method="POST"
        )

        resp = request.urlopen(req)

        return resp.read().decode("utf-8")
