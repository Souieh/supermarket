VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: venv install run test build clean

venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py

test:
	$(PYTHON) test_logic.py

build:
	$(PYTHON) -m PyInstaller --onefile --windowed --add-data "src:src" main.py

clean:
	rm -rf $(VENV)
	rm -rf build/
	rm -rf dist/
	rm -f *.spec
	find . -type d -name "__pycache__" -exec rm -rf {} +
