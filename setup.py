from setuptools import setup, find_packages

setup(
    name="pscde",
    version="0.1.0",
    packages=find_packages(include=["pscde", "pscde.*"]),
    install_requires=[
        "numpy",
        "pandas",
        "xarray",
        "zarr",
        "numcodecs"
    ],
    entry_points={
        "console_scripts": [
            # Optional: add CLI hooks here later
        ]
    }
)
