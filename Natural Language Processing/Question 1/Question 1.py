"""
Q-1. Take any YouTube videos link and your task is to extract the comments from
that videos and store it in a csv file and then you need define what is most
demanding topic in that videos comment section.
"""

#Ans:

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the YouTube video URL
video_url = "https://youtu.be/cjhlcIOgUy4"

# Path to chromedriver executable
chromedriver_path = "Natural Language Processing\Question 1\chromedriver.exe"  # Replace with the actual path to your chromedriver executable

# Configure the Chrome service
service = Service(chromedriver_path)

# Configure Selenium web driver
driver = webdriver.Chrome(service=service)
driver.get(video_url)

# Scroll and load all the comments
while True:
    try:
        # Locate the "Show more" button and click it
        show_more_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//yt-formatted-string[@class='more-button style-scope ytd-comment-replies-renderer']"))
        )
        show_more_button.click()
    except:
        # Break the loop if there are no more comments to load
        break

# Extract the comments from the loaded page
comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")

# Store the comments in a CSV file
csv_filename = 'youtube_comments.csv'
with open(csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Comment'])
    writer.writerows([[comment.text] for comment in comments])

print(f"Comments extracted and stored in '{csv_filename}'")

# Close the web driver
driver.quit()
