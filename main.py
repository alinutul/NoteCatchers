from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QMenuBar, QFileDialog
from PySide6.QtGui import QKeySequence, QFont
from PySide6.QtCore import Qt
from main_ui import Ui_MainWindow
from datetime import datetime

class NotesCatchers(QMainWindow):
    
    def save_note(self):
        note_content = self.ui.textEdit.toPlainText()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Note", "", self.file_filter)

        if file_path:
            with open(file_path, 'w') as f:
                f.write(note_content)
                self.is_unsaved = False
                self.update_window_title(file_path)

    def open_note(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Note", "", self.file_filter)
        if file_path:
            with open(file_path, 'r') as f:
                note_content = f.read()
                self.ui.textEdit.setPlainText(note_content)
            self.is_unsaved = False
            self.update_window_title(file_path)

    def update_window_title(self, file_path=None):
        if file_path:
            self.setWindowTitle(f"{file_path} - NoteCatchers")
        else:
            self.setWindowTitle("Untitled* - NoteCatchers" if self.is_unsaved else "Untitled - NoteCatchers")

    def new_note(self):
        self.ui.textEdit.setPlainText("")
        self.is_unsaved = True
        self.update_window_title()

    def on_text_changed(self):
        if self.ui.textEdit.toPlainText():
            self.is_unsaved = True
        self.update_window_title()

    def insert_date_time(self):
        cursor = self.ui.textEdit.textCursor()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.insertText(current_time)

    def wheelEvent(self, event):
        # Check if Ctrl key is pressed and user is scrolling
        if event.modifiers() == Qt.ControlModifier:
            delta = event.angleDelta().y()
            current_font = self.ui.textEdit.font()
            font_size = current_font.pointSize()

            # Increase or decrease font size based on scroll direction
            if delta > 0:  # Scroll up -> Increase font size
                new_font_size = font_size + 1
            else:  # Scroll down -> Decrease font size
                new_font_size = font_size - 1

            # Set the new font size
            current_font.setPointSize(new_font_size)
            self.ui.textEdit.setFont(current_font)

        # Call the default event handler to ensure the scroll works
        super().wheelEvent(event)

    def __init__(self):
        self.file_filter = "Text Files (*.txt);;All Files (*)"
        self.is_unsaved = False  # Track if the file is unsaved
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set shortcuts for save, open, and new actions
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionNew.setShortcut("Ctrl+N")
        self.ui.actionUndo.setShortcut("Ctrl+Z")
        self.ui.actionRedo.setShortcut("Ctrl+Y")
        self.ui.actionCopy.setShortcut("Ctrl+C")
        self.ui.actionCut.setShortcut("Ctrl+X")
        self.ui.actionPaste.setShortcut("Ctrl+V")
        self.ui.actionDelete.setShortcut("Del")
        # Connect actions to their corresponding methods
        self.ui.actionSave.triggered.connect(self.save_note)
        self.ui.actionOpen.triggered.connect(self.open_note)
        self.ui.actionNew.triggered.connect(self.new_note)
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionDelete.triggered.connect(lambda: self.ui.textEdit.textCursor().removeSelectedText())
        self.ui.actionDate_Time.triggered.connect(self.insert_date_time)
        # Connect the text area to detect changes
        self.ui.textEdit.textChanged.connect(self.on_text_changed)

        # Set the window size and layout
        self.setWindowTitle("Untitled - NoteCatchers")
        self.setMinimumSize(600, 400)  # Set minimum size to prevent window from being too small

        # Set layout for the main window (if not set in the .ui)
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.ui.textEdit)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        #adaugari: teme, fonturi, "you sure you dont want to save?", organizare cod
if __name__ == "__main__":
    app = QApplication([])
    window = NotesCatchers()
    window.show()
    app.exec()
