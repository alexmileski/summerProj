import PySimpleGUI as sg

layout = [
    [sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")],
    [sg.Text('Text', size=(15)), sg.InputText(key='Name')]
]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

# must use xlaunch to see the GUI https://aaroalhainen.medium.com/working-with-guis-in-wsl2-790ed1653279