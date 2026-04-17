from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout
from qfluentwidgets import (MessageBoxBase, SubtitleLabel, LineEdit,
                             PushButton, FluentIcon as FIF)
from ..modules.database import Database

class ConfigDialog(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel("إعدادات قاعدة البيانات / Database Settings", self)
        self.hostLineEdit = LineEdit(self)
        self.portLineEdit = LineEdit(self)
        self.dbLineEdit = LineEdit(self)

        self.hostLineEdit.setPlaceholderText("المضيف / Host (e.g. localhost)")
        self.portLineEdit.setPlaceholderText("المنفذ / Port (e.g. 27017)")
        self.dbLineEdit.setPlaceholderText("اسم قاعدة البيانات / Database Name")

        # Load existing config if any
        db = Database()
        if db.config:
            self.hostLineEdit.setText(db.config.get("host", "localhost"))
            self.portLineEdit.setText(str(db.config.get("port", 27017)))
            self.dbLineEdit.setText(db.config.get("db_name", "supermarket"))
        else:
            self.hostLineEdit.setText("localhost")
            self.portLineEdit.setText("27017")
            self.dbLineEdit.setText("supermarket")

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.hostLineEdit)
        self.viewLayout.addWidget(self.portLineEdit)
        self.viewLayout.addWidget(self.dbLineEdit)

        self.yesButton.setText("حفظ واتصال / Save & Connect")
        self.cancelButton.setText("إلغاء / Cancel")

        self.widget.setMinimumWidth(350)

    def validate(self):
        return (self.hostLineEdit.text() and
                self.portLineEdit.text().isdigit() and
                self.dbLineEdit.text())

    def get_config(self):
        return (self.hostLineEdit.text(),
                self.portLineEdit.text(),
                self.dbLineEdit.text())
