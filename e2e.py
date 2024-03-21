import requests
from bs4 import BeautifulSoup
import sys
#
# def test_scores_service(application_url):
#     try:
#         # Fetch the web page content
#         response = requests.get(application_url)
#         response.raise_for_status()
#
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Find the score element on the web page
#         score_element = soup.find('span', {'class': 'score'})  # Update with the actual tag and class
#
#         # Check if the score element exists and if its content is a number between 1 and 1000
#         if score_element and score_element.text.isdigit():
#             score_value = int(score_element.text)
#             return 1 <= score_value <= 1000
#         else:
#             return False
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching {application_url}: {e}")
#         return False
# def main_function(application_url):
#     if not test_scores_service(application_url):
#         return -1  # Tests failed, return -1 as exit code
#     return 0  # Tests passed, return 0 as exit code
#
# if __name__ == "__main__":
#     application_url = 'file:///Users/liorharel/wog_for_git/score_template.html'  # Example URL
#     exit_code = main_function(application_url)
#     sys.exit(exit_code)
#
# # application_url = 'file:///Users/liorharel/wog_for_git/score_template.html'
# # result = test_scores_service(application_url)
# # print(f"Is the score valid for {application_url}? {result}")


# from bs4 import BeautifulSoup
# import sys

def test_scores_service(html_content):
    try:
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the score element on the web page
        score_element = soup.find('span', {'class': 'score'})  # Update with the actual tag and class

        # Check if the score element exists and if its content is a number between 1 and 1000
        if score_element and score_element.text.isdigit():
            score_value = int(score_element.text)
            return 1 <= score_value <= 1000
        else:
            return False

    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        return False

def main_function(html_content):
    if not test_scores_service(html_content):
        return -1  # Tests failed, return -1 as exit code
    return 0  # Tests passed, return 0 as exit code

if __name__ == "__main__":
    try:
        with open('/Users/liorharel/wog_for_git/score_template.html', 'r') as file:
            html_content = file.read()

        exit_code = main_function(html_content)
        sys.exit(exit_code)
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
