from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
# adb shell dumpsys window | find "mCurrentFocus"
desire_cap = {
    "platformName": "android",
    "platformVersion": "11",
    "deviceName": "Yayas",
    "automationName": "UIAutomator2",
    "appPackage": "ajaib.co.id",
    "appActivity": "ajaib.co.id.pages.main.AMain",
    "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)

time.sleep(3)
profile = driver.find_element(AppiumBy.ID, 'ajaib.co.id:id/vProfile')
profile.click()
time.sleep(3)
topup = driver.find_element(AppiumBy.ID, "ajaib.co.id:id/vTopUp")
topup.click()
time.sleep(3)
rdn = driver.find_element(AppiumBy.ID, "ajaib.co.id:id/tvTitleRDN")
rdn.click()