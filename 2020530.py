from selenium import webdriver
import time
driver=webdriver.Firefox()#对应浏览器
driver.get("https://www.baidu.com/")#打开百度搜索框
#通过id定位
#driver.find_element_by_id("kw").send_keys("布拉格")#通过id定位百度输入框，搜索布拉格
#通过name定位
#driver.find_element_by_name("wd").send_keys("苹果")
#通过class name定位
#driver.find_element_by_class_name("s_ipt").send_keys("布拉格")
#通过tag name定位，必须是唯一的，这里并不唯一
#driver.find_element_by_tag_name("input").send_keys("布拉格")
#通过xpath定位
#driver.find_element_by_xpath("//*[@id='kw']").send_keys("布拉格")
#通过css selector定位
#driver.find_element_by_css_selector("#kw").send_keys("布拉格")
#driver.find_element_by_css_selector(".s_ipt").send_keys("布拉格")
#通过link text定位
#driver.find_element_by_link_text("hao123").click()
#通过partial link text定位
#driver.find_element_by_partial_link_text("hao").click()
#driver.find_element_by_id("su").click()#通过id定位到百度搜索框，点击
#实现clear操作测试对象
#driver.find_element_by_id("kw").send_keys("布拉格")
#driver.find_element_by_id("su").click()
#time.sleep(5)
#driver.find_element_by_id("kw").clear()
#data=driver.find_element_by_id("s-bottom-layer-right").text
#print(data)
#driver.find_element_by_id("kw").send_keys("布拉格")
#driver.find_element_by_id("su").click()
#time.sleep(8)#固定等待8秒
#driver.implicitly_wait(8)
#driver.find_element_by_link_text("布拉格_百度百科").click()
#t=driver.title
#print(t)#打印title
#t=driver.current_url
#print(t)#打印url
#driver.maximize_window()
#driver.set_window_size(480,800)#将宽设为480，高设为800
#driver.find_element_by_id("kw").send_keys("布拉格")
#driver.find_element_by_id("su").click()
#time.sleep(8)
#driver.back()#后退
#time.sleep(3)
#driver.forward()#前进
js="var q=document.documentElement.scrollTop=10000"#将页面滚动条滚到底部
driver.execute_script(js)
time.sleep(6)
js="var q=document.documentElement.scrollTop=0"#将页面滚动条滚到顶部
driver.execute_script(js)
time.sleep(6)
driver.quit()

