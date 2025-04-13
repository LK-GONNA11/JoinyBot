# JoinyBot 

## Description

JoinyBot is a Python script that automates joining Discord servers and sending messages using Selenium WebDriver. It allows users to search for servers on Disboard based on keywords and automatically join the first three results. It also provides a spamming feature to send a message multiple times in a specified channel.

## Prerequisites

Before running JoinyBot, ensure you have the following installed:

* **Python 3.x:** Ensure Python is installed on your system.
* **Selenium WebDriver:** Install the Selenium library using pip:
    ```bash
    pip install selenium
    ```
* **WebDriver for your browser:**
    * **Chrome:** Download `chromedriver` from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) and place it in a location accessible by your system's PATH or in the same directory as the script.
    * **Firefox:** Download `geckodriver` from [Mozilla Geckodriver Releases](https://github.com/mozilla/geckodriver/releases) and place it in a location accessible by your system's PATH or in the same directory as the script.
* **Discord Account:** You need a Discord account to log in and join servers.
* **Git (Optional):** If you want to manage your code with Git, ensure you have it installed.

## Installation and Git Management

1.  **Clone the repository (if using Git):**
    ```bash
    git clone https://github.com/LK-GONNA11/JoinyBot.git
    cd JoinyBot
    ```
2.  **Install dependencies:**
    ```bash
    pip install selenium
    ```
3.  **Download WebDriver:**
    * Place `chromedriver` or `geckodriver` in the project directory or ensure it is accessible via your system's PATH.
4.  **Run the script:**
    ```bash
    python JoinyBot.py
    ```

## Usage

1.  Open a terminal or command prompt and navigate to the directory containing `JoinyBot.py`.
2.  Run the script:
    ```bash
    python JoinyBot.py
    ```
3.  The script will prompt you to choose a browser (1 for Chrome, 2 for Firefox).
4.  After selecting the browser, the script will open the Discord login page. Log in to your Discord account.
5.  After logging in, press Enter in the terminal.
6.  The script will then navigate to the Disboard server search page and prompt you to enter a keyword.
7.  Enter the keyword to search for servers and press Enter.
8.  The script will display the number of servers found and automatically join the first three servers.
9.  Next, the script will prompt you to enter a message to spam.
10. Enter the message and press Enter.
11. The script will then prompt you to enter the number of times to send the message.
12. Enter the number of times and press Enter.
13. The Script will prompt you to enter the delay in seconds between each message.
14. Enter the delay in seconds and press Enter.
15. The script will then spam the message in the currently active Discord text channel.
16. The script will then finish and close.

## Script Breakdown

* **Imports:** The script imports necessary modules from Selenium and the operating system.
* **`C0()`:** Clears the console.
* **`S0()`:** Prints a separator line for better readability.
* **Browser Selection:** Prompts the user to choose between Chrome and Firefox and initializes the WebDriver accordingly.
* **Discord Login:** Opens the Discord login page and waits for the user to log in manually.
* **Disboard Server Search:** Navigates to Disboard, searches for servers based on the user's keyword, and joins the first three servers.
* **Spamming:** Prompts the user for a message, the number of times to send it, and the delay between messages, then sends the message repeatedly in the active Discord text channel.
* **Error Handling:** Includes `try...except` blocks to handle potential errors during server joining and message sending.

## Notes

* Ensure that the WebDriver version matches your browser version.
* Be cautious when using the spamming feature and avoid excessive spamming, as it may violate Discord's terms of service.
* This script is for educational purposes only. Use it responsibly.
* The script assumes that the correct element names and class names are present in the web pages. If Discord or Disboard update their website structure, the script may need to be updated.
* If you are using Git, remember to add a `.gitignore` file to exclude sensitive files (like credentials) from tracking.
