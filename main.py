from Objects.button import BigfootButton
import pyautogui
from time import sleep


click_delay = 0.0000000005
#four digit thing [0000 -> 9999]

buttons = {
    "0": BigfootButton(954, 580),
    "1": BigfootButton(748, 491),
    "2": BigfootButton(955, 486),
    "3": BigfootButton(1160, 490),
    "4": BigfootButton(748, 403),
    "5": BigfootButton(954, 405),
    "6": BigfootButton(1160, 406),
    "7": BigfootButton(748, 318),
    "8": BigfootButton(955, 320),
    "9": BigfootButton(1160, 748),
    "enter": BigfootButton(970, 748)
}

#Guesses all possible 4 digit number combinations
def guess_codes():
    sleep(3) #start delay
    for i in range(1, 26):
        pyautogui.press('e')
        code = str(i).rjust(4, '0')
        for digit in code:
            pyautogui.moveTo(buttons[digit].posX, buttons[digit].posY, duration=0, _pause=False)
            sleep(click_delay)
            pyautogui.click()
           
        pyautogui.moveTo(buttons['enter'].posX, buttons['enter'].posY, duration=0, _pause=False)
        sleep(click_delay)
        pyautogui.click()
        print(f"Guessed {code}")

def collect_codes():
    while True:
        print(pyautogui.position())


if __name__ == "__main__":
    guess_codes()