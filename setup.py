from setuptools import setup, find_packages

setup(
    name='anim',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple animation library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elliotwaite/pycairo-animations',
    packages=find_packages(include=['anim', 'anim.*']),
    install_requires=[
        "Pillow",
        "tqdm",
        "pycairo"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)

