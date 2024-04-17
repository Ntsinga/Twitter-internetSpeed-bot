from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "testingemail641@gmail.com"
TWITTER_PASSWORD = "getRich6416."


class InternetSpeedTwitterBot:
    def __init__(self):
        chromedriver_path = r"C:\Users\USER\Dev\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path=chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.up = ''
        self.down = ''

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))
        go_button.click()
        timer = time.time() + 60

        while time.time() < timer:
            self.down = self.driver.find_element(By.XPATH,
                                                 "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
            self.up = self.driver.find_element(By.XPATH,
                                               "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
            print(self.up)
            print(self.down)

    def tweet_at_provider(self):
        message = f'Hey @mtnug, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up'
        self.driver.get("https://twitter.com/i/flow/login")
        username = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        username.send_keys('InternetSp33d')
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        # password_button=WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[1]/div')))
        # password_button.click()

        password = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.NAME,
                                                                                                     'password')))
        password.click()
        password.send_keys(TWITTER_PASSWORD)
        logIn = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')))

        logIn.click()
        tweet = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        tweet.click()
        tweet.send_keys(message)

        post = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                 '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div > div > span > span')))
        post.click()


internetSpeed_bot = InternetSpeedTwitterBot()
internetSpeed_bot.get_internet_speed()
internetSpeed_bot.tweet_at_provider()
