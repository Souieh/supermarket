.PHONY: install run test build clean

install:
	pip install -r requirements.txt

run:
	python3 main.py

test:
	python3 test_logic.py

build:
	pyinstaller --onefile --windowed --add-data "src:src" main.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -f *.spec
	find . -type d -name "__pycache__" -exec rm -rf {} +
