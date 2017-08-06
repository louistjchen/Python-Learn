import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:

    url = input('Enter url: ')
    if(len(url) < 1): break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data.decode())
    counts = tree.findall('.//count')
    print('count:', len(counts))

    total = 0
    for count in counts:
        total = total + int(count.text)
    print('sum', total)
