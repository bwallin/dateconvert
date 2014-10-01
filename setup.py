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
            'day_of_year = day_of_year.day_of_year:main'
        ]
    }
}

setup(
    name='pydate',
    description='Calculates the day of year from a given YYYYMMDD.',
    author='Kyle W Purdon',
    author_email='kylepurdon@gmail.com',
    url='https://github.com/kpurdon/pydate',
    version='0.0.1',
    packages=find_packages(),
    **setuptools_kwargs
)
