import streamlit as st
from playwright.sync_api import sync_playwright

# Streamlit 앱 시작
st.title("Naver Title Scraper with Playwright")


def get_page_title(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        browser.close()
        return title


# URL 입력받기
url = st.text_input("Enter the URL to scrape", "http://naver.com")

if st.button("Get Page Title"):
    title = get_page_title(url)
    st.write(f"Page title: {title}")
