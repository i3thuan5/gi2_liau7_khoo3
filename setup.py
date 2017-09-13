from distutils.core import setup


setup(
    name='gi2_liau7_khoo3',
    packages=[],
    version='0.1.0',
    author='薛丞宏',
    author_email='ihcaoe@gmail.com',
    url='https://xn--v0qr21b.xn--kpry57d/',
    keywords=[
        'Corpus', 'gí-liāu-khòo', '語料庫', 'gi2-liau7-khoo3',
        'Taiwan', 'Taiwanese',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'django',
        'Taiwanese-Speech-And-Text-Corpus',
        'kau3-tian2_iong7-ji7',
    ],
)
