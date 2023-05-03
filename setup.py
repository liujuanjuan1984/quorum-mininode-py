import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quorum_mininode_py",
    version="1.2.6",
    author="liujuanjuan1984, zhangwm404",
    author_email="qiaoanlu@163.com",
    description="a mini python sdk for quorum lightnode with http/https requests to quorum fullnode",
    keywords=["rumsystem", "quorum", "lightnode", "sdk"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liujuanjuan1984/quorum_mininode_py",
    project_urls={
        "Github Repo": "https://github.com/liujuanjuan1984/quorum_mininode_py",
        "Bug Tracker": "https://github.com/liujuanjuan1984/quorum_mininode_py/issues",
        "About Quorum": "https://github.com/rumsystem/quorum",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["example"]),
    python_requires=">=3.5",
    install_requires=[
        "requests",
        "eth_keys",
        "pyrage",
        "protobuf",
        "eth_account",
    ],
)
