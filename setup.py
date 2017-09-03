from setuptools import find_packages, setup

install_requires = {
    # Async request
    'aiohttp >= 2.2.5',
    'cchardet >= 2.1.1',
    'aiodns >= 1.1.1',
    # Async util
    'async-timeout >= 1.3.0',
    # Database
    'SQLAlchemy >= 1.1.13',
    'alembic >= 0.9.5',
    # CLI
    'Click >= 6.7',
    # Configuration
    'toml >= 0.9.2',
    # Crontab
    'aiocron >= 0.6',
    # Fuzzy Search
    'fuzzywuzzy[speedup] >= 0.15.1',
    # HTML
    'lxml >= 3.8.0',
    'cssselect >= 1.0.1',
    # i18n
    'babel >= 2.5.0',
    # util
    'attrdict >= 2.0.0',
}

tests_require = {
    'mypy >= 0.521',
    'pytest >= 3.2.1',
}

extras_require = {
    'tests': tests_require,
    'lint': {
        'flake8 >= 3.4.1',
        'flake8-import-order >= 0.13',
    },
}

setup(
    name='yui',
    version='0.0.0',
    description='Slack Bot for item4.slack.com',
    url='https://item4.slack.com',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'yui=yui.cli:main',
        ],
    }
)
