from setuptools import setup, find_packages

import pyawsopstoolkit_models

setup(
    name=pyawsopstoolkit_models.__name__,
    version=pyawsopstoolkit_models.__version__,
    packages=find_packages(),
    url='https://github.com/coldsofttech/pyawsopstoolkit-models.git',
    license='MIT',
    author='coldsofttech',
    description=pyawsopstoolkit_models.__description__,
    requires_python=">=3.10",
    install_requires=[
        "pyawsopstoolkit==0.1.19",
        "pyawsopstoolkit_validators==0.1.0"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=[
        "aws", "toolkit", "operations", "tools", "development", "python", "models", "utilities",
        "amazon-web-services"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ]
)
