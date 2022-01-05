import PySimpleGUI as sg
from Resposta import Calcular


# Layouts:
def Inicial():
    #Tela antes da criação das imagens
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Text('Amplitude do Fasor:', size=(22, 0)),
         sg.Input(key='A', size=(10, 0))],
        [sg.Text('Ângulo do Fasor(Graus):', size=(22, 0)), sg.Input(key='ang', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - UFC', layout=layout, finalize=True)


def Com_imagem():
    #Tela após ter criado a primeira imagem
    sg.change_look_and_feel('DarkBlue3')
    layout = [
        [sg.Image('grafico.png')],
        [sg.Text('Amplitude do Fasor:', size=(52, 0)),
         sg.Input(key='A', size=(10, 0))],
        [sg.Text('Ângulo do Fasor(Graus):', size=(52, 0)), sg.Input(key='ang', size=(10, 0))],
        [sg.Button('Calcular', size=(10, 0))]
    ]
    return sg.Window('Circuitos 1 - UFC', layout=layout, finalize=True)


# Janelas Iniciais:
janela1, janela2 = Inicial(), None

# Leitor de janelas:
while True:
    window, event, value = sg.read_all_windows()
    # Ao fechar  a Janela:
    if event == sg.WIN_CLOSED:
        break
    #Ao pressionar o botão Calcular:
    elif event == 'Calcular':
        lista = ('A', 'ang')    #Valida e obtem os valores de entrada
        try:
            value['ang'] = float(value['ang'])
        except:
            sg.popup('Escolha somente um opção valida')
            continue
        try:
            value['A'] = float(value['A'])
        except:
            sg.popup('Escolha somente um opção valida')
            continue
        Calcular(value['A'], value['ang'])  #Gera o Garafico
        if janela2 is None:                 #Abre a proxima janela caso seja não tenha sido gerado nenhum grafico
            janela1.hide()
            janela2 = Com_imagem()
        else:                               #Atualiza o grafico já gerado
            janela2.hide()
            janela2 = Com_imagem()
