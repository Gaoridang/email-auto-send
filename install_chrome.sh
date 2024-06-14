# Since the user is still facing issues with the installation, let's debug the script.
# I will now write a comprehensive install script with additional debug information.
# The script will log each step to a temporary file so we can trace where the failure occurs.

install_script = """
#!/bin/bash

# Log file
LOGFILE=/tmp/install_chrome.log

# Start logging
echo "Starting Chrome installation" > $LOGFILE

# Step 1: Install Google Chrome
{
    echo "Step 1: Adding Google signing key" >> $LOGFILE
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
    echo "Step 1: Added Google signing key" >> $LOGFILE

    echo "Step 2: Adding Google Chrome repository" >> $LOGFILE
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
    echo "Step 2: Added Google Chrome repository" >> $LOGFILE

    echo "Step 3: Updating package list" >> $LOGFILE
    apt-get update
    echo "Step 3: Package list updated" >> $LOGFILE

    echo "Step 4: Installing Google Chrome" >> $LOGFILE
    apt-get install -y google-chrome-stable
    echo "Step 4: Installed Google Chrome" >> $LOGFILE
} || {
    echo "Failed to install Google Chrome" >> $LOGFILE
    exit 1
}

# Step 2: Install ChromeDriver
{
    echo "Step 5: Fetching ChromeDriver version" >> $LOGFILE
    CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
    echo "Step 5: Fetched ChromeDriver version $CHROME_DRIVER_VERSION" >> $LOGFILE

    echo "Step 6: Downloading ChromeDriver" >> $LOGFILE
    wget -N https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip -P /tmp
    echo "Step 6: Downloaded ChromeDriver" >> $LOGFILE

    echo "Step 7: Unzipping ChromeDriver" >> $LOGFILE
    unzip /tmp/chromedriver_linux64.zip -d /usr/bin
    echo "Step 7: Unzipped ChromeDriver" >> $LOGFILE

    echo "Step 8: Setting permissions for ChromeDriver" >> $LOGFILE
    chmod +x /usr/bin/chromedriver
    echo "Step 8: Set permissions for ChromeDriver" >> $LOGFILE

    echo "Step 9: Cleaning up" >> $LOGFILE
    rm /tmp/chromedriver_linux64.zip
    echo "Step 9: Cleaned up" >> $LOGFILE

    echo "ChromeDriver installation completed" >> $LOGFILE
} || {
    echo "Failed to install ChromeDriver" >> $LOGFILE
    exit 1
}

echo "Chrome installation completed" >> $LOGFILE
"""

# Save the script to a file
with open("/mnt/data/install_chrome.sh", "w") as file:
    file.write(install_script)

"/mnt/data/install_chrome.sh"
