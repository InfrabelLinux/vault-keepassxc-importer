from setuptools import setup
setup(
        name='vault-importer',
        version='1.0.0',
        author='Pieter De Praetere',
        author_email='pieter.de.praetere@helptux.be',
        packages=[
            'vault_importer'
        ],
        install_requires=[
            'requests'
        ],
        url='https://github.com/pieterdp/vault-keepassxc-importer',
        license='Apache',
        description='Import a KeepassXC CSV file into Hashicorp Vault.',
        scripts=[
            'bin/vault_import'
        ]
)
