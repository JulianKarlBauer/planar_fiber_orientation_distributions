import setuptools

setuptools.setup(
    name="planarfibers",
    version="0.0.1",
    author="Julian Karl Bauer",
    author_email="juliankarlbauer@gmx.de",
    description="PlanarFibers "
    "contains selected contributions of "
    "Bauer JK, Böhlke T. ?? "
    "Mathematics and Mechanics of Solids. Month? YYYY?. "
    "doi:??",
    url="https://github.com/JulianKarlBauer/planar_fiber_orientation_tensors_2021",
    packages=["planarfibers"],
    package_dir={"planarfibers": "planarfibers"},
    install_requires=[
        "numpy",
        "scipy",
        "sympy",
        "pandas",
        "matplotlib",  # Required for examples
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
