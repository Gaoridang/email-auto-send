import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Streamlit 앱 시작
st.title("Naver Title Scraper with Selenium")


def get_page_title(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    title = driver.title
    driver.quit()
    return title


# URL 입력받기
url = st.text_input("Enter the URL to scrape", "http://naver.com")

if st.button("Get Page Title"):
    title = get_page_title(url)
    st.write(f"Page title: {title}")
