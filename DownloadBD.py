import json

import requests
import NetUtils
import DownloadUtil
import time

baseUril = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7670236709753554050&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1617847502591="


def getBaseUril(word):
    return baseUril.format(word, word)


jason = requests.get(getBaseUril(input("请输入要下载的图片种类 ： \n")), headers=NetUtils.header).text

data = json.loads(jason)

datas = data["data"]

print("datas " + str(datas))
versionList = []
for x in datas:
    if len(x) > 0:
        versionList.append(x["thumbURL"])

# print versionList

startStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
start = time.time()

for i in versionList:
    time.sleep(0.5)
    DownloadUtil.download_from_url(i, "D:/PythonTest/" + str(time.time()) + ".jpg")

endStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
chazhi = time.time() - start

print("下载结束 总下载数量{},开始时间{},结束时间{} , 总用时：{}".format(str(len(versionList)), startStr, endStr, str(chazhi)))
