import time

from selenium import webdriver

# opens tab on Google Chrome
driver = webdriver.Chrome()

# open the store you want
url = "https://www.footlocker.ca/en/product/new-balance-m5740-v1-mens/56651695.html"
driver.get(url)

# while the size button isnt available
buttonAvailable = False
while not buttonAvailable:

    #path to the size button
    sizeButton = driver.find_element_by_xpath('//*[@id="ProductDetails"]/div[4]/div[4]/fieldset/div/div[8]')

    #if the button size button isnt clickable
    if ("c-form-field--disabled" in sizeButton.get_attribute("class")):

        #wait one second to refresh the page
        time.sleep(1)
        driver.refresh()

    # if it is available exit the loop
    else:
        buttonAvailable = True

#click the wanted size
sizeButton.click()

#click the add to cart button
cartButton = driver.find_element_by_xpath('//*[@id="ProductDetails"]/ul/li[3]/button')
cartButton.click()