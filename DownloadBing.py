import requests
import time
import NetUtils

from lxml import etree

import DownloadUtil

# 必应图片网页地址
url = 'https://bing.ioliu.cn/?p='


imageSize=0


def downloadImg(index):

    html = requests.get(url + str(index), headers=NetUtils.header).text  # 下载网页
    etree_html = etree.HTML(html)  # 构造xpath的解析对象
    img_url = etree_html.xpath('//img/@src')  # 获取图片地址
    # print(img_url)

    for img_list in img_url:  # 下载图片并保存至指定位置
        global imageSize
        imageSize=imageSize+1
        DownloadUtil.download_from_url(img_list, "D:/PythonTest/" + str(time.time()) + ".jpg")



startStr=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
start=time.time()
for i in range(1, 10):
    time.sleep(0.5)
    downloadImg(i)

endStr=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
chazhi=time.time()-start

print("下载结束 总下载数量{},开始时间{},结束时间{} , 总用时：{}".format(str(imageSize),startStr,endStr,str(chazhi)))


