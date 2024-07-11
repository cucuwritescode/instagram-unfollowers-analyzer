import sys
import json
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class AnalyzerThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, followers_data, following_data):
        super().__init__()
        self.followers_data = followers_data
        self.following_data = following_data

    def run(self):
        following_data = self.following_data.get('relationships_following', [])

        followers = set()
        for entry in self.followers_data:
            if isinstance(entry, dict):
                for item in entry.get('string_list_data', []):
                    followers.add(item['value'])

        self.progress.emit(50)

        following = set()
        for entry in following_data:
            if isinstance(entry, dict):
                for item in entry.get('string_list_data', []):
                    following.add(item['value'])

        not_following_back = sorted(list(following - followers))

        self.progress.emit(100)
        self.result = not_following_back

class UnfollowersAnalyzer(QWidget):
    def __init__(self):
        super().__init__()

        pygame.mixer.init()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Instagram Unfollowers Analyzer')
        self.setGeometry(100, 100, 500, 550)

        layout = QVBoxLayout()

        self.followers_button = QPushButton('Load Followers JSON', self)
        self.followers_button.clicked.connect(self.load_followers)
        self.followers_button.setIcon(QIcon('icons/followers.png'))
        layout.addWidget(self.followers_button)

        self.following_button = QPushButton('Load Following JSON', self)
        self.following_button.clicked.connect(self.load_following)
        self.following_button.setIcon(QIcon('icons/following.png'))
        layout.addWidget(self.following_button)

        self.analyze_button = QPushButton('Analyze', self)
        self.analyze_button.clicked.connect(self.analyze)
        self.analyze_button.setIcon(QIcon('icons/analyze.png'))
        layout.addWidget(self.analyze_button)
        self.analyze_button.setEnabled(False)

        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        self.result_label = QLabel('Users not following back:', self)
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        
        self.followers_data = None
        self.following_data = None

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #f2f2f2;
            }
            QPushButton {
                background-color: #1c1c1c;
                color: #f2f2f2;
                border: 1px solid #5c5c5c;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:disabled {
                background-color: #3c3c3c;
                border: 1px solid #7c7c7c;
            }
            QPushButton:hover {
                background-color: #3c3c3c;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
            QTextEdit {
                background-color: #1c1c1c;
                color: #f2f2f2;
                border: 1px solid #5c5c5c;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QProgressBar {
                background-color: #3c3c3c;
                border: 1px solid #5c5c5c;
                border-radius: 5px;
                text-align: center;
                font-size: 14px;
                color: #f2f2f2;
            }
            QProgressBar::chunk {
                background-color: #6b6b6b;
            }
        """)

    def load_followers(self):
        try:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Load Followers JSON", "", "JSON Files (*.json);;All Files (*)", options=options)
            if file_name:
                with open(file_name, 'r') as file:
                    self.followers_data = json.load(file)
                self.play_sound('level-up-191997.wav')
                print("Followers data loaded successfully")
                self.check_ready()
        except Exception as e:
            print(f"Error loading followers: {e}")

    def load_following(self):
        try:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Load Following JSON", "", "JSON Files (*.json);;All Files (*)", options=options)
            if file_name:
                with open(file_name, 'r') as file:
                    self.following_data = json.load(file)
                self.play_sound('level-up-191997.wav')
                print("Following data loaded successfully")
                self.check_ready()
        except Exception as e:
            print(f"Error loading following: {e}")

    def check_ready(self):
        if self.followers_data is not None and self.following_data is not None:
            self.analyze_button.setEnabled(True)

    def analyze(self):
        self.progress_bar.setValue(0)
        self.analyze_button.setEnabled(False)
        
        self.analyzer_thread = AnalyzerThread(self.followers_data, self.following_data)
        self.analyzer_thread.progress.connect(self.update_progress)
        self.analyzer_thread.finished.connect(self.display_result)
        self.analyzer_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def display_result(self):
        not_following_back = self.analyzer_thread.result
        self.result_text.clear()
        self.result_text.append("\n".join(not_following_back))
        self.play_rick_astley()
        self.analyze_button.setEnabled(True)

    def play_sound(self, sound_file):
        try:
            print(f"Playing sound from: {sound_file}")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

    def play_rick_astley(self):
        try:
            print("Playing Rick Astley song")
            pygame.mixer.music.load('Rick Astley - Never Gonna Give You Up (Official Music Video).wav')
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error playing Rick Astley song: {e}")

    def closeEvent(self, event):
        self.play_sound('simple-notification-152054.wav')
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UnfollowersAnalyzer()
    ex.show()
    sys.exit(app.exec_())