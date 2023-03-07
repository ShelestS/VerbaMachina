from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='VerbaMachina',
      version="0.0.1",
      description="VarbaMachina project",
      license="No",
      author="Shelest Sergei, Marvin Naessig, Sebastien Olive",
      author_email="pass23ss23ss23@gmail.com",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
