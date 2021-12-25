from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/15463567"

driver.get(url)

click = driver.find_element_by_xpath('//*[@id="test"]/button')

click.click()

cart = driver.find_element_by_xpath('//*[@id="cartIcon"]/div[1]/a')

cart.click()

checkout = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[2]/div/section/div/main/section/section[2]/div[3]/div/a/span')

checkout.click()