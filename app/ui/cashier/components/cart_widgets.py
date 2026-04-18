from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem
from qfluentwidgets import TableWidget, setFont


class CartTable(TableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["Name", "Price", "Quantity", "Discount", "Total"])
        header = self.horizontalHeader()
        if header:
            header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        setFont(self, 16)
        vheader = self.verticalHeader()
        if vheader:
            vheader.setDefaultSectionSize(60)
        hheader = self.horizontalHeader()
        if hheader:
            hheader.setFixedHeight(50)

    def update_cart(self, cart_items):
        self.setRowCount(0)
        for item in cart_items:
            row = self.rowCount()
            self.insertRow(row)
            qty = item["quantity"]
            price = item["price"]
            discount = item.get("discount", 0)
            total = (price * qty) - discount

            self.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.setItem(row, 1, QTableWidgetItem(f"{price:.2f}"))
            self.setItem(row, 2, QTableWidgetItem(str(qty)))
            self.setItem(row, 3, QTableWidgetItem(f"{discount:.2f}"))
            self.setItem(row, 4, QTableWidgetItem(f"{total:.2f}"))
