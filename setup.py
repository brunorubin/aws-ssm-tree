from setuptools import setup, find_packages

setup(
    name="aws-ssm-tree",
    version="0.2.0",
    author="Bruno Rubin",
    author_email="bruno.rubin@gmail.com",
    description="Builds a tree of parameters from AWS System Manager Parameter Store.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brunorubin/aws-ssm-tree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "boto3",
        "treelib",
    ],
    packages=find_packages(exclude=["tests", "img"]),
    entry_points={
        'console_scripts': [
            'ssm-tree = ssm_tree.main:main',
        ],
    }
)