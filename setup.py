from setuptools import setup, find_packages


with open('README.md', 'r') as file:
    long_description = '\n'.join(file.readlines()[3:])


requirements = [
    'fecfile>=0.6.1',
    'XlsxWriter>=1.1.6',
]


setup(
    name='fec2xlsx',
    version='0.1.2',
    description='A python library for making Excel files from FEC filings',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/esonderegger/fec2xlsx',
    project_urls={
        'Bug Tracker': 'https://github.com/esonderegger/fec2xlsx/issues',
        'Source Code': 'https://github.com/esonderegger/fec2xlsx/',
    },
    author='Evan Sonderegger',
    author_email='evan@rpy.xyz',
    license='MIT',
    keywords='fec campaign finance politics',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(exclude=['docs', 'test-data']),
    install_requires=requirements,
    zip_safe=False,
)
