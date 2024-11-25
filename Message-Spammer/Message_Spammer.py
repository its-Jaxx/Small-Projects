import time, math, random
import pyautogui as pui

messages = [
    'test1',
    'test2',
    'test3'
]

def numbers_only(s):
    return int(''.join(filter(str.isdigit, s)))

q = input("Enter amount of messages to send: ")
x = numbers_only(q)

delay = input("Enter delay in milliseconds: ")
delay = int(delay) / 1000

print(f"\nSending {x} messages in:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

for _ in range(x):
    a = random.choice(messages)
    pui.write(f"Hello {a}!")
    pui.press('enter')
    time.sleep(delay)

if x == 1:
    print("\n1 Message Sent!")
elif x > 1:
    print(f"\n{x} Messages Sent!")
