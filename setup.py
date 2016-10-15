# -*- encoding: utf-8 -*-
import os
from setuptools import setup


ENVS = ('test', 'dev', 'prod')


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requirements(env='base'):
    return [
        line for line in read('requirements/{}.txt'.format(env)).splitlines()
        if not line.startswith('#')
    ]


setup(
    name='{{ project_name }}',
    version='0.0.1',
    author='{{ author }}',
    author_email='{{ author_email }}',
    description='{{ description }}',
    long_description=read('README.md'),
    url='http://{{ project_name }}.local/',
    keywords='',
    platforms=['any'],
    license='Apache Software License v2.0',
    packages=['{{ project_name }}'],
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements(),
    extras_require={env: read_requirements(env) for env in ENVS},
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.__main__:prod',
            'dev_{{ project_name }} = {{ project_name }}.__main__:dev',
            'test_{{ project_name }} = {{ project_name }}.__main__:test',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
