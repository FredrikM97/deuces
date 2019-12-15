"""
Deuces: A pure Python poker hand evaluation library
"""

from setuptools import setup
#[metadata]
setup(
    name='deuces',
    version='0.2',
    description=__doc__,
    #long_description=open('README.md').read(),
    author='Will Drevo',
    url='https://github.com/worldveil/deuces',
    license='MIT',
    packages=['deuces', 'performance'],
    extras_require={
        'hand_evaluator':"",
        'FiveEval':"",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment'
    ]
)
