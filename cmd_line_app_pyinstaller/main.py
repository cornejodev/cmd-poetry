from bs4 import BeautifulSoup
import requests


# poetry run python cmd_line_app_pyinstaller/cmd_line_app.py
def get_data():
    response = requests.get("https://www.google.com")
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title")
    print(f"Hi, the title element of Google's webpage is: {title.text}")


if __name__ == "__main__":
    get_data()
    input("Press Enter to close...")
