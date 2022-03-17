from selenium import webdriver
import time

# 谷歌浏览器内核
driver_path = '/Users/albertmilagro/PycharmProjects/selenium_daily_report-master/chromedriver'  # 获取程序所在文件夹路径
driver = webdriver.Chrome(driver_path)

params = {"latitude": 45.73518, "longitude": 126.63223, "accuracy": 100}  # 地理位置模拟（经纬度）
driver.execute_cdp_cmd("Page.setGeolocationOverride", params)  # 强行覆写定位

student_number = '1183300508' # 输入学号
password = '111111'  # 输入密码

driver.get("https://ids.hit.edu.cn/authserver/login?service=https%3A%2F%2Fxg.hit.edu.cn%2Fzhxy-xgzs%2Fcommon%2FcasLogin%3Fparams%3DL3hnX21vYmlsZS94c0hvbWU%3D")
time.sleep(1.5)

driver.find_element_by_id('username').send_keys(student_number)  # 输入学号
time.sleep(0.1)
driver.find_element_by_id('password').send_keys(password)  # 输入密码
time.sleep(0.1)
driver.find_element_by_id('login_submit').click()  # 登录
time.sleep(0.2)

driver.find_element_by_id('mrsb').click()  # 每日上报界面
time.sleep(0.2)

driver.find_element_by_id('dtjwd').click()  # 刷新地点
time.sleep(0.1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[63]/label').click() # 1.本人已了解填写此登记表的目的及其严肃性，承诺填报信息全部真实可靠。
time.sleep(0.1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[64]/label').click()  # 2.如遇疫情突发或政策性调整致使不满足入校要求，我将主动报告，并暂缓入校。
time.sleep(0.1)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div[65]/label').click()  # 3.今日已如实查验并上报“龙江健康码”的码色。
time.sleep(0.1)
driver.find_element_by_id('tj_btn').click() # 上报
time.sleep(0.5)
driver.quit()