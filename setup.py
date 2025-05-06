from setuptools import setup, find_packages

setup(
    name='lib_ml',
    description='Shared preprocessing logic',
    author='remla25-team13',
    packages=find_packages(),
    install_requires=[
        "numpy==1.26.4",
        "scikit-learn==1.4.2",
        "pandas==2.2.2",
        "scipy==1.13"
    ],
    python_requires='>=3.12',
)
