import requests

def sourcetemplate(url):
    def load(**kwargs):
        return requests.get(url.format_map(kwargs))
    return load

load = sourcetemplate('https://api.github.com/repositories?since={since}')
load(since=200).json()