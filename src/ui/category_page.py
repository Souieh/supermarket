from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidgetItem, QHeaderView)
from qfluentwidgets import (SubtitleLabel, TableWidget, LineEdit, PushButton,
                            FluentIcon as FIF, InfoBar)
from ..modules.category import Category


class CategoryPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CategoryPage")
        self.layout = QVBoxLayout(self)

        self.titleLabel = SubtitleLabel("إدارة الفئات", self)

        self.actionBar = QHBoxLayout()
        self.nameEdit = LineEdit(self)
        self.nameEdit.setPlaceholderText("اسم الفئة")
        self.addButton = PushButton(FIF.ADD, "إضافة", self)
        self.addButton.clicked.connect(self.add_category)

        self.actionBar.addWidget(self.nameEdit)
        self.actionBar.addWidget(self.addButton)

        self.table = TableWidget(self)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["الفئة"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.deleteButton = PushButton(FIF.DELETE, "حذف الفئة المختارة", self)
        self.deleteButton.clicked.connect(self.delete_category)

        self.layout.addWidget(self.titleLabel)
        self.layout.addLayout(self.actionBar)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.deleteButton)

        self.load_categories()

    def load_categories(self):
        categories = Category.get_all_categories()
        self.table.setRowCount(0)
        for cat in categories:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(cat["name"]))

    def add_category(self):
        name = self.nameEdit.text()
        if not name:
            return
        if Category.add_category(name):
            self.load_categories()
            self.nameEdit.clear()
            InfoBar.success("تم", "تمت إضافة الفئة", parent=self)
        else:
            InfoBar.error("خطأ", "الفئة موجودة مسبقاً", parent=self)

    def delete_category(self):
        row = self.table.currentRow()
        if row < 0:
            return
        name = self.table.item(row, 0).text()
        if Category.delete_category(name):
            self.load_categories()
            InfoBar.success("تم", "تم حذف الفئة", parent=self)
