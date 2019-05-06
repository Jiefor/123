# -*-coding：UTF-8-*-
#d导入时间类
import time
#导入appium中的webdriver
from appium import webdriver
#设备信息初始化

#定义一个空字典，存放设备信息
desired_caps={}
desired_caps['device']='sagit'
desired_caps['deviceName']='MI_6'
desired_caps['platformName']='Android'
desired_caps['platformVersion']='8.0'
desired_caps['appPackage']='com.meilin.wulianbaogj'
desired_caps['appActivity']='.activity.SplashActivity'
desired_caps['unicodeKeyboard']=True
desired_caps['resetKeyboard']=True

#远程调起app
dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)


#进入登录页面，进行登录操作
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username').send_keys('13500000001')
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password').send_keys('a1235678')
dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn').click()
time.sleep('3')
#在线报事
dr.find_element_by_id('com.meilin.wulianbaogj:id/rl_baoshi').click()
dr.find_element_by_id('com.meilin.wulianbaogj:id/content').send_keys('test')
#最小化键盘
dr.hide_keyboard()

