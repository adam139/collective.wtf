from setuptools import setup, find_packages

version = '1.0b10'

setup(
    name='collective.wtf',
    version=version,
    description=("GenericSetup importer and exporter for workflow definitions "
                 "that uses CSV instead of XML"),
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    # Get more strings from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone workflow genericsetup',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='http://plone.org',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component',
        'Products.CMFCore',
        'Products.DCWorkflow',
        'Products.GenericSetup',
        'plone.memoize',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
