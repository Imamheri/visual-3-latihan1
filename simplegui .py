import PySimpleGUI as sg

# Layout jendela
layout = [
    [sg.Text("Hello, World!")],
    [sg.Button("OK")]
]

# Membuat jendela
window = sg.Window("My First GUI", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "OK":
        break

window.close()
