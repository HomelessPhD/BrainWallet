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
   To go this way, the BTC balances database should be downloaded (Here you could download the database (it is tared - untar to use [[1]](https://file.io/k2yapITLxppk) (time to time the hosting service remove the file - just msmg me if needed), and here where it was taken [[1']](https://t.me/Blockchain_BTC_ETH_DUMPS)) and placed in the same folder where "1_revert_to_hash.py" and "2_brute_passphrases.py" located . When the database file downloaded (and, if needed, unpacked - from tar.gz to *.txt file) - correct the filename in scrypt "1_revert_to_hash.py".

Run the "1_revert_to_hash.py" to prepare the database of RIPEMD160 hashes (P2PKH addresses). 

   Finally, you are ready to run the bruteforce - "2_brute_passphrases.py". 
This script will read the RIPEMD160 database (*.txt file that the "1_revert_to_hash.py" script prepared), compose the Hash Table upon that (dictionary) and loop over each passphrase from "pass_list.txt" verifying its "balance" through composed hashtable (actually it checks not the balance but if balance is non-zero - simple scripts modification could allow to check the balances values). 

This is the fastest way to check whether the balance of the private key (appropriate address) is positive or not: without multitrading, on a single core, 1 check in python requires less than E-06 s on my 9700k CPU system. BUT, the transformation of PASSPHRASE to the RIPEMD160 hash is much slower, ~ E-03 s (per compressed + un-compressed address) on my 9700k CPU system and so the final final speed will be limited now by this heavy elyptic curve + hashing operations (in cotrast to previous solutions where the speed were limited by balance check)

This idea could be improved by utilizing multitrading - running a few instances of the same script (2nd script - with different pass_list.txt) OR slightly modifying the 2nd script to run itself on a few threads.

Any ideas\questions or propositions you may send to generalizatorSUB@gmail.com.

## P.S.
Thank you for spending time on my notes, i hope it was not totally useless and you've found something interesting. 

-------------------------------------------------------------------------
### References:
[1] - BTC addresses:balances database (tared) - https://file.io/k2yapITLxppk

[1'] Telegram channel with fresh BTC addresses:balances databases - https://t.me/Blockchain_BTC_ETH_DUMPS

-------------------------------------------------------------------------
### Support
I am poor Ukrainian student that will really appreciate any donations.
Successfully evacuated from occupied regions of Ukraine.
 
P.S. Successfully evacuated from occupied regions of Ukraine.

**BTC**:  `1QKjnfVsTT1KXzHgAFUbTy3QbJ2Hgy96WU`

**LTC**:  `LNQopZ7ozXPQtWpCPrS4mGGYRaE8iaj3BE`

**DOGE**: `DQvfzvVyb4tnBpkd3DRUfbwJjgPSjadDTb`
 
 **BSV**: `1E56gGQ1rYG4kkRo5qPLMK7PHcpVYj15Pv`
