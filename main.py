import PySimpleGUI as Sg
import pyautogui
from pynput import keyboard
from time import sleep


# for notification spam
# pyautogui.PAUSE = 0.6

pyautogui.PAUSE = 0.001


def clicker(text, quantities):
    try:
        sleep(0.5)
        for i in range(int(quantities)):
            pyautogui.typewrite(text)
            pyautogui.press("enter")
        print(f'Text "{text}" typed {quantities} times :)')
    except ValueError:
        print("Error: Number of times to type must be an integer.")


def main():
    Sg.theme("Dark")

    layout = [
        [Sg.Text("Text"), Sg.InputText(key="text")],
        [Sg.Text("Quantities"), Sg.InputText(key="quantities")],
        [
            Sg.Button("Ctrl_R (Start)", key="start"),
        ],
    ]

    window = Sg.Window(
        "AutoClicker", layout, size=(200, 100), element_justification="center", resizable=False
    )

    def on_press(key):
        if key == keyboard.Key.ctrl_r:
            window.write_event_value("start", None)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED:
            break
        try:
            if event == "start":
                text = values["text"]
                quantities = values["quantities"]
                clicker(text, quantities)
        except Exception as e:
            Sg.Popup(str(e))
    window.close()


if __name__ == "__main__":
    main()
