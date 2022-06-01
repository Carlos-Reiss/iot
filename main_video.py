import time
import cv2
from simple_facerec import SimpleFacerec

# task: 
  # 0. ter logs de cada etapa
  # 1. encodar as imagens da pasta "imagens"
  # 2. carregar a camera
  # 4. detectar os rostos
  #  4.1. se nao conhecido, enviar sinal ou SMS
  # 5. Sinal para liberação da porta 
  # 6. Caso o cara for visitante ou nao conhecido, tocar campainha e enviar sinal ou SMS

# Encoda as imagens da pasta "imagens"
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Carrega a camera
cap = cv2.VideoCapture(0)

def is_face_recognized():

    tempo_comp = int(round(time.time())) + 30

    while True:
        tempo_atual_s = int(round(time.time()))
        if tempo_atual_s > tempo_comp:
            print("Tempo expirado. Rosto nao reconhecido.")
            break

        ret, frame = cap.read()

        # Detecta os rostos
        localizacao_rosto, nome_rosto = sfr.detect_known_faces(frame)

        if nome_rosto != "Nao conhecido":
            print("Abrir porta.")
            break

        #for face_loc, name in zip(localizacao_rosto, nome_rosto):
        #    y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        #    cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        #    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        #cv2.imshow("Frame", frame)

        #key = cv2.waitKey(1)
        #if key == 27:
        #    break

    cap.release()