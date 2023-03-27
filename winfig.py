import tkinter
from tkinter import *
import requests


def btn_clicked():
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/EUR-BRL')
    dicionario_moeda = requisicao.json()
    valorReais = entry0.get()
    valorReais = float(valorReais)
    euroHoje = dicionario_moeda['EURBRL']["bid"]
    euroHoje = float(euroHoje)
    euro = valorReais / euroHoje
    mensagem = tkinter.Label(window, text='')
    if euro:
        mensagem['text'] = 'A cotação é de € {:.2f}'.format(euro)
        mensagem.config(justify="center", fg='white', bg='#060606')
        mensagem.place(
            x=504,
            y=308
        )
        mensagem3 = tkinter.Label(window, text=f'€ {1.00:.2f} = R$ {euroHoje:.2f}')
        mensagem3.config(justify="center", fg='white', bg='#060606')
        mensagem3.place(
            x=504,
            y=378
        )
    else:
        mensagem2 = tkinter.Label(window, text='Insira um valor válido!')
        mensagem2.config(justify="center", fg='white', bg='#060606')
        mensagem2.place(
            x=504,
            y=308,
        )

window = Tk()

window.title('Cotação de Euro')

caminho = "cambio.ico"
window.iconbitmap(caminho)

window.geometry("753x446")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 446,
    width = 753,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    389.5, 223.0,
    image=background_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0
)

entry0.place(
    x = 443,
    y = 187,
    width = 250,
    height = 50
)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    background="#060606",
    command = btn_clicked,
    relief = "ridge")


b0.place(
    x = 504, y = 260,
    width = 125,
    height = 36)



window.resizable(False, False)
window.mainloop()