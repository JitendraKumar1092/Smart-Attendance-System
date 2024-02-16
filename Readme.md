# Attendance Management System using Face Recognition

This project is an Attendance Management System implemented using face recognition technology. It allows for automated attendance tracking by recognizing faces of registered students in a live video feed.

## Features

- **Face Recognition**: Utilizes the face_recognition library to recognize faces from live video input.
- **Attendance Logging**: Records attendance data including student names and timestamps in a CSV file.
- **Real-time Updates**: Updates the UI in real-time to display the attendance status of students.
- **Percentage Calculation**: Calculates the percentage of students present and displays it in the UI.

## Setup

1. **Install Dependencies**: Ensure you have Python installed along with the required libraries. You can install the necessary dependencies using pip:

    ```
    pip install numpy opencv-python-headless face_recognition tkinter
    ```

2. **Dataset Preparation**: Add images of students to the `faces` directory. The file name should correspond to the student's name.

3. **Run the Application**: Execute the `attendance_system.py` script to start the attendance management system.

## Usage

- Upon running the application, the live video feed will be displayed.
- As students' faces are recognized, their attendance will be marked and displayed in the UI.
- Press 'q' to exit the application.
- Press 'l' to log out a student manually.

## Project Structure

- `attendance_system.py`: Main script implementing the attendance management system.
- `faces/`: Directory containing images of registered students.
- `README.md`: Markdown file containing project information and setup instructions.
- `attendance_<date>.csv`: CSV file containing attendance data for each session.

## Dependencies

- **numpy**: For numerical operations.
- **opencv-python-headless**: For capturing and processing video input.
- **face_recognition**: For face recognition functionality.
- **tkinter**: For building the graphical user interface.

## Author

- Jitendra Kumar Yadav 
  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.