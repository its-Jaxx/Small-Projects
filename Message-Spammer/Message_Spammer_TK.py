import time
import random
import pyautogui as pui
import tkinter as tk
from tkinter import messagebox

stop_sending = False

def stop_sending_messages(sent_messages_var, after_id, num_messages_entry, delay_entry, fixed_text_entry, random_text_entry):
    global stop_sending
    stop_sending = True
    root.after_cancel(after_id)
    sent_messages = sent_messages_var.get()
    output_label.config(text=f"\nStopped sending - sent {sent_messages} messages")
    enable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)

def send_messages(x, delay, fixed_text, random_text, sent_messages_var, num_messages_entry, delay_entry, fixed_text_entry, random_text_entry):
    global stop_sending
    sent_messages = 0

    disable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)

    for i in range(5, 0, -1):
        output_label.config(text=str(i))
        root.update()
        time.sleep(1)
        if stop_sending:
            enable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)
            return

    for _ in range(x):
        if fixed_text:
            message = f"{fixed_text} "
        else:
            message = ""

        if random_text:
            selected_random_word = random.choice(random_text)
            message += selected_random_word

        pui.write(message)
        pui.press('enter')
        root.update()
        time.sleep(delay)
        sent_messages += 1
        sent_messages_var.set(sent_messages)  # Update the shared variable
        if stop_sending:
            enable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)
            return

    sent_messages_var.set(sent_messages)
    enable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)

def start_sending_messages(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry):
    num_messages = num_messages_entry.get()
    delay_value = delay_entry.get()
    fixed_text = fixed_text_entry.get()
    random_text = random_text_entry.get()

    if not num_messages:
        show_error_dialog("Error", "You need to enter how many messages you want to send.")
        return

    if not delay_value:
        show_error_dialog("Error", "You need to enter a number for the delay.")
        return

    if not fixed_text and not random_text:
        show_error_dialog("Error", "You need to enter a message in either 'Fixed text field' or 'Random word field'.")
        return

    try:
        x = int(num_messages)
        delay = int(delay_value) / 1000
        random_text = random_text.split(', ') if random_text else []
    except ValueError:
        show_error_dialog("Error", "Please enter valid numerical values.")
        return

    output_label.config(text=f"\nSending {x} messages in:")
    root.update()

    global stop_sending
    stop_sending = False

    sent_messages_var = tk.IntVar()
    sent_messages_var.set(0)

    after_id = root.after(0, send_messages, x, delay, fixed_text, random_text, sent_messages_var, num_messages_entry, delay_entry, fixed_text_entry, random_text_entry)

    stop_button.config(command=lambda: stop_sending_messages(sent_messages_var, after_id, num_messages_entry, delay_entry, fixed_text_entry, random_text_entry))

def show_error_dialog(title, message):
    messagebox.showerror(title, message, fg='red')

def disable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry):
    num_messages_entry.config(state=tk.DISABLED)
    delay_entry.config(state=tk.DISABLED)
    fixed_text_entry.config(state=tk.DISABLED)
    random_text_entry.config(state=tk.DISABLED)

def enable_entry_fields(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry):
    num_messages_entry.config(state=tk.NORMAL)
    delay_entry.config(state=tk.NORMAL)
    fixed_text_entry.config(state=tk.NORMAL)
    random_text_entry.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Message Sender")

root.geometry("350x300")

num_messages_label = tk.Label(root, text="Enter the number of messages:")
num_messages_label.pack()
num_messages_entry = tk.Entry(root)
num_messages_entry.pack()

delay_label = tk.Label(root, text="Enter delay in milliseconds:")
delay_label.pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

fixed_text_label = tk.Label(root, text="Enter fixed text:")
fixed_text_label.pack()
fixed_text_entry = tk.Entry(root)
fixed_text_entry.pack()

random_text_label = tk.Label(root, text="Enter random words (separated by commas):")
random_text_label.pack()
random_text_entry = tk.Entry(root)
random_text_entry.pack()

output_label = tk.Label(root, text="")
output_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()

send_button = tk.Button(button_frame, text="Send Messages", command=lambda: start_sending_messages(num_messages_entry, delay_entry, fixed_text_entry, random_text_entry))
send_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Stop Sending")
stop_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
