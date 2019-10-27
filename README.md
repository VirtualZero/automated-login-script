# automated-login-script
Powered by [VirtualZero](https://virtualzero.net "VirtualZero's Website")

Some agreements with employers and education institutions include free memberships to websites like Pluralsight, but to keep the subscription active, you must login every (insert number here) days. This script solves this problem by automating the login process allowing you to keep your valuable subscriptions active during periods of inactivity.

## Installation

### 1. Clone the automated-login-script repository to your machine. 

Copy the following command to clone the repository:

```sh
git clone https://github.com/VirtualZero/automated-login-script.git
```

### 2. Install pip3 & pipenv

If you do not have pip3 installed on your machine, copy the following command:

```sh
sudo apt install pip3 -y
```

If you do not have pipenv installed on your machine, copy the following command:

```sh
pip3 install --user pipenv
```

### 3. Create the virtual environment and install the dependencies

Copy the following command to move into the cloned directory, create the virtual environment, and install the dependencies:

```sh
cd automated-login-script && pipenv install
```

### 4. Install the correct drivers for the browsers installed on the target machine. Information on this is available in [Selenium](https://selenium-python.readthedocs.io/installation.html#drivers "Selenium's Driver Documentation")'s documentation.

### 5. Create a .env file to store your variables in. Your .env file should look like this:

```sh
username='YOUR-LOGIN-USERNAME'
password='YOUR-LOGIN-PASSWORD'
login_url='WEBSITE-LOGIN-PAGE-URL'
username_id='LOGIN-FORM-USERNAME-ID'
password_id='LOGIN-FORM-PASSWORD-ID'
submit_btn_id='LOGIN-FORM-SUBMIT-BUTTON-ID'
```

### 6. Finally, to execute the script enter the following command:

```sh
pipenv run python automated-login-script.py
```

#### To complete the login automation, schedule the script to run using cron, Task Scheduler, or a similar alternative.