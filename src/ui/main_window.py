from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import (FluentWindow, NavigationItemPosition,
                             FluentIcon as FIF, SubtitleLabel, setFont)

from .product_page import ProductPage
from .sales_page import SalesPage
from .dashboard_page import DashboardPage

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket Management System - نظام إدارة السوبر ماركت")
        self.resize(1100, 700)

        # Create pages
        self.dashboardPage = DashboardPage(self)
        self.productPage = ProductPage(self)
        self.salesPage = SalesPage(self)

        self.init_navigation()

    def init_navigation(self):
        self.addSubInterface(self.dashboardPage, FIF.HOME, "لوحة التحكم (Dashboard)")
        self.addSubInterface(self.productPage, FIF.APPLICATION, "المنتجات (Products)")
        self.addSubInterface(self.salesPage, FIF.SHOPPING_CART, "المبيعات (Sales)")

        self.navigationInterface.setExpandWidth(280)
        self.navigationInterface.setMinimumExpandWidth(0)
