from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clementbiteau/42Python/Python0/ex09",
    author="Clément Biteau",
    author_email="cbiteau@42.fr",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
