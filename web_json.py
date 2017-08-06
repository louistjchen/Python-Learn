import urllib.request, urllib.parse, urllib.error
import json

while True:

    url = input("Enter location: ")
    if(len(url) < 1): break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    total = 0
    info = json.loads(data)
    print('Count', len(info['comments']))
    for person in info['comments']:
        total = total + person['count']
    print('Sum:', total)
