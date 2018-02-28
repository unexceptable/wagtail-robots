from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name='wagtail-robots',
    long_description=long_description,
    version="0.1.1",
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
    ]
)
