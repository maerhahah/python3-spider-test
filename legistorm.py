from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys


# 判断登录与否
def login(browser, username, passwd):
    # 判断是否是已经登录
    isLogin = browser.page_source.find('logout.html')
    if isLogin != -1:
        return True

    # javascript 脚本
    javaScript = """
        var username = $('input[name="username"]').val('{0}');
        var password = $('input[name="password"]').val('{1}');
        $('.login-box .btn').click();
        """.format(username, passwd)

    try:
        # 执行登录脚本
        browser.execute_script(javaScript)
    except:
        return False
    return True


# 获取页面数据
def getHtml(url, username, passwd):
    try:
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(url)

        # 如果没有登录或者登录过期就登录后返在次返回当页面
        if login(browser, username, passwd) == False:
            browser.get(url)

        page_source = browser.page_source
        browser.close()

        return page_source
    except:
        return False


if __name__ == '__main__':

    # print(sys.argv)
    # print(len(sys.argv))
    # print(sys.argv[1])
    # exit(1)

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    url = 'https://www.legistorm.com/'
    topMenuUrlFile = 'topMenuUrl.txt'

    html = getHtml(url, USERNAME, PASSWORD)
    print(html)

    # 解析链接
    soup = BeautifulSoup(html, "html.parser")
    topMenuA = soup.find('div', attrs={'class': 'top-menu'}).find_all('a', {'href': True})

    # 解析全部存入文件
    for a in topMenuA:
        url = a['href']
        if url.find('legistorm') != -1:
            with open(topMenuUrlFile, 'a') as file:
                file.write(url + '\n')

    # 逐条获取每个头部链接的html内容
    # 1、 生成url列表
    apis = ''
    with open(topMenuUrlFile, 'r') as f:
        apis = f.readlines()

    # 2、遍历获取内容
    if apis:
        for api in apis:
            print('***********************************************')
            print(api + '\n')
            text = getHtml(api, USERNAME, PASSWORD)
            print(text)
