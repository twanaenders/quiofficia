from selenium import webdriver

# Create a service that will use the WebDriver executable at the specified path
service = webdriver.Service(executable_path="/usr/local/bin/chromedriver")

# Start the WebDriver server
service.start()

# Create a WebDriver instance using the service
driver = webdriver.Remote(command_executor=service.service_url, desired_capabilities=webdriver.DesiredCapabilities.CHROME)

# Use the WebDriver instance to interact with the browser
driver.get("https://www.example.com Stop the WebDriver server
service.stop()
