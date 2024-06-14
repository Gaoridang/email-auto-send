#!/bin/bash

# Update and install necessary packages
apt-get update
apt-get install -y chromium chromium-driver

# Create a symbolic link to make chromedriver available in PATH
ln -s /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver
