from setuptools import setup, find_packages

setup(
    name='tree-thon',
    version='0.1',
    description='TreeThon Language Compiler',
    long_description='A Python library for compiling TreeThon language code.',
    author=['Ritesh Mahale', 'Shreyash Mehshram'],
    author_email='ritesh@example.com',
    url='https://github.com/everest1508/treethon-compiler',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='tree-thon compiler language',
)

'''
Development Status :: 1 - Planning
Development Status :: 2 - Pre-Alpha
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
Development Status :: 6 - Mature
Development Status :: 7 - Inactive
'''

'''
python -m unittest discover tests
python setup.py sdist bdist_wheel
twine upload dist/*
'''
