from fabric.api import local, task


BANNER = """
 ____    _  _____ _____ ____ ___  _   ___     _______ ____ _____
|  _ \  / \|_   _| ____/ ___/ _ \| \ | \ \   / / ____|  _ \_   _|
| | | |/ _ \ | | |  _|| |  | | | |  \| |\ \ / /|  _| | |_) || |
| |_| / ___ \| | | |__| |__| |_| | |\  | \ V / | |___|  _ < | |
|____/_/   \_\_| |_____\____\___/|_| \_|  \_/  |_____|_| \_\|_|

"""


@task
def setup_env():
    local('mkdir -p ~/.virtual_envs')
    local('virtualenv ~/.virtual_envs/dateconvert_dev')
    local('. ~/.virtual_envs/dateconvert_dev/bin/activate && \
    pip install -r requirements.txt')


@task
def flake8():
    local('flake8 --config .flake8rc *.py **/*.py --verbose')


@task
def unit_test():
    local('nosetests --verbose')


@task
def test():
    print(BANNER)
    flake8()
    unit_test()


@task
def bump_patch():
    local('bumpversion patch')


@task
def bump_minor():
    local('bumpversion minor')


@task
def bump_major():
    local('bumpversion major')


@task
def pypi_register():
    local('python setup.py register')


@task
def pypi_upload():
    local('python setup.py bdist_wheel upload')
