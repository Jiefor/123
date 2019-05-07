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

#远程调起app
dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
time.sleep(1)
#弹窗
dr.find_element_by_id('android:id/button1').click()
time.sleep(2)
#进入登录页面，进行登录操作
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username').send_keys('13500000001')
time.sleep(1)
dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password').send_keys('a12345678')
time.sleep(1)
dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn').click()
time.sleep(3)
#上滑
dr.swipe(20,1700,20,200,2000)
#在线报事
dr.find_element_by_id('com.meilin.wulianbaogj:id/rl_baoshi').click()
dr.find_element_by_id('com.meilin.wulianbaogj:id/content').send_keys('test')
#最小化键盘
dr.hide_keyboard()
#滑动UP
dr.swipe(20,1700,20,200,2000)#第一次滑动
dr.swipe(20,1700,20,1000,2000)#第二次滑动
# #添加照片
# dr.find_element_by_xpath('')
# dr.find_element_by_name('拍摄').click()
# dr.find_element_by_id('com.android.camera:id/inten_done_apply').click()
# time.sleep(10)
# #添加视频
# dr.find_elements_by_id('com.meilin.wulianbaogj:id/recyclerViewPics')[4].click()
# dr.find_element_by_id('com.android.camera:id/v9_shutter_button_internal').click()
# time.sleep(4)
# dr.find_element_by_id('com.android.camera:id/v9_shutter_button_internal').click()
# dr.find_element_by_id('com.android.camera:id/inten_done_apply').click()
# time.sleep(30)
# #添加录音
# el=dr.find_element_by_id('com.meilin.wulianbaogj:id/talkBtn')
# TouchAction.long_press(el,100,1100,4000).perform().release()
#添加备注
dr.find_element_by_id('com.meilin.wulianbaogj:id/remarkET').send_keys('testdata')
#提交
dr.find_element_by_xpath("//*[@class='android.widget.Button']").click()
time.sleep(5)