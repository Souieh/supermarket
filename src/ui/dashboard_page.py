from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from qfluentwidgets import SubtitleLabel, CardWidget, BodyLabel, StrongBodyLabel, FluentIcon as FIF
from ..modules.sale import Sale

class StatCard(CardWidget):
    def __init__(self, title, value, icon, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.titleLabel = BodyLabel(title, self)
        self.valueLabel = StrongBodyLabel(value, self)
        self.valueLabel.setStyleSheet("font-size: 24px; color: #0078d4;")

        self.layout.addWidget(self.titleLabel)
        self.layout.addWidget(self.valueLabel)

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("DashboardPage")
        self.layout = QVBoxLayout(self)

        self.titleLabel = SubtitleLabel("لوحة التحكم / Dashboard", self)
        self.layout.addWidget(self.titleLabel)

        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)

        self.refresh_stats()

    def refresh_stats(self):
        try:
            stats = Sale.get_dashboard_stats()
        except:
            stats = {"total_products": 0, "out_of_stock": 0, "daily_revenue": 0, "total_sales": 0}

        # Clear grid
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        self.grid.addWidget(StatCard("إجمالي المنتجات / Total Products", str(stats["total_products"]), FIF.APPLICATION), 0, 0)
        self.grid.addWidget(StatCard("نفاذ المخزون / Out of Stock", str(stats["out_of_stock"]), FIF.CLOSE), 0, 1)
        self.grid.addWidget(StatCard("إيرادات اليوم / Daily Revenue", f"{stats['daily_revenue']:.2f}", FIF.MONEY), 1, 0)
        self.grid.addWidget(StatCard("إجمالي المبيعات / Total Sales", str(stats["total_sales"]), FIF.SHOPPING_CART), 1, 1)

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_stats()
