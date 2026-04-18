from PyQt6.QtWidgets import QHBoxLayout, QWidget
from qfluentwidgets import FluentIcon, PushButton, setFont


class CashierNavbar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.btn_admin = PushButton("Admin")
        self.btn_admin.setIcon(FluentIcon.SETTING)

        self.btn_hold = PushButton("Hold")
        self.btn_hold.setIcon(FluentIcon.PAUSE)

        self.btn_logout = PushButton("Logout")
        self.btn_logout.setIcon(FluentIcon.POWER_BUTTON)

        for btn in (self.btn_admin, self.btn_hold, self.btn_logout):
            btn.setFixedSize(100, 50)
            setFont(btn, 16)
            self.mainLayout.addWidget(btn)

        self.mainLayout.addStretch()
