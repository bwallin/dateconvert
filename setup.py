from setuptools import setup, find_packages


setuptools_kwargs = {
    'install_requires': [
        'click>=3.3,<4'
    ],
    'setup_requires': [
        'wheel>=0.24.0,<1'
    ],
    'entry_points': {
        'console_scripts': [
            'day_of_year = dateconvert.day_of_year:main'
        ]
    }
}

setup(
    name='dateconvert',
    description='A collection of date convertion CLI tools.',
    author='Kyle W Purdon',
    author_email='kylepurdon@gmail.com',
    url='https://github.com/kpurdon/dateconvert',
    version='0.0.1',
    packages=find_packages(),
    **setuptools_kwargs
)
