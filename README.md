# FaceExtractor

FaceExtractor is a Python package that extracts faces from images using the face_recognition and OpenCV libraries.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FaceExtractor.

```bash
pip install simntek-face-extractor
```

## Usage

```python
from your_package_name.face_extractor import FaceExtractor

# Create an instance of the FaceExtractor
face_extractor = FaceExtractor()

# Define the input and output directories
input_directory = "path/to/input_directory"
output_directory = "path/to/output_directory"

# Call the method to extract faces
face_extractor.extract_faces(input_directory, output_directory)

```

## Features
- Extract faces from images in a specified directory.
- Save face regions as new images.
- Dependencies
- opencv-python
- face_recognition
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT

## Acknowledgments
Thanks to the creators of OpenCV and face_recognition libraries.


