import sys
import webbrowser
from PyQt5.QtGui import QMovie, QFont, QCursor
from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Witch Assistant")
        self.setFixedSize(480, 400)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) # set flag
        self.movie_a = QMovie("data/animated_a.gif")
        self.movie_b = QMovie("data/animated_b.gif")
        self.background_label = QLabel()
        self.background_label.setMovie(self.movie_a)
        self.movie_a.start()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.background_label)
        self.setStyleSheet("background-color: black;")
        
        self.player = QMediaPlayer(self)
        self.player.setVolume(20)
        
        self.setCursor(Qt.PointingHandCursor) # set cursor shape to pointing hand

        

        # Add a push button underneath the GIF
        self.button = QPushButton("Open ChatGPT")
        self.button.setStyleSheet("color: white;")
        self.button.setFont(QFont("Balgruf", 12))
        self.button.setToolTip("<font color='black'>Hey, handsome. What do you want to talk?</font>")  # set the tooltip
        self.layout.addWidget(self.button)
        
        # Add another push button underneath the GIF
        self.button_3= QPushButton("Open GitHub")
        self.button_3.setStyleSheet("color: white;")
        self.button_3.setFont(QFont("Balgruf", 12))
        self.button_3.setToolTip("<font color='black'>Do you want to learn the principle of the world?</font>")  # set the tooltip
        self.layout.addWidget(self.button_3)
        
        # Add a second push button underneath the first button
        self.button_2 = QPushButton("About Calendar..")
        self.button_2.setStyleSheet("color: white;")
        self.button_2.setFont(QFont("Balgruf", 12))
        self.button_2.setToolTip("<font color='black'>Do you want to talk about our future?</font>")
        self.layout.addWidget(self.button_2)
        
       
        table_layout = QGridLayout()
        
        table_layout.setContentsMargins(0, 0, 0, 0)
        table_layout.setSpacing(0)
        table_widget = QWidget()
        table_widget.setLayout(table_layout)
        table_widget.setStyleSheet("background-color: #405FC8;")
        self.layout.addWidget(table_widget)

        
        # Add a clock label to the table layout
        self.clock_label = QLabel()
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFont(QFont('Balgruf', 24))
        self.clock_label.setStyleSheet("color: pink; font-size: 24px;")
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont("Balgruf", 14))
        table_layout.addWidget(self.clock_label, 0, 0)

        # Set up a timer to update the clock label every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Set the central widget of the main window


        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Connect the button to a function that opens a website
        self.button.clicked.connect(self.open_website)
        
         # Connect the button to a function that opens a website2
        self.button_3.clicked.connect(self.open_gitHub)
        
        # Connect the second button to a function
        self.button_2.clicked.connect(self.show_current_time)
        
    def play_sound(self):
        file_path = "data/my_sound.wav"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        self.player.setVolume(20)
        self.player.play()

    def enterEvent(self, event):
        self.background_label.setMovie(self.movie_b)
        self.movie_b.start()
        QTimer.singleShot(2800, self.play_sound)
        self.setCursor(Qt.PointingHandCursor) # set cursor shape to pointing hand
      
    def leaveEvent(self, event):
        self.background_label.setMovie(self.movie_a)
        self.movie_a.start()
        self.unsetCursor() # set cursor shape to default

    def open_website(self):
        webbrowser.open("https://chat.openai.com/")
        
    def open_gitHub(self):
        webbrowser.open("https://github.com/NerdKing1945/first-team-project")

    def show_current_time(self):
        # Display the current time in a message box
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        QMessageBox.information(self, "Check your Schedule!!", f"The current time is {current_time}.")
        webbrowser.open("https://calendar.google.com/calendar/u/0/r?pli=1")
    
    def update_time(self):
        # Update the clock label with the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.setText(current_time)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())








