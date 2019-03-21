"""
The build/compilations setup

>> pip install -r requirements.txt
>> python setup.py install
"""
import pip
import logging
import pkg_resources
try:
    from setuptools import setup, find_packages
except ImportError:
    print('Failed to import setuptools. Install it first')


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path, session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]


# parse_requirements() returns generator of pip.req.InstallRequirement objects
try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = []

setup(
    name='deep_sort',
    version='1.0',
    url='https://github.com/AlexanderSoroka/deep_sort',
    author='Nicolai Wojke, Alexander Soroka',
    author_email='soroka.a.m@gmail.com',
    license='GPLv3',
    description='Simple Online Realtime Tracking with a Deep Association Metric',
    packages=find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.4',
    long_description="""Simple Online and Realtime Tracking (SORT) is a pragmatic approach to multiple object tracking 
    with a focus on simple, effective algorithms.""",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GPLv3 License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Tracking"
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="DeepSORT tensorflow",
)
