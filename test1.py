import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 创建Chrome WebDriver实例
driver = webdriver.Chrome()

# 打开百度网站
driver.get("https://www.baidu.com/")

# 在搜索框中输入关键词
search_box = driver.find_element(By.NAME, "wd")  # 定位百度搜索框元素
search_box.send_keys("MySql")  # 替换成你想搜索的关键词
search_box.send_keys(Keys.RETURN)  # 模拟按下回车键

# 等待搜索结果加载
time.sleep(10)

# 获取第一条搜索结果的标题和链接
first_result = driver.find_element(By.CSS_SELECTOR, "#content_left .t a")
title = first_result.text
link = first_result.get_attribute("href")

# 打印结果
print("第一条搜索结果标题:", title)
print("第一条搜索结果链接:", link)

# 关闭浏览器
driver.quit()
