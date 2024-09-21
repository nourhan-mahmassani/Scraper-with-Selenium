# Scraper with Selenium
Selenium Web Scraper for Order Data
Overview
This Python script uses Selenium WebDriver to automate logging into the ChowNow admin portal and scrape order-related data (order number, date, customer name, and bill total) from the dashboard. The extracted data is then stored in a Pandas DataFrame and printed for further use or analysis.

Prerequisites
To run this script, you need the following installed on your machine:

Python 3.x
Download from: https://www.python.org/downloads/

Google Chrome Browser
Download from: https://www.google.com/chrome/

ChromeDriver
Download from: https://sites.google.com/a/chromium.org/chromedriver/

Required Python Packages
You can install the necessary packages using the following commands:

bash
Copy code
pip install selenium
pip install pandas
How to Run
Download ChromeDriver:

Download the ChromeDriver that matches your version of Chrome from ChromeDriver download page.
Extract it to a location on your system and note the path.
Set Up the Script:

Open the script file and update the executable_path in the Service object with the path to your chromedriver.exe.
Provide the correct login email and password for your ChowNow admin account.
Run the Script:
Once you have set up everything, simply run the script using Python:

bash
Copy code
python scraper.py
Data Output:
After successful execution, the script will print a Pandas DataFrame containing the following columns:

order_id: The order number.
name: The customer's name.
order_date: The date of the order.
bill_total: The total bill amount.
Code Explanation
The script does the following:

Initializes a Selenium Chrome WebDriver instance.
Logs into the ChowNow admin portal using the provided email and password.
Waits for the page to load.
Iterates through the list of orders displayed on the dashboard, scraping relevant data.
Stores the data in lists.
Converts the lists into a Pandas DataFrame and prints it.
Notes
Make sure that the ChromeDriver version matches the version of your Google Chrome.
Update the XPath selectors in the script if the page structure changes or if the script fails to find elements.
Add more exception handling if needed for production environments.
Troubleshooting
Timeout Issues: If the page takes too long to load, adjust the time.sleep() duration in the script.
Element Not Found: Double-check the XPath of elements if they change.
WebDriverException: Ensure that chromedriver.exe is placed in the correct path and that the executable has permission to run.
