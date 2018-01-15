from setuptools import setup

VERSION = "0.5.4"
DEPS = [
         "Flask"
       ]

setup(name="carmin-server",
      version=VERSION,
      description="REST API for exchanging data and remotely calling pipelines on CBrain",
      url="https://github.com/fli-iam/CARMIN",
      author="Tristan Glatard",
      author_email="tristan.glatard@gmail.com",
      classifiers=[
                "Programming Language :: Python",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 2.7",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: Implementation :: PyPy",
                "License :: OSI Approved :: MIT License",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Operating System :: OS Independent"
                  ],
      license="MIT",
      packages=["server"],
      include_package_data=True,
      test_suite="pytest",
      tests_require=["pytest"],
      setup_requires=DEPS,
      install_requires=DEPS,
      entry_points = {
        "console_scripts": [
        ]
      },
      data_files=[],
      zip_safe=False)