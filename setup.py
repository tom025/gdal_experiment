from setuptools import setup


def read_requirements(path):
    with open(path) as fp:
        return list(
            map(lambda l: l.rstrip(), fp)
        )

setup(
    name="gdal_experiment",
    version="0.1.dev0",
    packages=[],
    setup_requires=read_requirements('requirements/setup.txt')
)
