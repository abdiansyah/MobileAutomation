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
topup = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/androidx.cardview.widget.CardView/android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.TextView")
topup.click()
time.sleep(3)
rdn = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]")
rdn.click()