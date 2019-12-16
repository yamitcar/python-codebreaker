# csdpy
Template for Certified Scrum Developer course with Python

# Install
## Install in a Debian/Ubuntu

Puede usarse como base el csd-box https://github.com/kleer-la/virtual-machines

    sudo apt-get update
    sudo apt-get install python-virtualenv
    sudo apt-get install libxml2-dev libxslt-dev python3-dev

    virtualenv -p python3 p3
    source p3/bin/activate

## Install in Mac

Crear ambientes virtuales:

	python3 -m venv ~/.virtualenvs/<name>

Activar ambientes virtuales:

	source ~/.virtualenvs/<name>/bin/activate

## util

save dependencies

    pip freeze > requirements.txt

remove dependencies

    pip uninstall -r requirements.txt -y

close virtual env

    deactivate

## App template

    git clone http://github.com/yamitcar/csdpy
    cd csdpy
    pip install -r requirements.txt

## Optional
- Tab-complete for python http://blog.e-shell.org/221

# Test
- behave
- mamba test/* --format=documentation

# Run
- python app.py
- browse to localhost:5000
