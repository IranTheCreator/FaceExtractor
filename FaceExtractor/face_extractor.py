import cv2
import face_recognition
import os


class FaceExtractor:
    def __inti__(self):
        pass
    
    def extract_faces(input_folder, output_folder):
        # Listar todas as imagens no diretório de entrada
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Criar a pasta de saída se ainda não existir
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in image_files:
            # Carregar a imagem de entrada
            image_path = os.path.join(input_folder, filename)
            image = face_recognition.load_image_file(image_path)

            # Detectar faces na imagem usando face_recognition
            face_locations = face_recognition.face_locations(image)

            # Salvar as regiões dos rostos em novas imagens
            for i, face_location in enumerate(face_locations):
                top, right, bottom, left = face_location
                face_region = image[top:bottom, left:right]
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i}.jpg")
                cv2.imwrite(output_path, cv2.cvtColor(face_region, cv2.COLOR_RGB2BGR))
