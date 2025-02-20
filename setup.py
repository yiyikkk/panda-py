from skbuild import setup
from setuptools import find_packages

setup(
    name="panda_py",
    version="0.1.0",
    description="Python bindings for Panda robot using pybind11",
    packages=find_packages(where="src"),
    package_dir={"": "src"}, 
    cmake_install_dir="panda_py", 
    python_requires=">=3.10",
    include_package_data=True  
)
