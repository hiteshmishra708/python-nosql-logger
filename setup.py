from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='python_nosql_logger',
    version='1.0.6',
    description='For logging & accessing application data with NoSQL databases (MongoDB & ElasticSearch)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hiteshmishra708/python-nosql-logger',
    author='Hitesh Mishra',
    author_email='hiteshmishra708@gmail.com',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='logger, django logger, flask logger, nosql logger, mongodb logger, setuptools, development, elasticsearch, elastic search logging',
    # package_dir={'': 'pynosql_logger'},
    install_requires=['requests'],
    packages=find_packages(),
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://github.com/hiteshmishra708/python-nosql-logger/issues',
        'Say Thanks!': 'https://linkedin.com/in/hiteshmishra708/',
        'Source': 'https://github.com/hiteshmishra708/python-nosql-logger/',
    },
)