from setuptools import find_packages, setup
setup(
    name='pypopup',
    packages=find_packages(),
    version='0.1.0',
    description='Simple Cross-Platform Notification Library',
    author='Milosz Kolodziejski',
    license='MIT',
    install_requires=[
        'bleach==4.1.0',
        'certifi==2021.10.8',
        'charset-normalizer==2.0.8',
        'colorama==0.4.4',
        'docutils==0.18.1',
        'idna==3.3',
        'importlib-metadata==4.8.2',
        'keyring==23.3.0',
        'packaging==21.3',
        'pkginfo==1.8.1',
        'plyer==2.0.0',
        'Pygments==2.10.0',
        'pync==2.0.3',
        'pyparsing==3.0.6',
        'python-dateutil==2.8.2',
        'readme-renderer==30.0',
        'requests==2.26.0',
        'requests-toolbelt==0.9.1',
        'rfc3986==1.5.0',
        'six==1.16.0',
        'tqdm==4.62.3',
        'twine==3.6.0',
        'urllib3==1.26.7',
        'webencodings==0.5.1',
        'zipp==3.6.0'
        ]
)