import re

def extract_url(string):
    result = re.search('<(.*)>; rel="next"', string)
    return result.group(1)