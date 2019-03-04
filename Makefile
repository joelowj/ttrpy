init:
	pip install pipenv
	pipenv install --dev
test:
	pipenv run pytest
coverage:
	pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=ttrpy tests
