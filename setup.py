from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pdf_thumbnail/__init__.py
from pdf_thumbnail import __version__ as version

setup(
	name="pdf_thumbnail",
	version=version,
	description="PDF Thumbnail For ERPNext",
	author="Zaspisoft",
	author_email="zaspisoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
