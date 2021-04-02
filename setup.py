import setuptools
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smsiran",
    version="0.0.3",
    author="Soroush piri zendedel",
    author_email="soroush_zendedel@live.com",
    keywords=["SMS","Persian","iran","web service","sms web service"],
    description="A library for using SMS web services in IRAN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avanditc/smsiran",
    download_url = 'https://github.com/avanditc/smsiran/archive/refs/tags/v0.0.3.tar.gz',
    project_urls={
        "Bug Tracker": "https://github.com/avanditc/smsiran/issues",
        "Owner": "https://AvandITC.ir",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'requests',
    ],
    python_requires=">=3.6",
)