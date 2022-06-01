from time import sleep
from video import is_face_recognized



while True:
    print("==============================================================")
    option = input("[?] Digite 1 para reconhecimento facial e 2 para campainha: ")
    print("==============================================================")
    print()

    if option == "1":
        print("[*] Iniciando reconhecimento facial.")
        is_face_recognized()
    elif option == "2":
        print("[*] Iniciando o alerta da campainha.")
    else:
        print("[!] Opção não encontrada.")
    print()