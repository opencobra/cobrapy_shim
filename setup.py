from setuptools import setup

setup(
    name="cobrapy_shim",
    author="Ali Ebrahim",
    author_email="aebrahim@ucsd.edu",
    version="1.0",
    py_modules=["cobrapy_shim"],
    install_requires=["cobra>=0.4.0b3"],

    entry_points={"console_scripts": [
        "sbml2mat = cobrapy_shim:sbml_to_mat",
        "mat2sbml = cobrapy_shim:mat_to_sbml"]
                  },
    url="https://github.com/opencobra/cobrapy_shim",
    license="CC0",
    classifiers=[
        "Environment :: Console",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
        'Operating System :: OS Independent',
    ]

)
