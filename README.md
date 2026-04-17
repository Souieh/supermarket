# Supermarket Management System (نظام إدارة السوبر ماركت)

A modern desktop application for supermarket management built with Python, PyQt6, and MongoDB.

## Features

- **Modern Fluent UI**: Clean and intuitive design using `PyQt6-Fluent-Widgets`.
- **Product Management**: Full CRUD (Create, Read, Update, Delete) for products.
- **Sales Processing**: Cart-based checkout with real-time stock validation and automatic inventory updates.
- **Dashboard**: Visual statistics including total products, out-of-stock alerts, daily revenue, and total sales.
- **Bilingual Interface**: Supports both Arabic and English.
- **Receipt Generation**: Automatic generation of `.txt` receipts in the `receipts/` directory.
- **Database Configuration**: Configure MongoDB connection (Host, Port, DB Name) at first launch.
- **Transaction Support**: Safe database write operations using MongoDB transactions.

## Prerequisites

- Python 3.10+
- MongoDB (Running locally or accessible via network)

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
```bash
python main.py
```

### Building the Executable
To package the application into a single executable:
```bash
pyinstaller --onefile --windowed --add-data "src:src" main.py
```

## Project Structure
- `src/modules/`: Core business logic (Product, Sale, Receipt, Database).
- `src/ui/`: UI components and pages built with PyQt6.
- `receipts/`: Directory where generated receipts are saved.
- `main.py`: Entry point of the application.

## Testing
Run the logic tests to verify core functionality:
```bash
python test_logic.py
```
