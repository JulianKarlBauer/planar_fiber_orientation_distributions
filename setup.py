import setuptools

setuptools.setup(
    name="planarfiberdist",
    version="0.0.1",
    author="Julian Karl Bauer",
    author_email="juliankarlbauer@gmx.de",
    description="PlanarFiberDist "
    "contains selected contributions of "
    "Bauer JK, Böhlke T. ?? "
    "Mathematics and Mechanics of Solids. Month? YYYY?. "
    "doi:??",
    url="https://github.com/JulianKarlBauer/planar_fiber_orientation_tensors_2021",
    packages=["planarfiberdist"],
    package_dir={"planarfiberdist": "planarfiberdist"},
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
