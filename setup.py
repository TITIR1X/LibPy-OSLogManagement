from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Output of OS commands to str-convertible list for assignment to variables.'
PACKAGE_NAME = 'OSLogManagement'
AUTHOR = 'Santiago Benavidez (TITIR1X)'
EMAIL = 'SantiagoBenavidez@pythondeveloper.com'
GITHUB_URL = 'https://github.com/TITIR1X/PyLogManagement'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'Python', 'Console', 'Log', 'Management', 'RegEx', 'Variable', 'String', 'Output of OS commands to str-convertible list for assignment to variables.'
    ],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)