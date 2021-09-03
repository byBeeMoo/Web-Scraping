from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://translate.google.es/') # Change .es for your region, now translates ENG > ESP
sleep(6)

with open("./translated.txt", "w", encoding="utf-8") as f:
    while True:
        sleep(1)
        textContent = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')
        # //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span/text()
        print(textContent.text)
        f.writelines(textContent.text)
        
        button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[5]/div/div[2]/button[2]')
        #   //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[5]/div/div[2]/button[2]
        button.click()
        