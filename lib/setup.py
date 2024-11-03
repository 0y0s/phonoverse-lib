from setuptools import setup

setup(
    name="phonoverse",
    version="1.0",
    description="Python client for the PhonoVerse Translation API",
    author="0y0s",
    author_email="0y0s.ofc@gmail.com",
    url="https://phonoverse.x10.bz/",
    py_modules=["phonoverse"],
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
) 
