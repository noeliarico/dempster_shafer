import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dempster_shafer", # Replace with your own username
    version="0.0.23",
    author="Noelia Rico, Luigi Troiano",
    author_email="noeliarico@uniovi.es",
    description="Tools for Dempster-Shafer theory of evidence computation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noeliarico/dempster_shafer",
    project_urls={
        "Bug Tracker": "https://github.com/noeliarico/dempster_shafer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'numpy',
        'numba'
    ],
)