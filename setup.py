from setuptools import setup, find_packages

version="1.0.0"
setup(
    name="files2rouge",
    version=version,
    description="Calculating ROUGE score between two files (line-by-line)",
    url="http://github.com/pltrdy/files2rouge",
    download_url="https://github.com/pltrdy/files2rouge/archive/%s.tar.gz" % version,
    author="pltrdy",
    author_email="pltrdy@gmail.com",
    keywords=["NL", "CL", "natural language processing", "computational linguistics", "summarization"],
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Linguistic"
        ],
    license="LICENCE.txt",
    long_description=open("README.md").read(),

    entry_points={
      'console_scripts': [
        'files2rouge=files2rouge:main'
      ]
    },
    install_requires = [
      "pythonrouge==0.3"
    ],
    dependency_links = [
     "https://github.com/pltrdy/pythonrouge/tarball/0.3#egg=pythonrouge-0.3",
    ],
    include_package_data=True,
)
