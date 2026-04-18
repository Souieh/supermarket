import os
import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import InfoBar

from ...modules.receipt import Receipt
from ...modules.sale import Sale
from .components.cart_widgets import CartTable
from .components.navbar import CashierNavbar
from .components.product_browser import ProductBrowser
from .components.sidebar import ActionsCard, PaymentCard, TotalsCard
from .components.cart_model import CartModel


class CashierWindow(QWidget):
    switchToAdmin = pyqtSignal()
    returnToLauncher = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("واجهة الصَرّاف")
        self.showMaximized()
        mono_font = QFont("Monospace")
        mono_font.setStyleHint(QFont.StyleHint.Monospace)
        self.setFont(mono_font)

        # Model
        self.cart_model = CartModel()

        # UI
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Navbar
        self.navbar = CashierNavbar(self)
        self.navbar.btn_admin.clicked.connect(self.switchToAdmin.emit)
        self.navbar.btn_hold.clicked.connect(self.returnToLauncher.emit)
        self.navbar.btn_logout.clicked.connect(self.returnToLauncher.emit)
        main_layout.addWidget(self.navbar)

        # Split area
        split_layout = QHBoxLayout()
        main_layout.addLayout(split_layout, 1)

        # Left: product browser + cart table
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setSpacing(15)

        self.product_browser = ProductBrowser(self)
        self.product_browser.product_selected.connect(self.cart_model.add_item)
        left_layout.addWidget(self.product_browser, 2)

        self.cart_table = CartTable(self)
        left_layout.addWidget(self.cart_table, 3)
        split_layout.addWidget(left_widget, 3)

        # Right: sidebar with totals, actions, payment
        right_layout = QVBoxLayout()
        right_layout.setSpacing(20)

        self.totals_card = TotalsCard(mono_font, self)
        right_layout.addWidget(self.totals_card)

        self.actions_card = ActionsCard(self)
        # Define actions with slots
        actions = [
            ("حذف عنصر", self.clear_cart),
            ("خصم", self.apply_discount),
            ("داخلي", self.toggle_inhouse),
            ("تعليق", self.returnToLauncher.emit),
            ("إعدادات", self.switchToAdmin.emit),
        ]
        for i, (text, slot) in enumerate(actions):
            self.actions_card.add_action(text, slot, i // 2, i % 2)
        right_layout.addWidget(self.actions_card)

        self.payment_card = PaymentCard(self)
        payments = [
            ("نقداً", self.checkout),
            ("بطاقة", self.card_payment),
            ("قسيمة", self.gift_payment),
            ("ولاء", self.loyalty_payment),
        ]
        for text, slot in payments:
            self.payment_card.add_payment_method(text, slot)
        right_layout.addWidget(self.payment_card)

        right_layout.addStretch()
        split_layout.addLayout(right_layout, 1)

        # Connect model signals to views
        self.cart_model.cart_changed.connect(self.cart_table.update_cart)
        self.cart_model.totals_changed.connect(self.totals_card.update_totals)

    # ----- Actions that interact with the model -----
    def clear_cart(self):
        self.cart_model.clear()

    def checkout(self):
        if not self.cart_model.items:
            return
        total = sum(item["price"] * item["quantity"] for item in self.cart_model.items)
        sale = Sale(self.cart_model.items, total)
        try:
            receipt_id = sale.process_sale()
            filename = Receipt.generate(sale.to_dict())
            InfoBar.success("تم", f"تم البيع بنجاح. فاتورة: {receipt_id}", parent=self)
            self.cart_model.clear()
            # Open receipt file
            try:
                if sys.platform == "win32":
                    os.startfile(filename)
                elif sys.platform == "darwin":
                    import subprocess

                    subprocess.run(["open", filename])
                else:
                    import subprocess

                    subprocess.run(["xdg-open", filename])
            except Exception:
                pass
        except Exception as e:
            InfoBar.error("خطأ", str(e), parent=self)

    # Placeholders
    def apply_discount(self):
        InfoBar.info("خصم", "وظيفة الخصم قيد التطوير", parent=self)

    def toggle_inhouse(self):
        InfoBar.info("داخلي", "وظيفة رسوم الخدمة قيد التطوير", parent=self)

    def card_payment(self):
        InfoBar.info("بطاقة", "الدفع بالبطاقة قيد التطوير", parent=self)

    def gift_payment(self):
        InfoBar.info("قسيمة", "الدفع بقسيمة هدايا قيد التطوير", parent=self)

    def loyalty_payment(self):
        InfoBar.info("ولاء", "الدفع بنقاط الولاء قيد التطوير", parent=self)
