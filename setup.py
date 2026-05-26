from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [l for l in f.read().strip().split("\n") if l and not l.startswith("#")]

with open("brusnika_lms/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split('"')[1]
            break

setup(
    name="brusnika_lms",
    version=version,
    description="Connect Frappe / ERPNext with Brusnika.LMS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Brusnika Solutions",
    author_email="info@brusnika-solutions.com",
    url="https://brusnika-lms.com/",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
