#d导入时间类
import time
from appium.webdriver.common.touch_action import TouchAction
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
desired_caps['automationName']='Uiautomator2'#有什么作用？
#远程调起app
dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(12)
# #弹窗
# dr.find_element_by_id('android:id/button1').click()
# time.sleep(2)
#进入登录页面，进行登录操作
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username').send_keys('13500000001')
time.sleep(1)
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password').send_keys('a12345678')
time.sleep(1)
dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn').click()
time.sleep(3)
#报事
dr.find_element_by_id('com.meilin.wulianbaogj:id/home_fragment_rel_baos').click()
time.sleep(2)
#长按录音
TouchAction(dr).press(x=500,y=1500).release().perform()
time.sleep(1)
# #弹窗
# dr.find_element_by_id('android:id/button1').click()
# time.sleep(4)
TouchAction(dr).press(x=500,y=1500).release().perform()

