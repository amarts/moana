from setuptools import setup

def version():
    with open("VERSION") as version_file:
        return version_file.read().strip()


setup(
    name="moana",
    version=version(),
    packages=["moana"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "moana = moana.main:main",
        ]
    },
    zip_safe=False,
    author="Kadalu Authors",
    author_email="engineering@kadalu.io",
    description="Manage Kadalu Storage using Moana",
    license="Apache-2.0",
    keywords="kadalu, container, gluster, cli",
    url="https://github.com/kadalu/moana",
    long_description="""
    Manage Kadalu Storage using Moana
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
