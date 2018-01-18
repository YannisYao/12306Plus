import hashlib
import os
from business.urlcontants import UrlContants
from business.middleproxy import MiddleProxy
from bs4 import BeautifulSoup
#首先获取图片，然后给图片进行md5摘要取名
IMAGE_DIRECTORY = 'captcha_images'


def md5str(str):
    m = hashlib.md5(str.encode(encoding= 'utf-8'))
    return m.hexdigest()

def md5(byte):
    return hashlib.md5(byte).hexdigest()

def download_captcha(url=UrlContants.CAPTCHA_URL):
    s = MiddleProxy.getSession().get(url,headers=MiddleProxy.headers_image)
    if s.status_code == 200 and s.headers['Content-Type'] == 'image/jpeg':
        content = s.content
        # image_name = md5(content)
        # print(image_name)
        #return save_image(content, image_name+'.jpg')
        return (True,content)
    elif s.status_code == 200 and s.headers['Content-Type'] == 'text/html':
        bsObj = BeautifulSoup(s.content,'html.parser')
        err_msg = bsObj.find('div', {'class': 'err_text'}).find('li', {'id': 'err_bot'}).get_text().strip()
        err_msg = err_msg[:err_msg.index('！')+2]
        return (False,err_msg)

def save_image(byte,name):
    if not os.path.exists(IMAGE_DIRECTORY):
        os.mkdir(IMAGE_DIRECTORY)
    if not os.path.exists(os.path.join(IMAGE_DIRECTORY,name)):
        with open(os.path.join(IMAGE_DIRECTORY, name), 'wb') as f:
            f.write(byte)
    return os.path.join(IMAGE_DIRECTORY,name)