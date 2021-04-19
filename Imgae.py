from urllib.request import Request, urlopen
import json

api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'

hds = {'User-Agent': 'Mozilla/5.0'}

request = Request(api_url, headers=hds)
response = urlopen(request)
directory_bytes = response.read()
directory_str = directory_bytes.decode('utf-8')

contents = json.loads(directory_str)

for i in range(len(contents)):
    content = contents[i]
    print(content['download_url'])
    break

