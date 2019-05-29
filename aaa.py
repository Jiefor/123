# -*-coding：UTF-8-*-

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
desired_caps['automationName']='Uiautomator2'
#远程调起app
dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#弹框自动允许
dr.switch_to.alert.accept()
#dr.switch_to_alert().accept()
time.sleep(2)
#登录
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username').send_keys('13500000001')
time.sleep(2)
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password').send_keys('a12345678')
time.sleep(2)
dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn').click()
time.sleep(4)
#上滑
dr.swipe(20,1700,20,200,2000)
#在线报事
dr.find_element_by_id('com.meilin.wulianbaogj:id/iv_baoshi').click()
time.sleep(2)
#报事内容
dr.find_element_by_id('com.meilin.wulianbaogj:id/content').send_keys('test')
time.sleep(2)
#取消键盘
dr.hide_keyboard()
#上滑
dr.swipe(20,1700,20,200,2000)
#上滑
dr.swipe(20,1700,20,200,2000)
time.sleep(1)
#拍照
dr.find_element_by_xpath('')
#adb='adb shell input tap 204 935'
# os.system(adb)
#录像

#退出app
#dr.close_app()
