from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager



username = input("Gmail user: ")
password = input("Gmail passwd: ")

listOfChannelsToKeep = input("List the channels you want to keep separated by whitespaces: ").split()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')

email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys(username)

nextKey = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
nextKey.click()

passwd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
passwd.send_keys(password)

nextKey = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
nextKey.click()

time.sleep(4)
driver.get('https://www.youtube.com/?hl=es&gl=ES')

sideMenuDeploy = driver.find_element_by_xpath('//*[@id="guide-icon"]')
sideMenuDeploy.click()
time.sleep(1)
moreChannels = driver.find_element_by_xpath('//*[@id="items"]/ytd-guide-collapsible-entry-renderer')
moreChannels.click()
time.sleep(6)
sections = driver.find_elements_by_xpath('//*[@id="items"]')
elements = sections[1].find_elements_by_tag_name('ytd-guide-entry-renderer')
links = elements[0].find_elements_by_xpath('//*[@id="endpoint"]')

channels = []
channelNames = []
channelsToKeep = listOfChannelsToKeep
elementCount = 10

for element in elements:
    if links[elementCount].get_attribute('title') != 'Explorar canales':
        try:
            name = links[elementCount].get_attribute('title') 
            text = links[elementCount].get_attribute('href')        
        except TypeError:
            name = str(links[elementCount].get_attribute('title'))
            text = str(links[elementCount].get_attribute('href'))

        if str(text) != "None":
            channelNames.append(name)
            channels.append(text)
            print( name + ' ' + text )
        elementCount += 1

    else:
        break

elementCount = 0
isInTheList = False

sideMenuCollapse = driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[1]/yt-icon-button/button/yt-icon')
sideMenuCollapse.click()

for channelName in channelNames:
    for channelToKeep in channelsToKeep:
        if channelName.lower() == channelToKeep.lower():

            isInTheList = True
            break

    if isInTheList == False:

        driver.get(channels[elementCount])
        unsub = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button')
        unsub.click()
        cancelSubscription = driver.find_element_by_xpath('//*[@id="confirm-button"]/a')
        cancelSubscription.click()
        time.sleep(5)

    elementCount += 1
    isInTheList = False
