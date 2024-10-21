import PySimpleGUI as sg


layout = [[sg.Text("Latihan Pertama")],
          [sg.Button("OK")]]


window = sg.Window(title="Latihan Pertama", layout=layout, size=(400, 200))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "OK":
        break


window.close()
