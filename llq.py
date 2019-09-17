from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://shodan.io'
url = 'https://www.legistorm.com'
print(url)

# 禁止图片的加载

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

print(1)
# 启动浏览器，并设置好wait
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.set_window_size(configure.windowHeight, configure.windowWidth)   # 根据桌面分辨率来定，主要是为了抓到验证码的截屏
# wait = WebDriverWait(browser, timeout = configure.timeoutMain)


print(2)
browser.get(url)

print(browser.page_source)

# txt = driver.page_source
# with open('html.txt','r') as f:
#     print('ss')
#     f.write(txt)
