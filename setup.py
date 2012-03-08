from setuptools import setup, find_packages

import logging
import multiprocessing
from setup_ext import UpdateLessCSSCommand

setup(
    name='tw2.lesscss',
    version='2.0.1c',
    description='Less CSS support for ToscaWidgets 2',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    url='https://github.com/toscawidgets/tw2.lesscss',
    install_requires=[
        "tw2.core",
        'mako',
    ],
    tests_require=[
        'nose',
        'strainer'
    ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.lesscss
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    cmdclass = {
        'updatelesscss' : UpdateLessCSSCommand,
    }
)
