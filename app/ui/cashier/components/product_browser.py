from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import (
    InfoBar,
    LineEdit,
    PushButton,
    ScrollArea,
    SearchLineEdit,
    StrongBodyLabel,
    setFont,
)

from ....modules.category import Category
from ....modules.product import Product
from .touch_button import TouchButton


class ProductBrowser(QWidget):
    product_selected = pyqtSignal(dict)  # emits product dict

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_categories()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Search + code row
        search_add_layout = QHBoxLayout()
        self.search_edit = SearchLineEdit()
        self.search_edit.setPlaceholderText("Search products...")
        self.search_edit.setFixedHeight(50)
        setFont(self.search_edit, 20)
        self.search_edit.textChanged.connect(self.load_categories)

        self.code_edit = LineEdit()
        self.code_edit.setPlaceholderText("Product code")
        self.code_edit.setFixedHeight(50)
        setFont(self.code_edit, 20)
        self.code_edit.returnPressed.connect(self.add_by_code)

        btn_add_code = PushButton("Add by code")
        btn_add_code.setFixedHeight(50)
        btn_add_code.clicked.connect(self.add_by_code)

        search_add_layout.addWidget(self.search_edit, 3)
        search_add_layout.addWidget(self.code_edit, 2)
        search_add_layout.addWidget(btn_add_code, 1)
        layout.addLayout(search_add_layout)

        # Scroll area for products
        self.scroll = ScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.product_layout = QVBoxLayout(self.container)
        self.product_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.container)
        layout.addWidget(self.scroll)

    def load_categories(self):
        # Clear existing widgets
        while self.product_layout.count():
            item = self.product_layout.takeAt(0)
            if item is None:
                continue
            widget = item.widget()
            if widget:
                widget.deleteLater()

        search_query = self.search_edit.text()
        categories = Category.get_all_categories()

        for cat in categories:
            cat_name = cat["name"]
            header = StrongBodyLabel(cat_name)
            header.setStyleSheet("margin-top: 10px;")
            setFont(header, 16, weight=QFont.Weight.Bold)
            self.product_layout.addWidget(header)

            products = Product.get_all_products(
                search_query=search_query, category=cat_name
            )
            for prod in products:
                btn = TouchButton(f"{prod['name']} {prod['price']:.2f}")
                btn.setStyleSheet("text-align: left; padding-left: 15px;")
                btn.clicked.connect(lambda ch, p=prod: self.product_selected.emit(p))
                self.product_layout.addWidget(btn)

        self.load_forgot_foods()

    def load_forgot_foods(self):
        header = StrongBodyLabel("FOODS FORGOT")
        header.setStyleSheet(
            "border-bottom: 1px solid black; margin-top: 20px;"
        )
        self.product_layout.addWidget(header)

        forgot_foods = [
            {"name": "Lobster Forgot", "price": 50.00},
            {"name": "Cucumber", "price": 50.00},
            {"name": "Pumpkin", "price": 50.00},
        ]
        for f in forgot_foods:
            btn = TouchButton(f"{f['name']} {f['price']:.2f} - 12g")
            btn.setStyleSheet("text-align: left; padding-left: 15px;")
            btn.clicked.connect(
                lambda ch, prod=f: self.product_selected.emit(
                    {"code": "FORGOT", "name": prod["name"], "price": prod["price"]}
                )
            )
            self.product_layout.addWidget(btn)

    def add_by_code(self):
        code = self.code_edit.text().strip()
        if not code:
            return
        product = Product.get_product(code)

        if product:
            self.product_selected.emit(product)
            self.code_edit.clear()
        else:
            InfoBar.error("Error", "Product not found", parent=self)
            return
