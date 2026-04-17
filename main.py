import sys
from PyQt6.QtWidgets import QApplication
from src.modules.database import Database
from src.ui.config_dialog import ConfigDialog
from src.ui.launcher_window import LauncherWindow
from src.ui.admin_window import AdminWindow
from src.ui.cashier_window import CashierWindow

class SupermarketApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.launcher = None
        self.admin_win = None
        self.cashier_win = None

    def start(self):
        self.show_launcher()
        sys.exit(self.app.exec())

    def show_launcher(self):
        self.launcher = LauncherWindow()
        # Connect internal buttons of cards
        self.launcher.adminCard.btn.clicked.connect(self.open_admin)
        self.launcher.cashierCard.btn.clicked.connect(self.open_cashier)
        self.launcher.settingsCard.btn.clicked.connect(self.open_settings)
        self.launcher.show()

    def open_admin(self):
        db = Database()
        success, _ = db.connect()
        if not success:
            self.open_settings()
            return
        self.admin_win = AdminWindow()
        self.admin_win.show()
        self.launcher.hide()

    def open_cashier(self):
        db = Database()
        success, _ = db.connect()
        if not success:
            self.open_settings()
            return
        self.cashier_win = CashierWindow()
        self.cashier_win.show()
        self.launcher.hide()

    def open_settings(self):
        dialog = ConfigDialog()
        if dialog.exec():
            host, port, db_name = dialog.get_config()
            Database().save_config(host, port, db_name)
            if self.launcher:
                self.launcher.check_connection()

def main():
    app = SupermarketApp()
    app.start()

if __name__ == "__main__":
    main()
