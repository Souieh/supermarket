from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout
from qfluentwidgets import CardWidget, StrongBodyLabel, TitleLabel
from .touch_button import TouchButton


class TotalsCard(CardWidget):
    def __init__(self, mono_font, parent=None):
        super().__init__(parent)
        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.subtotal_label = StrongBodyLabel("المجموع الفرعي    0.00")
        self.discount_label = StrongBodyLabel("الخصم    - 0.00")
        self.tax_label = StrongBodyLabel("الضريبة    0.00")
        self.service_label = StrongBodyLabel("رسوم الخدمة    0.00")
        self.total_label = TitleLabel("المجموع الكلي    0.00")
        self.balance_label = StrongBodyLabel("الرصيد    $0.00")

        labels = [
            self.subtotal_label,
            self.discount_label,
            self.tax_label,
            self.service_label,
            self.total_label,
            self.balance_label,
        ]
        for i, lbl in enumerate(labels):
            lbl.setFont(mono_font)
            lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
            layout.addWidget(lbl, i, 0)

    def update_totals(self, totals):
        self.subtotal_label.setText(f"المجموع الفرعي    {totals['subtotal']:10.2f}")
        self.discount_label.setText(f"الخصم    - {totals['discount']:8.2f}")
        self.tax_label.setText(f"الضريبة    {totals['tax']:13.2f}")
        self.service_label.setText(f"رسوم الخدمة    {totals['service']:10.2f}")
        self.total_label.setText(f"المجموع الكلي    {totals['total']:10.2f}")
        self.balance_label.setText(f"الرصيد    ${totals['balance']:10.2f}")


class ActionsCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainLayout = QGridLayout(self)
        self.mainLayout.setSpacing(10)

    def add_action(self, text, slot, row, col):
        btn = TouchButton(text)
        btn.clicked.connect(slot)
        self.mainLayout.addWidget(btn, row, col)


class PaymentCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(10)

    def add_payment_method(self, text, slot):
        btn = TouchButton(text)
        btn.setFixedHeight(70)
        btn.clicked.connect(slot)
        self.mainLayout.addWidget(btn)
