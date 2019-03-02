from setuptools import setup, find_packages

setup(
    name="ttrpy",
    packages=find_packages(),
    version="0.1.1",
    license="Apache License 2.0",
    description="Technical analysis and other functions to construct technical trading rules with Python",
    author="joelowj",
    author_email="ong.joel.94@gmail.com",
    url="https://github.com/joelowj/ttrpy",
    download_url="https://github.com/joelowj/ttrpy/archive/v0.1.0.tar.gz",
    keywords=[
        "finance",
        "technical analysis",
        "technical indicators",
        "investment",
    ],
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
    ],
)
