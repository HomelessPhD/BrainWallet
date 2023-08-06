# Brain Wallet
<Here i will add a short explanation of what the BrainWallet was\is, but a bit later>

# Short instruction how to use the "dummy brutting scripts" in order to brute BTC Brain Wallet phrases

The main idea here is to compose the {private key -> public key -> BTC address} for each phrase of interest
AND check the resulting BTC address balance using one of possible ways. The first part is trivial, but the second
part could be solved in different ways in general: 
1) make a WEB API request (https://blockchain.info/q/getreceivedbyaddress/{address}/) - it has high timeout
   (making lots of requests could result in BAN - so the script contain the "sleep". It is very slow option)
2) make an Electrum request (install Electrum client locally on PC and make request to this client - seems like
   it also could have some timeouts where else nodes of Electrum would ban you, but i am not sure about that,
   to be safe i have added some small extra pause like for WEB option. This "Electrum" option is much faster
   then WEB but still much much slower than possible third option in the list)
   
3) make a request to the locally storred SQL database of BTC addresses balances (some guys prepare such bases
   parsing all the BTC blockchain into SQL databases sharing them - i have not tried it yet for Brain Wallets,
   but its possible. If someone interested i could try to work with that and write here my experience.)

The brute scripts rely on the Python, and so below a short instruction for Ubuntu how to prepare it to run the script:

***Install python and all required:***
```    
sudo apt-get update
sudo apt install python3 python3-pip
```

***Add support for "old" hashing into hashlib (OpenSSL):***
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

***Install all required packages ("hashlib" and  "codecs" are usually default modules\libs, but "ecdsa" - not, so install it):***

```pip install ecdsa```

## The WEB way

To use the WEB API option (slowest possible), just run the script Brute.py from the folder "WEB":
```python3 Brute.py```

The list of phrases to try (to brute) will be taken by the script from the file "pass_list.txt" and all interesting findings would be
placed in file "found.txt".

## The Electrum way

To go this way, the Electrum should be installed. The way to that shown below (just taken from official Electrum site - you could follow 
there for instrunctions):

***Install dependencies***

```sudo apt-get install python3-pyqt5 libsecp256k1-dev python3-cryptography```

***Install electrum through Python:***
```
wget https://download.electrum.org/4.4.4/Electrum-4.4.4.tar.gz

tar -xvf Electrum-4.4.4.tar.gz
cd Electrum-4.4.4/
python3 -m pip install .[fast]
```

The script works nearly the same way - run "Brute_electrum.py" from the folder "Electrum". The phrases to brute are taken from "pass_list.txt",
and the results are stored in "found.txt"
```python3 Brute_electrum.py```

## The Hash Table  - brute in Python
(This is the fastest described here way)
   To go this way, the BTC balances database should be downloaded and placed in the same folder where "1_revert_to_hash.py" and "2_brute_passphrases.py" located . When the database file downloaded (and, if needed, unpacked - from tar.gz to *.txt file) - correct the filename in scrypt "1_revert_to_hash.py".

Run the "1_revert_to_hash.py" to prepare the database of RIPEMD160 hashes (P2PKH addresses). Now you can and "2_brute_passphrases.py" after that to run the bruteforce

Any ideas\questions or propositions you may send to generalizatorSUB@gmail.com.

## P.S.
Thank you for spending time on my notes, i hope it was not totally useless and you've found something interesting. 

-------------------------------------------------------------------------
### References:
[]

-------------------------------------------------------------------------
### Support
I am poor Ukrainian student that will really appreciate any donations.
I have no home (flat\appartment), live in the dorm trying to accumulate funds
for the smallest flat in the city - with no success at the moment,
have nearly 10% of needed amount.
 
P.S. Successfully evacuated from occupied regions of Ukraine.

**BTC**:  `1QKjnfVsTT1KXzHgAFUbTy3QbJ2Hgy96WU`

**LTC**:  `LNQopZ7ozXPQtWpCPrS4mGGYRaE8iaj3BE`

**DOGE**: `DQvfzvVyb4tnBpkd3DRUfbwJjgPSjadDTb`
 
 **BSV**: `1E56gGQ1rYG4kkRo5qPLMK7PHcpVYj15Pv`
