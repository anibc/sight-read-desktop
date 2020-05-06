run:
	black --check .
	python3 main.py

clean:
	find . -name *.pyc -delete
	find . -name __pycache__ -delete
