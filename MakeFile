# virtualenv creation
env/bin/activate: requirements.txt
	python3 -m venv env
	./env/bin/pip install -r requirements.txt

# setup project for development
setup: env/bin/activate
	@echo -e "\u001b[32mvirtual envirnment setup for developement\u001b[0m" # &green<text>&reset

# build sphinx html docs
sphinx-build: env/bin/activate
	./env/bin/sphinx-build -b html sphinx_docs/source/ sphinx_docs/build/html

# clean sphinx build files
sphinx-clean: env/bin/activate
	rm -rf sphinx_docs/build

# remove pycache and envirnment
clean:
	rm -rf __pycache__
	rm -rf env
	rm -rf sphinx_docs/build
