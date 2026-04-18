from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont
from qfluentwidgets import PushButton, setFont


class TouchButton(PushButton):
    """Fluent-styled touch button with fixed height."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedHeight(80)
        self.setIconSize(QSize(32, 32))
        setFont(self, 18, weight=QFont.Weight.Bold)
