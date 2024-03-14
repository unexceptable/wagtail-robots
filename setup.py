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
        'wagtail>=5.2',
        'wagtail-modeladmin>=2.0',
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
    ]
)
