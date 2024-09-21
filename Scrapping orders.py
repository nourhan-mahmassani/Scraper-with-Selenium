# Import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# List of order numbers
order_nb = ["263509113", "263508546", "263504816", "263504491", "263503885", "263503775", 
            "263503360", "263499408", "263499186", "263499109", "263498469", "263493708", 
            "263493477", "263492758", "263489562", "263489437", "263486209", "263484685", 
            "263479959", "263443566", "263430366", "263424185", "263423854", "263420657", 
            "263420407"]

# Specify the path to your chromedriver executable
service = Service(executable_path=r"C:\Users\User\Desktop\chromedriver-win32\chromedriver.exe")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the login page of the specified website
driver.get('https://admin.chownow.com/admin/login')

# Wait for 5 seconds to allow the page to load
time.sleep(5)

# Store the current window handle (for switching back if needed)
main_page = driver.current_window_handle

# Create empty lists to store order data
order_id = []
order_date = []
bill_total = []
name = []

# Define login credentials
email = 'username'
password = 'password'

# Input the email into the login field using XPath
driver.find_element("xpath", '/html/body/div[3]/div/div/div/form/div[3]/input').send_keys(email)

# Input the password into the login field using XPath
driver.find_element("xpath", '/html/body/div[3]/div/div/div/form/div[4]/input').send_keys(password)

# Click the login button using XPath
driver.find_element("xpath", '/html/body/div[3]/div/div/div/form/div[6]/input').click()

# Wait for 15 seconds to ensure the page has loaded after login
time.sleep(15)

# Loop through the orders on the page (assumes there are 19 orders in the table)
for i in range(1, 20):
    # Get order number using XPath
    order_nb = driver.find_element("xpath", '/html/body/div[1]/main/div[3]/div/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[1]/u/a').text
    
    # Get order date using XPath
    order_dat = driver.find_element("xpath", '/html/body/div[1]/main/div[3]/div/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[5]').text
    
    # Get customer name using XPath
    customer = driver.find_element("xpath", '/html/body/div[1]/main/div[3]/div/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[6]').text

    # Get bill total using XPath
    bill = driver.find_element("xpath", '/html/body/div[1]/main/div[3]/div/div[1]/div/div[3]/table/tbody/tr[' + str(i) + ']/td[7]').text
    
    # Append the data to the respective lists
    order_id.append(order_nb)
    name.append(customer)
    order_date.append(order_dat)
    bill_total.append(bill)

# Create a DataFrame from the lists of order data
order_df = pd.DataFrame(list(zip(order_id, name, order_date, bill_total)), 
                        columns=['order_id', 'name', 'order_date', 'bill_total'])

# Print the DataFrame
print(order_df)
