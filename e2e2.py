import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service(application_url):
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Open the application URL
        driver.get(application_url)

        # Wait for the score element to be present on the webpage
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'score')))

        # Find the score element on the web page
        score_element = driver.find_element_by_class_name('score')

        # Get the text content of the score element
        score_text = score_element.text.strip()

        # Check if the score element content is a number between 1 and 1000
        if score_text.isdigit():
            score_value = int(score_text)
            if 1 <= score_value <= 1000:
                return True
            else:
                return False
        else:
            return False

    except NoSuchElementException:
        print("Score element not found on the web page.")
        return False

    except Exception as e:
        print(f"Error occurred while testing the web service: {e}")
        return False

    finally:
        
        driver.quit()

def main_function(application_url):
    if not test_scores_service(application_url):
        return -1  # Tests failed, return -1 as exit code
    return 0  # Tests passed, return 0 as exit code

if __name__ == "__main__":
    # Example usage
    application_url = "http://localhost:63342/wog_for_git/score_template.html"
    exit_code = main_function(application_url)
    sys.exit(exit_code)
