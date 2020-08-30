from selenium import webdriver
import time
import getpass

class Instabot:
    
    def __init__(self, username, password):
        
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com/")
        self.driver.maximize_window()
        time.sleep(2)
        
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(4)
        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        

    def getunfollowers(self):
        
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        time.sleep(2)

        self.driver.find_element_by_partial_link_text('following')\
            .click()
        time.sleep(1)
        following = self.getnames()

        self.driver.find_element_by_partial_link_text('followers')\
            .click()
        time.sleep(1)
        followers = self.getnames()



        unfollowers = [user for user in following if user not in followers]
        print("The unfollowers are: ", unfollowers)
        print("The number of unfollowers: ", len(unfollowers))

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button")\
            .click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log Out')]")\
            .click()

        self.driver.close()
        
        
    def getnames(self):    
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        height, ht = 0, 1
        while height != ht:
            height = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

print("Enter username and password. Password will be hidden.")
name = input("Username: ")
password = getpass.getpass()
mybot = Instabot(name, password)
mybot.getunfollowers()