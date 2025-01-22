
# Attendify

**Attendify** is a face recognition-based attendance system that automatically registers the presence of individuals by detecting their faces through a webcam. The system captures faces in real-time, matches them with known face encodings, and logs the attendance along with the timestamp into a CSV file.

## Features

- **Real-time Face Recognition**: Uses the webcam to detect and recognize faces in real-time.
- **Attendance Logging**: Automatically logs attendance with the name and timestamp when a recognized face is detected.
- **CSV Export**: The attendance data is saved in a CSV file, organized by date.
- **Multiple Faces Support**: Supports recognition of multiple individuals at once.
- **Customizable Faces**: Easily add or update known faces by adding new images to the `faces/` folder.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

You will also need to install the following Python libraries:

```bash
pip install face_recognition opencv-python numpy
```

## How It Works

1. **Known Faces**: You need to load images of individuals to recognize. The system encodes these images into numerical representations called "face encodings."
2. **Real-time Video Feed**: The system captures frames from the webcam and processes them to detect faces.
3. **Face Comparison**: The detected faces are compared to the known face encodings. If a match is found, the system logs the individual's name and the current timestamp.
4. **Attendance Log**: The attendance log is written to a CSV file, named with the current date (`dd-mm-yyyy.csv`).

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Attendify.git
    cd Attendify
    ```

2. Add face images of known individuals in the `faces/` directory. Ensure that each image is named appropriately (e.g., `akash.jpg`, `ayush.jpg`, etc.).

3. Run the program:
    ```bash
    python face_recognition_system.py
    ```

4. Press `q` to exit the video feed and stop the program.

## CSV Log

The program generates a CSV file with the following format:
- **Name**: Name of the recognized individual.
- **Time**: The time the individual was detected.

Example CSV entry:
```csv
Akash, 15-01-2025 14:30:15
Ayush, 15-01-2025 14:31:00
```

## Contributing

Feel free to fork the repository and submit pull requests if you'd like to contribute enhancements or fixes. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, feel free to reach out via email or open an issue in the GitHub repository.
