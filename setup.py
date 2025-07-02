from setuptools import setup, find_packages

setup(
    name='roastme',
    version='0.1.1',
    description='Drop savage roasts with a single line of code',
    author='Harsh srivastava',
    author_email='blueharsh2@gmail.com',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description = open("README.md", encoding="utf-8").read(),

    long_description_content_type='text/markdown'
)
