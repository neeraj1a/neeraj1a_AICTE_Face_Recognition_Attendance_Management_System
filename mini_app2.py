import tkinter as tk
import cv2
import os

# Main window setup
window = tk.Tk()
window.title("Simple Attendance System")
window.geometry('600x400')
window.configure(background='lightgrey')

# Function to capture and save images
def take_img():
    enrollment = txt.get()
    name = txt2.get()
    if enrollment == '' or name == '':
        Notification.configure(text="Enrollment & Name required!", bg="red", fg="white")
        return

    # Ensure the Haarcascade file exists
    cascade_path = 'haarcascade_frontalface_default.xml'
    if not os.path.exists(cascade_path):
        Notification.configure(text="Error: Haarcascade file missing!", bg="red", fg="white")
        return

    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        Notification.configure(text="Error loading Haarcascade file!", bg="red", fg="white")
        return

    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")

    # Initialize camera
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cam.isOpened():
        Notification.configure(text="Error: Camera not accessible!", bg="red", fg="white")
        return

    sampleNum = 0
    while True:
        ret, img = cam.read()
        if not ret:
            Notification.configure(text="Error: Unable to read from camera!", bg="red", fg="white")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            sampleNum += 1
            cv2.imwrite(f"TrainingImage/{name}.{enrollment}.{sampleNum}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Capturing Images', img)
        if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum >= 20:
            break
    cam.release()
    cv2.destroyAllWindows()
    Notification.configure(text=f"Images saved for Enrollment: {enrollment}, Name: {name}", bg="green", fg="white")

# GUI Elements
message = tk.Label(window, text="Simple Attendance System", bg="black", fg="white", width=40, height=2, font=('times', 15, 'bold'))
message.place(x=50, y=20)

lbl = tk.Label(window, text="Enter Enrollment: ", width=20, height=2, fg="black", bg="lightgrey", font=('times', 12, 'bold'))
lbl.place(x=50, y=100)

txt = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 12))
txt.place(x=250, y=115)

lbl2 = tk.Label(window, text="Enter Name: ", width=20, fg="black", bg="lightgrey", height=2, font=('times', 12, 'bold'))
lbl2.place(x=50, y=150)

txt2 = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 12))
txt2.place(x=250, y=165)

Notification = tk.Label(window, text="", bg="lightgrey", fg="black", width=40, height=2, font=('times', 12))
Notification.place(x=50, y=250)

takeImg = tk.Button(window, text="Capture Images", command=take_img, fg="black", bg="lightblue", width=15, height=2, font=('times', 12, 'bold'))
takeImg.place(x=50, y=320)

window.mainloop()
