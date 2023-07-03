from imagem import imagem
import cv2
from tkinter import *
from tkinter import ttk
from Janelas import *

def main():
    
    webcam = cv2.VideoCapture(0)

    window = Tk()
    window.title('Corretor de Provas')
    window.config(padx=10, pady=10)

    gabarito = Button(text = 'Criar Gabarito', 
                      width = 20 ,
                      command = criar_gabarito)

    gabarito.pack()
    corrigir = Button(text = 'corrigir provas', 
                      width = 20 ,
                      command = corrigir_provas)
    
    corrigir.pack()
    Dados = Button(text = 'Dados', 
                      width = 20 ,
                      command = dados)

    Dados.pack()

    

    window.mainloop()
    def generate_frames():
        while True:
            validation, frame = webcam.read()
            if not validation:
                break
            else:
                ret, buffer =  cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()


    ANSWER_KEY = [{0: 0, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}, 
                  {0: 1, 1: 0, 2: 0, 3: 3, 4: 1, 5: 3, 6: 3, 7: 2, 8: 2, 9: 2}]
    
    img = cv2.imread('IMG_6841 (1).JPG')
    image = imagem(img)
    processadas, papers = image.pre_processa_imagem()
    pontuação, papers = image.processa_imagem(ANSWER_KEY, processadas, papers)
    imagem_pronta = cv2.hconcat(papers)
    cv2.imshow('', imagem_pronta)
    cv2.waitKey(0)


if(__name__ == "__main__"):
    main()