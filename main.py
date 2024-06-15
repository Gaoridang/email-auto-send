import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Streamlit 애플리케이션
st.title("Streamlit에서 셀레니움 사용하기")


def install_chrome():
    if not os.path.exists("google-chrome"):
        # 크롬 설치
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O google-chrome.deb"
        )
        os.system("dpkg -x google-chrome.deb .")
        os.system("mv opt/google/chrome/google-chrome .")
        os.system("chmod +x google-chrome")
        os.system("rm -rf opt google-chrome.deb")


def install_chromedriver():
    if not os.path.exists("chromedriver"):
        # 크롬 드라이버 설치
        os.system(
            "wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"
        )
        os.system("unzip chromedriver_linux64.zip")
        os.system("chmod +x chromedriver")
        os.system("rm chromedriver_linux64.zip")


if st.button("셀레니움 실행"):
    install_chrome()
    install_chromedriver()

    # 크롬 실행 경로 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.binary_location = os.path.abspath("./google-chrome")

    service = Service(os.path.abspath("./chromedriver"))
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 네이버 웹 페이지 열기
    driver.get("https://www.naver.com")
    st.write("페이지 타이틀:", driver.title)
    driver.quit()
