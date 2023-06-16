# BrainWallet
BTC BrainWallet brute (a dummy script)

    Install python and all required:
    
sudo apt-get update

sudo apt install python3 python3-pip

    Add support for "old" hashing into hashlib (OpenSSL):

```
To quickly enable it, find the directory that holds your OpenSSL config file or a symlink to it, by running the below command:

openssl version -d

You can now go to the directory and edit the config file (it may be necessary to use sudo):

nano openssl.cnf

Make sure that the config file contains following lines:

openssl_conf = openssl_init

[openssl_init]
providers = provider_sect

[provider_sect]
default = default_sect
legacy = legacy_sect

[default_sect]
activate = 1

[legacy_sect]
activate = 1
```

    Install all required packaged ("hashlib" and  "codecs" are usually default modules\libs, but "ecdsa" - not, so install it):

pip install ecdsa



----FOR ELECTRUM SCRIPT USING-----
    Install dependencies
sudo apt-get install python3-pyqt5 libsecp256k1-dev python3-cryptography

    Install electrum through Python:

wget https://download.electrum.org/4.4.4/Electrum-4.4.4.tar.gz

tar -xvf Electrum-4.4.4.tar.gz
cd Electrum-4.4.4/
python3 -m pip install .[fast]
