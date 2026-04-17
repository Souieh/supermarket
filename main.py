import sys
from PyQt6.QtWidgets import QApplication
from src.modules.database import Database
from src.ui.config_dialog import ConfigDialog
from src.ui.main_window import MainWindow
from qfluentwidgets import InfoBar, InfoBarPosition

def main():
    app = QApplication(sys.argv)
    db = Database()

    def start_app():
        success, message = db.connect()
        if success:
            window = MainWindow()
            window.show()
            return window
        else:
            show_config(message)
            return None

    def show_config(error_message=None):
        dialog = ConfigDialog()
        if error_message:
            # Note: InfoBar needs a parent, but dialog is not yet shown.
            # We'll just print or use a simpler message if needed.
            print(f"Connection Error: {error_message}")

        if dialog.exec():
            host, port, db_name = dialog.get_config()
            db.save_config(host, port, db_name)
            win = start_app()
            if win:
                # Keep reference
                global main_win
                main_win = win

    main_win = start_app()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
