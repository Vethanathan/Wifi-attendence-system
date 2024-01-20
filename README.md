# Attendance Management System

## Project Overview

This repository contains an Attendance Management System developed in Python. The system utilizes computer vision techniques to automatically capture and record attendance of individuals present in a room. It offers a convenient and efficient solution for attendance tracking, eliminating the need for manual recording.

## Features

- **Automatic Attendance:** The system automatically captures and logs attendance based on the presence of individuals in a room.
- **Python-Based:** Developed entirely in Python, making it easily accessible and modifiable.
- **Computer Vision:** Utilizes computer vision libraries for real-time detection and recognition of individuals.
- **Efficiency:** Provides a time-efficient and accurate alternative to traditional manual attendance methods.
- **Network Scanning:** Utilizes Nmap for network scanning to enhance security and control access to the attendance system.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- OpenCV
- NumPy
- Nmap

Install required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the attendance system script:

```bash
python attendance_system.py
```

2. The system will automatically detect individuals in the room, mark their attendance, and perform a network scan for added security.

## File Structure

- **`attendance_system.py`**: Main script for the attendance system.
- **`haarcascades/`**: Directory for Haar cascades used in face detection.
- **`data/`**: Directory to store attendance records.

## Configuration

Adjust the configuration parameters in `attendance_system.py` as needed:

```python
# Configuration Parameters
CASCADE_PATH = "haarcascades/haarcascade_frontalface_default.xml"
RECOGNIZER_PATH = "data/recognizer.yml"
LABELS_PATH = "data/labels.pickle"
```

## Attendance Records

Attendance records are stored in the `data/` directory. Each session's attendance is saved in a separate file.

## Security

The system employs Nmap for network scanning to ensure enhanced security and control access to the attendance system.

## Acknowledgments

- OpenCV: [https://opencv.org/](https://opencv.org/)
- Nmap: [https://nmap.org/](https://nmap.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For any questions or inquiries, please contact [vethanathan] at [vethanathanvk@gmail.com].
