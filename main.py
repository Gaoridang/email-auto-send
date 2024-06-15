import streamlit as st
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Streamlit 애플리케이션
st.title("Streamlit에서 셀레니움 사용하기")


def install_chrome():
    # 크롬 다운로드 및 설치
    if not os.path.exists("/usr/bin/google-chrome"):
        os.system(
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
        )
        os.system("apt-get install -y ./google-chrome-stable_current_amd64.deb")
        os.system("rm google-chrome-stable_current_amd64.deb")


def install_chromedriver():
    # 크롬 드라이버 다운로드 및 설치
    if not os.path.exists("/usr/bin/chromedriver"):
        os.system(
            "wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip"
        )
        os.system("unzip chromedriver_linux64.zip")
        os.system("mv chromedriver /usr/bin/chromedriver")
        os.system("chmod +x /usr/bin/chromedriver")
        os.system("rm chromedriver_linux64.zip")


if st.button("셀레니움 실행"):
    install_chrome()
    install_chromedriver()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.naver.com")
    st.write("페이지 타이틀:", driver.title)
    driver.quit()
