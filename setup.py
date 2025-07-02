from setuptools import setup, find_packages

setup(
    name='roastme',
    version='0.1.0',
    description='Drop savage roasts with a single line of code',
    author='Harsh the Roast Lord',
    author_email='your_email@example.com',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown'
)
