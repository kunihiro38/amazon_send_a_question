import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestSend():
    def setup_method(self):
        # web立ち上げ
        options = Options()
        options.add_argument("--user-data-dir=userdata")
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.vars = {}

    def teardown_method(self):
        # webページを閉じる
        self.driver.quit()

    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_send(self, url, email, password, inquiry_text):
        # メイン
        self.driver.get("https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_signin&switch_account=")
        try:
            search_box = self.driver.find_element_by_id("ap_email")
            search_box.send_keys(email)
            search_box.submit()
            time.sleep(2)
        except:
            pass
        try:
            search_box = self.driver.find_element_by_id("ap_password")
            search_box.send_keys(password)
            search_box.submit()
            time.sleep(2)
        except:
            pass
        self.driver.get(url)
        question_url=self.driver.find_element_by_xpath('//*[@id="seller-contact-button"]/span/a').get_attribute("href")
        self.driver.get(question_url)
        self.driver.find_element(By.ID, "a-autoid-0-announce").click()
        self.driver.find_element(By.ID, "preOrderSubject_0").click()
        self.driver.find_element(By.NAME, "writeButton").click()
        self.driver.find_element(By.ID, "comment").click()
        self.driver.find_element(By.ID, "comment").send_keys("test")
        time.sleep(2)
        print("finish")
        # self.driver.find_element(By.NAME, "sendEmail").click()

if __name__ == "__main__":
    url="https://www.amazon.co.jp/sp?_encoding=UTF8&asin=B07W3SJMFN&isAmazonFulfilled=1&isCBA=&marketplaceID=A1VC38T7YXB528&orderID=&seller=A2KE6GVG21JQW0&tab=&vasStoreID="
    email="input_your_email"
    password="input_your_password"
    inquiry_text = "○○様 \n\nお世話になっております。\n〇〇と申します。"
    driver=TestSend()
    driver.setup_method()
    driver.test_send(url, email, password, inquiry_text)
    driver.teardown_method()
