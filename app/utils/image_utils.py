import numpy as np
import cv2

COR_BRANCA = 255
FORCA_FILTRO = 2
TAMANHO_KERNEL = 2

def remove_white_borders(imagem):
    imagem_binaria = gera_imagem_binaria(imagem)
    imagem_binaria = remocao_ruidos(imagem_binaria)
    return identifica_retangulo(imagem, imagem_binaria)

def gera_imagem_binaria(imagem):
    imagem_escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_binaria = cv2.threshold(imagem_escala_cinza, 0, WHITE_COLOR, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return imagem_binaria

def remocao_ruidos(imagem_base, imagem_binaria):
    kernel = np.ones((TAMANHO_KERNEL,TAMANHO_KERNEL), np.uint8)
    imagem_final = cv2.fastNlMeansDenoising(imagem_binaria, h=FORCA_FILTRO)
    imagem_final = cv2.erode(imagem_final, kernel)
    imagem_final = cv2.dilate(imagem_final, kernel)
    return imagem_final


def identifica_retangulo(imagem, imagem_binaria):
    coordenadas = cv2.findNonZero(imagem_binaria)
    x, y, width, height = cv2.boundingRect(coordenadas)
    return imagem[y:y+height, x:x+width]

def identifica_retangulo_minimo(imagem, imagem_binaria):
    coordenadas = cv2.findNonZero(imagem_binaria)
    retangulo = cv2.minAreaRect(coordenadas)
    matriz_transformacao = cv2.getRotationMatrix2D(retangulo[0], retangulo[2], 1)
    imagem_rotacionada = cv2.warpAffine(imagem, matriz_transformacao, imagem.shape)
    imagem_final = cv2.getRectSubPix(imagem_rotacionada, retangulo[1], retangulo[0])
    return imagem_final

