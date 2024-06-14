#!/bin/bash

# 로그 파일 경로
LOGFILE=/tmp/install_chrome.log

# 로그 시작
echo "Starting Chrome installation" > $LOGFILE

# Google Chrome 설치
{
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
    echo "Added Google Linux signing key" >> $LOGFILE

    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
    apt-get update
    apt-get install -y google-chrome-stable
    echo "Installed Google Chrome" >> $LOGFILE
} || {
    echo "Failed to install Google Chrome" >> $LOGFILE
    exit 1
}

# ChromeDriver 설치
{
    CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
    wget -N https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip -P /tmp
    unzip /tmp/chromedriver_linux64.zip -d /usr/bin
    chmod +x /usr/bin/chromedriver
    rm /tmp/chromedriver_linux64.zip
    echo "Installed ChromeDriver" >> $LOGFILE
} || {
    echo "Failed to install ChromeDriver" >> $LOGFILE
    exit 1
}

echo "Chrome installation completed" >> $LOGFILE
