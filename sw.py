from selenium import webdriver
path=r"C:\\webdrivers\\chromedriver"
driver = webdriver.Chrome(path)
driver.get('http://web.whatsapp.com')

n=int(input("Enter number of times you want to run this prog : "))

for i in range(1,n):
    name = input('Enter the name of user or group : ')
    msg = input('Enter the message : ')
    count = int(input('Enter the count : '))

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_13mgZ')

    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_class_name('_3M-N-').click()
