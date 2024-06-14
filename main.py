import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Streamlit 애플리케이션
st.title("Streamlit에서 셀레니움 사용하기")

# 버튼 클릭 시 셀레니움으로 크롬 브라우저 실행
if st.button("셀레니움 실행"):
    # 크롬 드라이버 설정
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # GUI 없이 실행
    options.add_argument("--disable-gpu")  # GPU 비활성화
    options.add_argument("--no-sandbox")  # 샌드박스 비활성화
    options.add_argument("--disable-dev-shm-usage")  # /dev/shm 사용 비활성화

    # 크롬 드라이버 초기화
    driver = webdriver.Chrome(service=service, options=options)

    # 네이버 웹 페이지 열기
    driver.get("https://www.naver.com")
    st.write("페이지 타이틀:", driver.title)

    # 드라이버 종료
    driver.quit()
