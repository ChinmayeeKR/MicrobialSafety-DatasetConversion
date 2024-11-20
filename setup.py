from setuptools import setup, find_packages

setup(
    name="convert2squad",  
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "contourpy==1.3.1",
        "cycler==0.12.1",
        "fonttools==4.55.0",
        "kiwisolver==1.4.7",
        "matplotlib==3.9.2",
        "numpy==2.1.3",
        "packaging==24.2",
        "pillow==11.0.0",
        "pyparsing==3.2.0",
        "python-dateutil==2.9.0.post0",
        "six==1.16.0",
    ],
    entry_points={
        "console_scripts": [
            "convert2squad=convert2squad.cli:main",  
        ],
    },
    description="CLI tool for conversion of categorized dataset into SQuAD jsons",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
