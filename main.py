import re
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from email.mime.text import MIMEText
import smtplib


def get_comments(blog_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.implicitly_wait(3)

    try:
        driver.get(blog_url)
        time.sleep(10)

        wait = WebDriverWait(driver, 30)
        iframe = wait.until(EC.presence_of_element_located((By.ID, "mainFrame")))
        driver.switch_to.frame(iframe)

        try:
            comment_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="Comi223439388627"]'))
            )
            comment_button.click()
            time.sleep(5)
        except Exception as e:
            st.write(f"Error clicking comment button: {e}")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        comments = [
            comment.text.strip()
            for comment in driver.find_elements(
                By.CSS_SELECTOR, "div.u_cbox_comment_box"
            )
        ]
        return comments
    except Exception as e:
        st.write(f"Error fetching comments: {e}")
        return []
    finally:
        driver.quit()


def find_emails_in_comments(comments):
    email_addresses = []
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@naver\.com")
    for comment in comments:
        emails = email_pattern.findall(comment)
        if emails:
            email_addresses.extend(emails)
    return list(set(email_addresses))


def send_email(subject, body, to_email, from_email, email_password):
    message = MIMEText(body)
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    try:
        with smtplib.SMTP("smtp.naver.com", 587) as server:
            server.starttls()
            server.login(from_email, email_password)
            server.sendmail(from_email, to_email, message.as_string())
        st.write(f"Email sent successfully to {to_email}.")
    except Exception as e:
        st.write(f"Failed to send email to {to_email}: {e}")


def main():
    st.title("Blog Comment Checker and Email Sender")

    blog_url = st.text_input("Blog URL")
    email_sender = st.text_input("Sender Email")
    email_password = st.text_input("Email Password", type="password")
    email_subject = st.text_input("Email Subject")
    email_body = st.text_area("Email Body")

    if st.button("Check Comments"):
        comments = get_comments(blog_url)
        if comments:
            receiver_emails = find_emails_in_comments(comments)
            if receiver_emails:
                st.session_state["receiver_emails"] = receiver_emails
                st.write("Emails found:")
                for email in receiver_emails:
                    st.write(email)
            else:
                st.write("No emails found.")
        else:
            st.write("No comments found.")

    if "receiver_emails" in st.session_state and st.button("Send Emails"):
        receiver_emails = st.session_state["receiver_emails"]
        for receiver_email in receiver_emails:
            send_email(
                email_subject, email_body, receiver_email, email_sender, email_password
            )


if __name__ == "__main__":
    main()
