# Key Logger with Email Notification

This Python script uses the `pynput` library to create a key logger. The script listens for keyboard inputs and writes them to a file named `Keys123.txt`, and sends the file via email every 30 minutes. The script will stop logging when the `Page Down` key is pressed.

## Package Installation

Install the required package to run this project

1. **Pynput Library** - Allows you to control and monitor input devices (for capturing keystrokes).
```python
  pip install pynput
```

2. **SMTP Email Library** - Used for sending emails with attachments.
```python
  pip install secure-smtplib
```

3. **Python-Dotenv Library** - Used to load the environment variables.
```python
  pip install python-dotenv
```

## Usage

1. Set up environment variables for your email credentials:
- `FROM_EMAIL`: The email address from which the log will be sent.
- `TO_EMAIL`: The recipient's email address.
- `EMAIL_PASSWORD`: The password for the email account. (or)
- `EMAIL_APP_PASSWORD`: App-specific password.

```bash
# Sender's email address
FROM_EMAIL=xxx@gmail.com

# Recipient's email address
TO_EMAIL=yyy@gmail.com

# Sender's email password (or app-specific password if using Gmail)
EMAIL_PASSWORD=Pass@123 (or)
EMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
```

2. **Run the Script**: The key logger will start listening for keyboard inputs and log them to a file named Keys123.txt.

3. **Email Notification**: Every 30 minutes, the script will check if the file Keys123.txt has any content. If it does, it will send the file as an attachment to the recipient's email.

4. The script will stop logging when the `Page Down` key is pressed.

5. Press `Ctrl-C` to fully terminate the program.

## Creating App Password for Google Account

App Passwords allow you to use third-party applications (such as Python scripts) securely with Google services like Gmail, without exposing your main Google password.

**Step 1: Enable Two-Factor Authentication (2FA) on Your Google Account.**
- Visit Your Google Account Settings. [Link](https://myaccount.google.com/)
- Go to Security Settings.
- Enable 2-Step Verification.

**Step 2: Generate an App Password.**
- Go to the App Passwords Page. [Link](https://myaccount.google.com/apppasswords)
- Type the app name and click on **Create**.

**`Note`**: The App Password is a 16-character password and is only shown once. Make sure to copy and save it in a secure location.

## Warning

Key loggers can be used maliciously to record sensitive information like passwords. This script is intended only for educational purposes. Do not use it to invade someone's privacy. Misuse of this script can result in criminal charges. The author is not responsible for any misuse of this script. Use it responsibly.
