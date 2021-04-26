from urllib.request import Request, urlopen
import json
import os


def image_download(url, filepath):
    request = Request(url)
    response = urlopen(request)

    image_data = response.read()

    file = open(filepath, 'wb')
    file.write((image_data))
    file.close()
    print(url + '로 부터' + filepath + '에 다운로드 완료')
    #url로 부터 경로에 다운로드 완료

mask_url = 'https://github.com/prajnasb/observations/raw/master/mask_classifier/Data_Generator/images/blue-mask.png'
image_download(mask_url, 'data/mask.png')
exit()


api_url = 'https://api.github.com/repos/prajnasb/observations/contents/experiements/data/without_mask?ref=master'

hds = {'User-Agent': 'Mozilla/5.0'}

request = Request(api_url, headers=hds)
response = urlopen(request)
directory_bytes = response.read()
directory_str = directory_bytes.decode('utf-8')

contents = json.loads(directory_str)

for i in range(len(contents)):
    content = contents[i]
    #print(content['download_url'])
    request = Request(content['download_url'])
    response = urlopen(request)
    image_data=response.read()

    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/without_mask'):
        os.mkdir('data/without_mask')

    image_file =  open('data/without_mask/' + content['name'], 'wb')
    image_file.write(image_data)
    print('다운로드 완료(' + str(i + 1) + '/' +  str(len(contents)) + '): ' + content['name'])
    # 다운로드 완료(10/500): 10.jpg
    break


