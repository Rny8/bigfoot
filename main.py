from Objects.button import BigfootButton
import pyautogui

#four digit thing [0000 -> 9999]

buttons = {
    "0": BigfootButton(50, 50),
    "1": BigfootButton(50, 50),
    "2": BigfootButton(50, 50),
    "3": BigfootButton(50, 50),
    "4": BigfootButton(50, 50),
    "5": BigfootButton(50, 50),
    "6": BigfootButton(50, 50),
    "7": BigfootButton(50, 50),
    "8": BigfootButton(50, 50),
    "9": BigfootButton(50, 50)
}

#Guesses all possible 4 digit number combinations
def guess_codes():
    for i in range(1, 100):
        code = str(i)
        for digit in code:
            pyautogui.moveTo(buttons[digit].posX, buttons[digit].posY)
            pyautogui.click()
        print(f"Guessed {i}")

if __name__ == "__main__":
    guess_codes()