# Importing all the required libraries
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_reviews(product_url, num_reviews_to_scrape=10):
    # Calling the driver
    driver = webdriver.Chrome()  # You should have ChromeDriver installed and in your PATH

    # Requesting the Amazon product's url
    driver.get(product_url)


    # Extracting our review data
    reviews = []
    review_elements = driver.find_elements(By.CSS_SELECTOR, '.a-section.review')
    for review_element in review_elements[:num_reviews_to_scrape]:
        review = {}
        review['author'] = review_element.find_element(By.CSS_SELECTOR, '.a-profile-name').text.strip()
        review['date'] = review_element.find_element(By.CSS_SELECTOR, '.review-date').text.strip()
        review['text'] = review_element.find_element(By.CSS_SELECTOR, '.review-text-content').text.strip()
        reviews.append(review)
        print(review)

    # Terminating the WebDriver
    driver.quit()
    # Returning the reviews
    return reviews



# Product url
product_url = 'https://www.amazon.com/ENHANCE-Headphone-Customizable-Lighting-Flexible/dp/B07DR59JLP/'

# Calling the extract_reviews() function
reviews_data = extract_reviews(product_url, num_reviews_to_scrape=10)



# Creating a function to export the data to csv
def export_csv(reviews, csv_filename='reviews_data.csv'):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Author', 'Date', 'Review']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for review in reviews:
            writer.writerow({'Author': review['author'], 'Date': review['date'], 'Review': review['text']})


# Export data to a csv file
export_csv(reviews_data)