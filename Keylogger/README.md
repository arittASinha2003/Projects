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

4. The script will stop logging when the Page Down key is pressed.

## Warning

Key loggers can be used maliciously to record sensitive information like passwords. This script is intended only for educational purposes. Do not use it to invade someone's privacy. Misuse of this script can result in criminal charges. The author is not responsible for any misuse of this script. Use it responsibly.
