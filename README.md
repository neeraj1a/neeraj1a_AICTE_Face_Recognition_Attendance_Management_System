Attendance Management System using Facial Recognition
Welcome to the Attendance Management System, a comprehensive solution that leverages facial recognition to automate attendance marking. This project provides both smart (via facial recognition) and manual attendance recording features, along with an admin panel to manage student records efficiently.

Table of Contents
Features
Technologies Used
Installation Guide
Usage Guide
License
Features
Real-time Facial Recognition: Use your webcam to automatically record attendance.
GUI Interface: User-friendly graphical interface for seamless interaction.
Smart Attendance: Automatically recognize and mark attendance based on stored facial data.
Manual Attendance: Enter attendance details manually for additional flexibility.
Admin Panel: Manage and view student data directly from the application.
Technologies Used
Python: Core language for implementation.
Tkinter: For creating the graphical user interface.
OpenCV: For face detection and recognition.
Pandas: For handling CSV files and data analysis.
Pillow: For image processing.
Installation Guide
Prerequisites
Install Python (version 3.8 or above) from the official Python website.
Install VS Code for code editing and execution.
Setup Steps
1. Clone the Repository
```bash git clone <repository_url> cd <project_directory> ```

2. Set Up Virtual Environment
Open VS Code and launch the terminal using `Ctrl + ` (backtick). Run the following commands: ```bash python -m venv venv venv\Scripts\activate # Use & .venv\Scripts\Activate.ps1 for PowerShell ```

3. Install Dependencies
Upgrade `pip` and install the required libraries: ```bash python -m pip install --upgrade pip pip install opencv-contrib-python numpy pandas matplotlib ipywidgets ipython pillow ```

4. Configure Python Interpreter
Press `Ctrl + Shift + P` in VS Code, search for Python: Select Interpreter, and choose the interpreter from your `venv` folder.

Usage Guide
Launch the Application
Run the following command to start the application: ```bash python main.py ```

Application Workflow
1. Take Images
Capture images of students for training the model.
Take Images

2. Train Images
Train the facial recognition model using the captured images.
Train Images

3. Smart Attendance
Automatically record attendance by recognizing faces.
Smart Attendance

4. Manual Attendance
Manually enter attendance when necessary.
Manual Attendance

5. Admin Panel
View and manage registered student details.
Admin Panel

Closing the Application
The app supports a safe exit via the Close Camera button or the window close button.
