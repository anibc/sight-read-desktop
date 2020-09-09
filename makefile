P3=../venv/qsightread/bin/python3

run:
	$(P3) main.py

check_black:
	$(P3) -m black --check .

black:
	$(P3) -m black .

clean:
	find . -name *.pyc -delete
	find . -name __pycache__ -delete

clear: clean
	echo > logs/app.log
	clear
