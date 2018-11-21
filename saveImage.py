# 先导入库
import os
import urllib
import zlib

def save_img(self, img_mun, title, img_url):
    # 将图片保存到本地
    self.log('saving pic: ' + img_url)

    # 保存漫画的文件夹
    document = '/Users/ningmiao/Desktop/cartoon'

    # 每部漫画的文件名以标题命名
    comics_path = document + '/' + title
    exists = os.path.exists(comics_path)
    if not exists:
        self.log('create document: ' + title)
        os.makedirs(comics_path)

    # 每张图片以页数命名
    pic_name = comics_path + '/' + img_mun + '.jpg'

    # 检查图片是否已经下载到本地，若存在则不再重新下载
    exists = os.path.exists(pic_name)
    if exists:
        self.log('pic exists: ' + pic_name)
        return

    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }

        req = urllib.request.Request(img_url, headers=headers)
        response = urllib.request.urlopen(req, timeout=30)

        # 请求返回到的数据
        data = response.read()

        # 若返回数据为压缩数据需要先进行解压
        if response.info().get('Content-Encoding') == 'gzip':
            data = zlib.decompress(data, 16 + zlib.MAX_WBITS)

        # 图片保存到本地
        fp = open(pic_name, "wb")
        fp.write(data)
        fp.close

        self.log('save image finished:' + pic_name)

    except Exception as e:
        self.log('save image error.')
        self.log(e)
