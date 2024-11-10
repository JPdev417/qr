import sys
import qrcode
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Creador de Códigos QR")
        self.setGeometry(100, 100, 400, 200)
        self.setFixedSize(400, 200)


        # URL Input
        self.url_label = QLabel("URL al archivo/web:", self)
        self.url_label.move(20, 20)
        self.url_input = QLineEdit(self)
        self.url_input.setGeometry(150, 20, 220, 25)

        # Save Path
        self.path_label = QLabel("Exportar a:", self)
        self.path_label.move(20, 60)
        self.path_input = QLineEdit(self)
        self.path_input.setGeometry(150, 60, 160, 25)
        self.path_input.setText(os.path.expanduser("~/Desktop"))  # Default to Desktop
        self.browse_button = QPushButton("Buscar", self)
        self.browse_button.setGeometry(320, 60, 60, 25)
        self.browse_button.clicked.connect(self.select_path)

        # Generate Button
        self.generate_button = QPushButton("Generar", self)
        self.generate_button.setGeometry(150, 100, 130, 40)
        self.generate_button.clicked.connect(self.generate_qr_code)

    def select_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Save Folder", os.path.expanduser("~/Desktop"))
        if folder:
            self.path_input.setText(folder)

    def generate_qr_code(self):
        data = self.url_input.text()
        save_path = self.path_input.text()

        if not data:
            QMessageBox.warning(self, "Input Error", "Please enter URL or text to encode.")
            return

        if not save_path:
            QMessageBox.warning(self, "Path Error", "Please select a save path.")
            return

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Define file path and save the image
        file_path = os.path.join(save_path, "qr_code.png")
        img.save(file_path)

        # Show success message
        QMessageBox.information(self, "Success", f"QR guardado a: {file_path}")

        # Automatically open the QR code image
        if sys.platform == "darwin":  # macOS
            os.system(f"open '{file_path}'")
        elif sys.platform == "win32":  # Windows
            os.startfile(file_path)
        elif sys.platform == "linux":  # Linux
            os.system(f"xdg-open '{file_path}'")

# Set up the application
app = QApplication(sys.argv)
window = QRCodeGenerator()
window.show()
sys.exit(app.exec_())
