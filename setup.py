from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="swit-splunk-py",
    version="0.0.1",
    author="Howard Jeong",
    author_email="howard.jeong@swit.io",
    description="Swit Pubsub Client for Splunk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/switapi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)