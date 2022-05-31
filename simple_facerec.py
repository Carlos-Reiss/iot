import face_recognition
import cv2
import os
import glob
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Carrega as imagens
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} Encodando imagens encontradas.".format(len(images_path)))

        # Armazena o encoding e o nome
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Pega o nome do arquivo
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Pega o encode
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Armazena o nome e o nome do arquivo
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encodando imagens")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Não conhecido"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
