from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import urllib.request


def main():
    global findLink1, findLink2, findLink3
    baseurl = "http://www.5ikfc.com/mdl/menu/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
               'content-type': 'application/x-www-form-urlencoded'}
    data = bytes(urllib.parse.urlencode({"name": "tim"}), encoding="utf-8")
    req = urllib.request.Request(url=baseurl, data=data, headers=headers, method="GET")
    response = urllib.request.urlopen(req)
    # 正则表达式提取网页信息
    findLink2 = re.compile(r'<b>(.*?)</b>')  # 价格
    findLink1 = re.compile(r'<a href=".*?">(.*?)</a>', re.S)  # 图
    findLink3 = re.compile(r'<a href=".*?">(.*?)</a>')  # 名字


main()


# 访问URL
def ask_url(url):
    global response, request
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def get_data(baseurl):
    global data, item
    datalist = []
    url = baseurl
    html = ask_url(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    for item1 in soup.find_all('ul', class_="fx"):

        data = []
        item = str(item1)
        for n in range(0, 231):
            global link1
            link1 = re.findall(findLink1, item)[n * 2]
            link2 = re.findall(findLink2, item)[n]
            link3 = re.findall(findLink3, item)[n * 2 + 1]
            data.append(link3)
            data.append(link2)
    return datalist


get_data("http://www.5ikfc.com/mdl/menu/")


def savedata(datalist, savepath):  # 将商品的名称和价格导入到excel表格中
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('套餐', cell_overwrite_ok=True)
    for i in range(0, 2):
        col = ("名字", "价格")
        sheet.write(0, i, col[i])
    k = 0
    for j in range(0, 231):
        for i in range(0, 2):
            k = k + 1
            sheet.write(j + 1, i, data[k - 1])
    book.save(savepath)


def save():
    savepath = "menuinfo.xls"
    savedata(data, savepath)


save()
