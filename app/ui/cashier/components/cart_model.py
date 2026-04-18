from PyQt6.QtCore import QObject, pyqtSignal


class CartModel(QObject):
    cart_changed = pyqtSignal(list)  # emits full cart list
    totals_changed = pyqtSignal(
        dict
    )  # emits subtotal, discount, tax, service, total, balance

    def __init__(self):
        super().__init__()
        self.items = []  # list of dicts: code, name, price, quantity, discount
        self.tax_rate = 0.15
        self.service_fee = 0.0

    def add_item(self, product):
        for item in self.items:
            if item["code"] == product["code"]:
                item["quantity"] += 1
                self._notify()
                return
        self.items.append(
            {
                "code": product["code"],
                "name": product["name"],
                "price": product["price"],
                "quantity": 1,
                "discount": 0.0,
            }
        )
        self._notify()

    def remove_item(self, row):
        if 0 <= row < len(self.items):
            del self.items[row]
            self._notify()

    def clear(self):
        self.items.clear()
        self._notify()

    def update_quantity(self, row, new_qty):
        if 0 <= row < len(self.items) and new_qty > 0:
            self.items[row]["quantity"] = new_qty
            self._notify()

    def update_discount(self, row, discount):
        if 0 <= row < len(self.items):
            self.items[row]["discount"] = discount
            self._notify()

    def _calculate_totals(self):
        subtotal = sum(item["price"] * item["quantity"] for item in self.items)
        discount = sum(item.get("discount", 0) for item in self.items)
        tax = (subtotal - discount) * self.tax_rate
        total = subtotal - discount + tax + self.service_fee
        balance = 500.00  # placeholder; could be linked to customer balance
        return {
            "subtotal": subtotal,
            "discount": discount,
            "tax": tax,
            "service": self.service_fee,
            "total": total,
            "balance": balance,
        }

    def _notify(self):
        self.cart_changed.emit(self.items)
        self.totals_changed.emit(self._calculate_totals())

    def get_items_for_sale(self):
        # Return items in the format expected by Sale module
        return self.items
