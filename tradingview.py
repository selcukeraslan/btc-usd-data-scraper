from selenium import webdriver
from time import sleep

file = open('btcusdFiyat.csv', 'w')

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("-headless")
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.delete_all_cookies()

driver.get("https://tr.tradingview.com/chart/?symbol=BITSTAMP%3ABTCUSD")
driver.implicitly_wait(5)
while True:
    fiyatBilgisi = driver.find_element(
        "xpath", "/html/body/div[3]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[5]/span[1]/span[1]").text
    print(fiyatBilgisi)
    file.write(fiyatBilgisi)
    file.write("\n")
    file.flush()
    sleep(3)
file.close()
