# vault-importer

A simple script designed to import KeepassXC CSV exports into Hashicorp Vault.

## Usage
```
vault_import
    --csv CSV    Location of the CSV file.
    --base BASE  Base path of your secrets in the vault.
    --url URL    URL of the Vault. Include the port.
```

## Installation
Execute `python3 setup.py install --user` to install.
