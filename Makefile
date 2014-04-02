VIRTUALENV?=virtualenv

init:
	echo "ddddddddd"

runtest:
	set -e
	flake8 src/
	flake8 test/

	nosetests test/ --with-coverage --cover-package happywork2 -s
