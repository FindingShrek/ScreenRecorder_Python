import sys
import pyautogui
import datetime

import dxcam
import cv2

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QGridLayout, QSizePolicy,QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt

class ScreenRecorder(QDialog):
    def __init__(self):
        super(ScreenRecorder, self).__init__()

        ScreenCaptureLayout = QGridLayout(self)
        
        # Window Name
        self.setWindowTitle("Screen Recorder")
        
        self.width, self.height = pyautogui.size()
        self.resize(self.width - 1000, self.height - 500)
        
        self.PreviewLabel = QLabel()
        self.RecordButton = QPushButton("Start")
        
        self.PreviewLabel.setAlignment(Qt.AlignCenter)
        self.PreviewLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.RecordButton.setFixedSize(100, 60)

        ScreenCaptureLayout.addWidget(self.PreviewLabel, 0, 0, 4, 5)
        ScreenCaptureLayout.addWidget(self.RecordButton, 4, 2, 1, 1)
        
        self.RecordButton.clicked.connect(self.StartStopButton)
        
        self.initRecorder()

    def initRecorder(self):
        # Getting the screen resolution
        width, height = pyautogui.size()
        self.width = width  # Width of the video
        self.height = height  # Height of the video
        self.target_fps = 18  # Target FPS of the video

        # ==== VIDEO ENCODER ====
        
        # Initialize VideoWriter object
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        # Creat a camera or screen capture
        self.camera = dxcam.create(output_idx = 0, output_color="BGR")
        # Stsrt capturing
        self.camera.start(target_fps = self.target_fps, video_mode = True)
        
        # A function that manage or creat a time lapse in PyQt5 GUI
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateFrame)
        self.timer.start(30)
        
        self.timer001 = QTimer(self)
        self.timer001.timeout.connect(self.timerEvent)
        self.running = False

    def StartStopButton(self):
        # Converting date and time to a string format
        self.timeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f'{self.timeStamp}.mp4'
        
        if not self.running:
            self.writer = cv2.VideoWriter(self.filename, self.fourcc, self.target_fps, (self.width, self.height))
            self.timer001.start(30)  # Start the timer
            self.RecordButton.setText('Stop')
            self.running = True
        else:
            self.timer001.stop()  # Stop the timer
            self.writer.release()
            self.RecordButton.setText('Start')
            self.running = False
            
    def timerEvent(self):
        # This function is called each time the timer times out
        self.writer.write(self.camera.get_latest_frame())

    def updateFrame(self):
        # Displaying the latest frame captured by the camera
        self.frame = cv2.cvtColor(self.camera.get_latest_frame(), cv2.COLOR_BGR2RGB)
        h, w, ch = self.frame.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(self.frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(self.PreviewLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.PreviewLabel.setPixmap(QPixmap.fromImage(p))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenRecorder()
    window.show()
    sys.exit(app.exec_())