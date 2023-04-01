from setuptools import setup
import setuptools

with open("ReadME.md","r") as fh:
    long_description = fh.read()
setup(
    name='vibeAI24',
    version='1.0.2',
    description='A library for predicting and blocking suspicious traffic',
    author='Vibe AI',
    author_email='contactvibe615@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    keywords=['cyberAI','AIcyber','vibeAI24'],
    install_requires=[
        'numpy',
        'pandas',
        'pydantic'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['vibeAI24']
)
