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
time.sleep(1)
#弹窗
#dr.switch_to.alert.accept()#该方法未实现，咱不可用
dr.find_element_by_id('android:id/button1').click()
time.sleep(2)
#进入登录页面，进行登录操作
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username').send_keys('13500000001')
time.sleep(2)
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password').send_keys('a12345678')
time.sleep(2)
dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn').click()
time.sleep(4)
#上滑
dr.swipe(20,1700,20,200,2000)
#在线报事
dr.find_element_by_id('com.meilin.wulianbaogj:id/rl_baoshi').click()
time.sleep(2)
dr.find_element_by_id('com.meilin.wulianbaogj:id/content').send_keys('test')
time.sleep(2)
#最小化键盘
dr.hide_keyboard()
time.sleep(2)
#滑动UP
dr.swipe(20,1700,20,200,2000)#第一次滑动
time.sleep(1)
dr.swipe(20,1700,20,1000,2000)#第二次滑动
time.sleep(2)
#添加照片
TouchAction(dr).press(x=200,y=450).release().perform()
time.sleep(2)
dr.find_element_by_id('android:id/button1').click()
time.sleep(2)
#dr.switch_to_alert().accept()#弹框允许，暂不可以用方法未实现
dr.find_element_by_id('com.android.camera:id/v9_shutter_button_internal').click()
time.sleep(5)
dr.find_element_by_id('com.android.camera:id/inten_done_apply').click()
time.sleep(10)
#添加视频
#滑动UP
dr.swipe(20,1700,20,200,2000)#第一次滑动
time.sleep(1)
dr.swipe(20,1700,20,1000,2000)#第二次滑动
time.sleep(2)
TouchAction(dr).press(x=220,y=840).release().perform()
time.sleep(2)
# dr.find_element_by_id('android:id/button1').click()
# time.sleep(2)
#开始
TouchAction(dr).press(x=550,y=1700).release().perform()
time.sleep(5)
#结束录制
TouchAction(dr).press(x=550,y=1700).release().perform()
time.sleep(3)
#上传
dr.find_element_by_id('com.android.camera:id/inten_done_apply').click()
time.sleep(30)
#添加录音
#滑动UP
dr.swipe(20,1700,20,200,2000)#第一次滑动
time.sleep(1)
dr.swipe(20,1700,20,1000,2000)#第二次滑动
time.sleep(2)

time.sleep(3)
el=dr.find_element_by_xpath('//*[@text="按住说话"]')
TouchAction(dr).long_press(el,4000).perform()

dr.find_element_by_id('android:id/button1').click()
time.sleep(2)
#添加备注
dr.find_element_by_id('com.meilin.wulianbaogj:id/remarkET').send_keys('testdata01')
time.sleep(2)
#提交
dr.find_element_by_xpath('//*[@text="提交"]').click()
time.sleep(5)
print("over~")
