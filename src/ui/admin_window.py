from PyQt6.QtCore import Qt, QSize
from qfluentwidgets import (FluentWindow, NavigationItemPosition,
                             FluentIcon as FIF)

from .product_page import ProductPage
from .sales_page import SalesPage
from .dashboard_page import DashboardPage
from .category_page import CategoryPage

class AdminWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Panel - لوحة الإدارة")
        self.resize(1100, 750)

        # Create pages
        self.dashboardPage = DashboardPage(self)
        self.categoryPage = CategoryPage(self)
        self.productPage = ProductPage(self)
        self.salesPage = SalesPage(self)

        self.init_navigation()

    def init_navigation(self):
        self.addSubInterface(self.dashboardPage, FIF.HOME, "لوحة التحكم (Dashboard)")
        self.addSubInterface(self.categoryPage, FIF.MENU, "الفئات (Categories)")
        self.addSubInterface(self.productPage, FIF.APPLICATION, "المنتجات (Products)")
        self.addSubInterface(self.salesPage, FIF.SHOPPING_CART, "المبيعات (Sales)")

        self.navigationInterface.setExpandWidth(280)
        self.navigationInterface.setMinimumExpandWidth(0)
