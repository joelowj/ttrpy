init:
	pip install pipenv
	pipenv install --dev
test:
	pipenv run py.test
coverage:
	pipenv run py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=ttrpy tests
