from selenium import webdriver
import time
import re


def search_product():
    input_div = driver.find_element_by_id('q')
    input_div.send_keys("手机")
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(60)
    pages = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    print(pages)
    pages = int(re.compile('\d+').search(pages).group())
    print(pages)
    return pages


def drop_down():
    for i in range(1, 11, 2):
        time.sleep(0.5)
        j = i/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


def get_products():
    # //div[@class=items],//代表任意位置，@代表属性
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        image = div.find_element_by_xpath('//div[@class="pic"]/a/img').get_attribute('src')
        price = div.find_element_by_xpath('//a[@class="pic-link J_ClickStat J_ItemPicA"]').get_attribute('trace-price')
        print(image, price, sep='|')


def next_page(commodity):
    pages = search_product()
    num = 1
    while num != pages:
        url = 'https://s.taobao.com/search?q={}&s={}'.format(commodity, num*44)
        driver.implicitly_wait(10)
        driver.get(url)
        drop_down()
        get_products()
        num += 1


if __name__ == '__main__':
    commodity = input('请输入要搜索的商品：')
    driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\黑马\CODE\爬虫\chromedriver.exe')
    driver.get('https://www.taobao.com/')
    next_page(commodity)
