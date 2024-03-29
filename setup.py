from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name='wagtail-robots',
    long_description=long_description,
    version="0.3.1",
    description='Robots.txt exclusion for Wagtail, complementing Sitemaps.',
    author='Adrian Turjak',
    author_email='adriant@catalyst.net.nz',
    url='https://github.com/adrian-turjak/wagtail-robots/',
    packages=find_packages(),
    package_data={
        'robots': [
            'templates/robots/*.html',
        ],
    },
    install_requires=[
        'wagtail>=2.15',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Wagtail :: 2',
        'Framework :: Wagtail :: 3',
        'Framework :: Wagtail :: 4',
    ]
)
