import cv2
import face_recognition
import os

class FaceExtractor:
    def __init__(self):
        """
        Initializer for the FaceExtractor class.
        No specific initializations are needed at this point.
        """
        pass
    
    def extract_faces(self, input_folder, output_folder):
        """
        Extracts faces from images in an input directory and saves face regions in an output directory.

        Parameters:
        - input_folder (str): Path to the directory containing input images.
        - output_folder (str): Path to the directory where face regions will be saved as new images.
        """
        # List all images in the input directory
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        # Create the output folder if it doesn't exist yet
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in image_files:
            # Load the input image
            image_path = os.path.join(input_folder, filename)
            image = face_recognition.load_image_file(image_path)

            # Detect faces in the image using face_recognition
            face_locations = face_recognition.face_locations(image)

            # Save face regions as new images
            for i, face_location in enumerate(face_locations):
                top, right, bottom, left = face_location
                
                # Extract the face region from the original image
                face_region = image[top:bottom, left:right]
                
                # Create the path for the new output image
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i}.jpg")
                
                # Save the face region as a new image using OpenCV
                cv2.imwrite(output_path, cv2.cvtColor(face_region, cv2.COLOR_RGB2BGR))
