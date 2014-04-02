VIRTUALENV?=virtualenv

cleanup:
	find . -name '*.pyc' -delete
	find . -name 'sessions' | xargs rm -rf 

runtest:
	set -e
	flake8 src/
	flake8 test/

	nosetests test/ --with-coverage --cover-package happywork2 -s
