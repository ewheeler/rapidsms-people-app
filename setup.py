from setuptools import setup, find_packages

setup(
    name='rapidsms-people',
    version='0.1',
    license="BSD",

    install_requires=['rapidsms'],

    description='People management application for RapidSMS',

    author='Evan Wheeler, Tobias McNulty',
    author_email='rapidsms@googlegroups.com',

    url='https://github.com/mwana/rapidsms-people-app',
    download_url='https://github.com/mwana/rapidsms-people-app/downloads',

    package_dir={'': 'lib'},
    packages=find_packages('lib', exclude=['*.pyc']),
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
