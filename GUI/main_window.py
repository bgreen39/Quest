import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Quest Game")
        self.setFixedSize(400, 400)  # Set fixed size of the window

        # Create layout
        layout = QVBoxLayout()

        # Display Logo Image
        self.logo = QLabel(self)
        pixmap = QPixmap('/Users/briannagreen/Downloads/Quest.png')  # Update with the path to your logo
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignCenter)  # Center the logo
        layout.addWidget(self.logo)

        # Create buttons
        self.avatar_button = QPushButton("Make Avatar", self)
        self.avatar_button.clicked.connect(self.make_avatar)  # Connect to a method for avatar creation
        layout.addWidget(self.avatar_button)

        self.journey_button = QPushButton("Start Journey", self)
        self.journey_button.clicked.connect(self.start_journey)  # Connect to a method to start the journey
        layout.addWidget(self.journey_button)

        # Set the layout
        self.setLayout(layout)

    def make_avatar(self):
        print("Making Avatar...")  # This will trigger when the "Make Avatar" button is clicked
        # You can add code to go to another screen or window to create the avatar

    def start_journey(self):
        print("Starting Journey...")  # This will trigger when the "Start Journey" button is clicked
        # You can add code to begin the journey, show the guide, etc.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec_())
