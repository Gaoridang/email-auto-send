#!/bin/bash

echo "Starting Chrome installation" >> /tmp/install_chrome.log

# Install Google Chrome
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "Added Google Linux signing key" >> /tmp/install_chrome.log

echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
apt-get update
apt-get install -y google-chrome-stable

echo "Installed Google Chrome" >> /tmp/install_chrome.log

# Install ChromeDriver
CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip -P /tmp
unzip /tmp/chromedriver_linux64.zip -d /usr/bin
chmod +x /usr/bin/chromedriver
rm /tmp/chromedriver_linux64.zip

echo "Installed ChromeDriver" >> /tmp/install_chrome.log
