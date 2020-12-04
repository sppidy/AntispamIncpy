import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AntispamInc", 
    version="0.0.1",
    author="Example Author",
    url="antispaminc.tk",
    author_email="dev@antispaminc.tk",
    description="Python Wrapper For Antispam Inc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
            'requests',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
