import setuptools

setuptools.setup(
    name = 'PiMath',
    version = '1.0',
    author = 'HPJG',
    author_email = '1846407929@qq.com',
    description='Π PiMath:A Python Math Package',
    keywords='math',
    url='https://github.com/HPJG/PiMath', 
    classifiers=[ 
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
            'Topic :: Scientific/Engineering :: Mathematics'
        ],
    license='GNU General Public License v3', 

    packages=setuptools.find_namespace_packages()
)
