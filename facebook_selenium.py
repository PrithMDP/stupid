from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys("emailhere")
elem = driver.find_element_by_id("pass")
elem.send_keys('passwordherefollowedby\n')

driver.get("https://developers.facebook.com/tools/explorer")

time.sleep(2)

print driver.find_element_by_xpath("//*[@id=\"u_0_0\"]/div/div[2]/div/div[2]/a").click()

driver.find_element_by_xpath("//*[@id=\"js_7\"]/div/ul/li[1]/a/span/span/span").click()



driver.find_element_by_xpath("//*[@id=\"facebook\"]/body/div[7]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/div/button").click()

time.sleep(5)
#elem =  driver.find_element_by_xpath("//*[@id=\"u_0_0\"]/div/div[2]/div/div[1]/label/input").text()

driver.find_element_by_xpath("//*[@id=\"u_0_0\"]/div/div[2]/div/div[1]/i").click()


driver.find_element_by_xpath("//*[@id=\"js_3\"]/div/div/div/div/div[2]/button").click()
time.sleep(5)

time.sleep(1)
c_hand = "NONe"
for handle in driver.window_handles:
    print "Handle = ",handle
    c_hand = handle

driver.switch_to_window(c_hand)
a_token = driver.current_url

loc = a_token.find("/?q=")
a_token = a_token[loc+4:]

print "ACCESS TOKEN IS", a_token

time.sleep(5)
driver.close()
