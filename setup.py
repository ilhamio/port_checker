from setuptools import setup, find_packages

setup(
    name='application',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'nslookup',
        'pydantic',
        'pythonping',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'checker = application.presentation.cli.start:cli',
        ],
    },
)
