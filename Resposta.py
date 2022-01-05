from math import radians, sin, cos
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Simbolos usados para a legenda do grafico:
div = '\u221F'
grau = '\u00B0'


def angulo(ang):
    """
    Encontra um equivalente angular entre 0 e 360 graus para qualquer angulo
    :param ang: Angulo desejado
    :return: O angulo equivalente
    """
    while True:
        if 0 <= ang <= 360:
            break
        elif ang < 0:
            ang += 360
        elif ang > 360:
            ang -= 360
    return ang


def Calcular(A, ang):
    """
    Gera o grafico
    :param A: Amplitude do fasor
    :param ang: Angulo do fasor
    :param basewidth: Tamanho da imagem
    :param teta: Angulo em radianos
    :param tamanho: Quantidade de pontos do grafico
    :param x: Vetor com os valores de do eixo Real
    :param y: Vetor com os valores de do eixo Imaginario
    :return: A imagem do grafico no formato png atualizada
    """
    #Definindo Variaveis
    basewidth = 500
    teta = radians(angulo(ang))
    tamanho = np.linspace(0, A, 100)

    #Gerando X e Y
    x = np.array([eixo_x(ponto, teta) for ponto in tamanho])
    y = np.array([eixo_y(ponto, teta) for ponto in tamanho])

    #Gerando o Grafico e salvando a imagem
    plt.tight_layout()
    plt.style.use('ggplot')
    plt.plot(x, y, label=f'{A}{div}{ang}{grau}')
    plt.title('Diagrama Fasorial')
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.legend(loc='best')
    plt.savefig('grafico.png', format='png')

    #Redimensionado o gráfico
    img = Image.open('grafico.png')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('grafico.png')


def eixo_x(A, teta):
    """
    Gera o valor de x dado um angulo e amplitude
    :param A: Amplitude atual
    :param teta: Angulo do fasor em radianos
    :return: O ponto equivalente para a amplitude atual
    """
    x = A * cos(teta)
    return x


def eixo_y(A, teta):
    """
    Gera o valor de y dado um angulo e amplitude
    :param A: Amplitude atual
    :param teta: Angulo do fasor em radianos
    :return: O ponto equivalente para a amplitude atual
    """
    y = A * sin(teta)
    return y


