import PySimpleGUI as sg
sg.theme("azure")
layout=[[sg.Text("Nama   :  Imam heri utomo",font=("Arial",25,"bold"))],
[sg.Text("Nim    :   2210010170")],
[sg.Text("Kelas   :   5AnonregBJM")],
[sg.Text("Matkul  : Pemograman visual 3")]]
window = sg.Window(title="latihan pertama",layout=layout, size=(500,300),font=("Times",20))
window ()
window.close ()