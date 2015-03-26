from py.html.sanitizer import Sanitizer
import sys
import requests

d = ''
if len(sys.argv) > 1:
    d = requests.get(sys.argv[1]).text
else:
    with open('py/test/fixture.html') as f:
        d = f.read()

sanitizer = Sanitizer()
print(sanitizer.sanitize(d))