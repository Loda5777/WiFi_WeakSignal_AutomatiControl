import sys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# driver = webdriver.Chrome(r'D:\Python\chromedriver.exe')
# driver = webdriver.Chrome(r'D:\WifiThroughputTestProj\support\chromedriver.exe')
driver = webdriver.Chrome(r'E:\Google\Chrome\Application\chromedriver.exe')

'''
def Ip_Confirm():
    # 内部网络
    opt = driver.find_element_by_id("Advanced_LAN_Content_menu")
    opt.click()
    sleep(2)
    # DHCP服务器
    opt = driver.find_element_by_id("Advanced_DHCP_Content_tab")
    opt.click()
    # IP池起始及终止地址限定
    Ip_strat = driver.find_element_by_name("dhcp_start")
    Ip_end = driver.find_element_by_name("dhcp_end")
    Str1 = Ip_strat.get_attribute("value")
    Str2 = Ip_end.get_attribute("value")
    if Str1 == '192.168.50.250' and Str2 == '192.168.50.254':
        pass
    else:
        Ip_strat.clear()
        Ip_end.clear()
        Ip_strat.send_keys("192.168.50.250")
        Ip_end.send_keys("192.168.50.254")
        opt = driver.find_element_by_class_name("button_gen")
        opt.click()
        sleep(45)

'''


def login():
    driver.get('http://router.asus.com/error_page.htm?flag=1')
    driver.maximize_window()
    driver.find_element_by_class_name("button").click()
    sleep(1)
    # 输入账号
    driver.find_element_by_id("login_username").send_keys("admin")
    # 输入密码
    driver.find_element_by_name("login_passwd").send_keys("12345678")
    # 回车
    driver.find_element_by_class_name("button").click()
    sleep(5)
    # 确认URL是否正确
    currentURL = driver.current_url
    if currentURL == "http://router.asus.com/Advanced_Wireless_Content.asp":
        print("--------------------------------------------")
        print("successfully Connected to WifiUserInterface!")
        print("--------------------------------------------")
    else:
        print("failure")
    sleep(5)
    # 内部网络
    opt = driver.find_element_by_id("Advanced_LAN_Content_menu")
    opt.click()
    sleep(2)
    # DHCP服务器
    opt = driver.find_element_by_id("Advanced_DHCP_Content_tab")
    opt.click()
    # IP池起始及终止地址限定
    Ip_strat = driver.find_element_by_name("dhcp_start")
    Ip_end = driver.find_element_by_name("dhcp_end")
    Str1 = Ip_strat.get_attribute("value")
    Str2 = Ip_end.get_attribute("value")
    if Str1 == '192.168.50.250' and Str2 == '192.168.50.254':
        # 无线网络
        ele = driver.find_element_by_id("Advanced_Wireless_Content_menu")
        ele.click()
        sleep(1)
    else:
        Ip_strat.clear()
        Ip_end.clear()
        Ip_strat.send_keys("192.168.50.250")
        Ip_end.send_keys("192.168.50.254")
        opt = driver.find_element_by_class_name("button_gen")
        opt.click()
        sleep(50)
        # 输入账号
        driver.find_element_by_id("login_username").send_keys("admin")
        # 输入密码
        driver.find_element_by_name("login_passwd").send_keys("123456")
        # 回车
        driver.find_element_by_class_name("button").click()
        sleep(5)
        # 无线网络
        ele = driver.find_element_by_id("Advanced_Wireless_Content_menu")
        ele.click()
        sleep(1)


def quit():
    driver.quit()


def Wireless_Content_Click():
    wait = WebDriverWait(driver, 10)
    for _ in range(3):
        try:
            ele = wait.until(
                EC.element_to_be_clickable((By.ID, "Advanced_Wireless_Content_menu"))
            )
            ele.click()
            break
        except:
            sleep(1)
            print('try to find element click')
    print('点击无线设置')


def applySettings():
    '''
    wait = WebDriverWait(driver, 10)
    for _ in range(3):
        try:
            ele = wait.until(
                EC.element_to_be_clickable((By.ID, "applyButton"))
            )
            ele.click()
            break
        except:
            sleep(1)
            print('try to find element click')
    '''
    # 应用无线设置页面
    sleep(5)
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()

    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    print("<一般设置> 已应用")


def applySettings_Pro():
    # 应用本页面设置
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


'''
wl_unit1_wifi4_on 对应打开2.4G的wifi4(802.11n)协议
wl_unit1_wifi6_on 对应打开2.4G的wifi6（802.11ax）协议
wl_unit1_off      对应关闭2.4G所有协议
wl_unit2_1_on     对应打开5G的wifi5(802.11ac)协议
wl_unit2_2_on     对应打开5G的wifi6(802.11ax)协议
wl_unit2_off      对应关闭5G的所有协议
'''


def wl_unit1_wifi4_on():
    # 切到专业设置
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # 设置WiFi4(802.11n)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("0")
    # "0"=Up to MCS 7 (802.11n) "1"=Up to MCS 9 (TurboQAM/256-QAM) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    # 应用本页面设置
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11n)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 切到一般设置
    sleep(2)
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("1")  # "0"=自动 "1"=N only "2"=Legacy
    # 应用本页面设置
    sleep(2)
    # driver.find_element_by_id("applyButton").click()
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11n)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit1_wifi5_on():
    # 切到专业设置
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # 设置WiFi4(802.11ax)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("1")
    # "0"=Up to MCS 7 (802.11n) "1"=Up to MCS 9 (TurboQAM/256-QAM) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    # 应用本页面设置
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11ax)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 切到一般设置
    sleep(2)
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("0")  # "0"=自动 "1"=N only "2"=Legacy
    # 802.11ax HE frame support 模式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_11ax']")
    Select(opt).select_by_value("0")  # "1"=启用 "0"=停用
    # 应用本页面设置
    sleep(2)
    # driver.find_element_by_id("applyButton").click()
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11ax)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit1_wifi6_on():
    # 切到专业设置
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # 设置WiFi4(802.11ax)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("2")
    # "0"=Up to MCS 7 (802.11n) "1"=Up to MCS 9 (TurboQAM/256-QAM) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    # 应用本页面设置
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11ax)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 切到一般设置
    sleep(2)
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("0")  # "0"=自动 "1"=N only "2"=Legacy
    # 802.11ax HE frame support 模式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_11ax']")
    Select(opt).select_by_value("1")  # "1"=启用 "0"=停用
    # 应用本页面设置
    sleep(2)
    # driver.find_element_by_id("applyButton").click()
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz(802.11ax)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit1_off():
    wait = WebDriverWait(driver, 10)
    for _ in range(3):
        try:
            ele = wait.until(
                EC.element_to_be_clickable((By.ID, "Advanced_WAdvanced_Content_tab"))
            )
            ele.click()
            break
        except:
            sleep(1)
            print('try to find element click')
    print('点击专业设置')
    # driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("0")  # 2.4GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[2]')  # radio_button_off
    opt.click()
    sleep(1)
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("2.4GHz<专业设置> off")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit2_wifi4_on():
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # WiFi5(802.11ac)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("1")  # "1"=Up to MCS 9 (802.11ac) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ac)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    sleep(2)
    # 切到一般设置
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("8")  # "0"=自动 "9"=AX only "8"=N/AC/AX mixed "2"=Legacy
    # 802.11ax HE frame support
    opt = driver.find_element_by_css_selector(".input_option[name='wl_11ax']")
    Select(opt).select_by_value("0")  # "1"=启用 "0"=停用
    # 应用本页面设置
    sleep(2)
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ac)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)

    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ac)<一般设置> on")
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit2_wifi5_on():
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # WiFi6(802.11ax)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("1")  # "1"=Up to MCS 9 (802.11ac) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ax)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 切到一般设置
    sleep(2)
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("8")  # "0"=自动 "9"=AX only "8"=N/AC/AX mixed "2"=Legacy
    # 802.11ax / Wi-Fi 6 模式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_11ax']")
    Select(opt).select_by_value("0")  # "1"=启用 "0"=停用
    # 应用本页面设置
    sleep(2)
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ax)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit2_wifi6_on():
    driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[1]')  # radio_button_on
    opt.click()
    sleep(1)
    # WiFi6(802.11ax)调制方式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
    Select(opt).select_by_value("2")  # "1"=Up to MCS 9 (802.11ac) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ax)<专业设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 切到一般设置
    sleep(2)
    driver.find_element_by_id("Advanced_Wireless_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    # 无线模式设置
    opt = driver.find_element_by_css_selector(".input_option[name='wl_nmode_x']")
    Select(opt).select_by_value("8")  # "0"=自动 "9"=AX only "8"=N/AC/AX mixed "2"=Legacy
    # 802.11ax / Wi-Fi 6 模式
    opt = driver.find_element_by_css_selector(".input_option[name='wl_11ax']")
    Select(opt).select_by_value("1")  # "1"=启用 "0"=停用
    # 应用本页面设置
    sleep(2)
    opt = driver.find_element_by_id("applyButton")
    webdriver.ActionChains(driver).move_to_element(opt).click(opt).perform()
    sleep(1)
    # 判断弹出弹出框并确定
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz(802.11ax)<一般设置> on")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)
    # 若有第二个弹窗，则做确认动作
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            driver.switch_to.alert.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def wl_unit2_off():
    wait = WebDriverWait(driver, 10)
    for _ in range(3):
        try:
            ele = wait.until(
                EC.element_to_be_clickable((By.ID, "Advanced_WAdvanced_Content_tab"))
            )
            ele.click()
            break
        except:
            sleep(1)
            print('try to find element click')
    print('点击专业设置')
    # driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    Select(opt).select_by_value("1")  # 5GHz
    sleep(1)
    opt = driver.find_element_by_xpath('//*[@id="wl_rf_enable"]/td/input[2]')  # radio_button_off
    opt.click()
    sleep(1)
    driver.find_element_by_id("apply_btn").click()
    sleep(1)
    result = 0
    i = 0
    while not result:
        result = EC.alert_is_present()(driver)
        if result:
            print("5GHz<专业设置> off")
            result.accept()
        i += 1
        if i == 20:
            break
        sleep(0.5)


def Change_bandWidth(Fband, bandWidth):
    Wireless_Content_Click()
    opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
    webdriver.ActionChains(driver).move_to_element(opt)
    sleep(1)
    if Fband == "2.4G":
        # 频段设置
        Select(opt).select_by_value("0")  # 2.4GHz
        sleep(5)
        # 定位带宽下拉框
        opt = driver.find_element_by_css_selector(".input_option[name='wl_bw']")
        # 带宽设置
        if bandWidth == "20MHz":
            Select(opt).select_by_value("1")  # "1"=20MHz "2"=40MHz
        elif bandWidth == "40MHz":
            Select(opt).select_by_value("2")  # "1"=20MHz "2"=40MHz
        else:
            pass
        sleep(1)
    elif Fband == "5G" or "5.8G":
        Select(opt).select_by_value("1")  # 5GHz
        sleep(5)
        opt = driver.find_element_by_css_selector(".input_option[name='wl_bw']")
        if bandWidth == "20MHz":
            Select(opt).select_by_value("1")  # "1"=20MHz "2"=40MHz "3"=80MHz
        elif bandWidth == "40MHz":
            Select(opt).select_by_value("2")  # "1"=20MHz "2"=40MHz "3"=80MHz
        elif bandWidth == "80MHz":
            Select(opt).select_by_value("3")  # "1"=20MHz "2"=40MHz "3"=80MHz
        sleep(1)
    else:
        pass
    applySettings()


def SetAPforNewChannel(Fband, bandWidth, channelNum):
    Wireless_Content_Click()
    # 信道设置
    # 定位信道下拉框
    opt = driver.find_element_by_css_selector(".input_option[name='wl_channel']")
    if bandWidth == '40MHz':
        if Fband == '2.4G':
            channelNum = channelNum
        else:
            if channelNum == '36':
                channelNum = '36l'
            elif channelNum == '44':
                channelNum = '44l'
            elif channelNum == '149':
                channelNum = '149l'
            elif channelNum == '161':
                channelNum = '161u'
            else:
                pass
    elif bandWidth == '80MHz':
        if channelNum == '36':
            channelNum = '36/80'
        elif channelNum == '44':
            channelNum = '44/80'
        elif channelNum == '149':
            channelNum = '149/80'
        elif channelNum == '161':
            channelNum = '161/80'
        else:
            pass
    else:
        channelNum = channelNum
    print(channelNum)
    webdriver.ActionChains(driver).move_to_element(opt)
    sleep(1)
    Select(opt).select_by_value(channelNum)
    # 2021.3.10改
    applySettings()
    return 'YES'


def SetAPwifiName(wifiName):
    #   只起一个切换作用，当前必须是wifi5或wifi6状态
    if wifiName == 'wifi5':
        driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
        opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
        Select(opt).select_by_value("1")  # 5GHz
        sleep(1)
        # WiFi5(802.11ac)调制方式
        opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
        Select(opt).select_by_value("1")  # "1"=Up to MCS 9 (802.11ac) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
        driver.find_element_by_id("apply_btn").click()
        sleep(1)
        result = 0
        i = 0
        while not result:
            result = EC.alert_is_present()(driver)
            if result:
                print("5GHz(802.11ac)<专业设置> on")
                result.accept()
            i += 1
            if i == 20:
                break
            sleep(0.5)
    else:
        driver.find_element_by_id("Advanced_WAdvanced_Content_tab").click()  # 专业设置
        opt = driver.find_element_by_css_selector(".input_option[name='wl_unit']")
        Select(opt).select_by_value("1")  # 5GHz
        sleep(1)
        # WiFi5(802.11ac)调制方式
        opt = driver.find_element_by_css_selector(".input_option[name='wl_turbo_qam']")
        Select(opt).select_by_value("2")  # "1"=Up to MCS 9 (802.11ac) "2"=Up to MCS 11 (NitroQAM/1024-QAM)
        driver.find_element_by_id("apply_btn").click()
        sleep(1)
        result = 0
        i = 0
        while not result:
            result = EC.alert_is_present()(driver)
            if result:
                print("5GHz(802.11ac)<专业设置> on")
                result.accept()
            i += 1
            if i == 20:
                break
            sleep(0.5)
    return "YES"


def SetAPallParameter(resetFbandOrNot, Fband, areaName, wifiName, bandWidth, channelNum):
    if resetFbandOrNot == 'Y':
        if Fband == "2.4G" and wifiName == "wifi4":
            wl_unit1_wifi4_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "2.4G" and wifiName == "wifi5":
            wl_unit1_wifi5_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "2.4G" and wifiName == "wifi6":
            wl_unit1_wifi6_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "5G" and wifiName == "wifi4":
            wl_unit2_wifi4_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "5G" and wifiName == "wifi5":
            wl_unit2_wifi5_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)

        elif Fband == "5G" and wifiName == "wifi6":
            wl_unit2_wifi6_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
    else:
        if Fband == "2.4G" and wifiName == "wifi4":
            wl_unit1_wifi4_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "2.4G" and wifiName == "wifi5":
            wl_unit1_wifi5_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "2.4G" and wifiName == "wifi6":
            wl_unit1_wifi6_on()
            sleep(10)
            wl_unit2_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "5G" and wifiName == "wifi4":
            wl_unit2_wifi4_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
        elif Fband == "5G" and wifiName == "wifi5":
            wl_unit2_wifi5_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)

        elif Fband == "5G" and wifiName == "wifi6":
            wl_unit2_wifi6_on()
            sleep(10)
            wl_unit1_off()
            sleep(10)
            Change_bandWidth(Fband, bandWidth)
            sleep(10)
            SetAPforNewChannel(bandWidth, channelNum)
            sleep(10)
    return "YES"


if __name__ == "__main__":
    args = sys.argv
    # args = ['', 'SetAPallParameter', 'Y', '5G', 'China', 'wifi5', '40MHz', '36']
    argslen = len(args)
    if args[1] == 'SetAPallParameter':
        argslen = len(args)
        if argslen > 2 and argslen < 9:
            for i in range(2, argslen):
                if i == 2:
                    resetFbandOrNot = args[i]
                elif i == 3:
                    Fband = args[i]
                elif i == 4:
                    areaName = args[i]
                elif i == 5:
                    wifiName = args[i]
                elif i == 6:
                    bandWidth = args[i]
                elif i == 7:
                    channelNum = args[i]
                else:
                    pass
        else:
            print("The number of the element is wrong!")
        login()
        SetAPallParameter(resetFbandOrNot, Fband, areaName, wifiName, bandWidth, channelNum)