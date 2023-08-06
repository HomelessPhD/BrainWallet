import codecs
import hashlib
import ecdsa

import time

def pass_to_hash_unc_p2pkh(passphrase):
        # The classic BrainWallet private key is simple sha256 hash
        # computed from "BrainWallet passphrase"
    private_key = str(hashlib.sha256(passphrase.encode('utf-8')).hexdigest())    
    private_key_bytes = codecs.decode(private_key, 'hex')
        # Get ECDSA public key (paired to given private key)
    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    key_hex = codecs.encode(key_bytes, 'hex')
        # Add bitcoin byte '04' that denote UNCOMPRESSED public key
    bitcoin_byte = b'04'
    public_key = bitcoin_byte + key_hex
        # Compute the hash: public key bytes -> sha256 -> RIPEMD160
    public_key_bytes = codecs.decode(public_key, 'hex')
            # Run SHA256 for the public key
    sha256_bpk = hashlib.sha256(public_key_bytes)
    sha256_bpk_digest = sha256_bpk.digest()
            # Run ripemd160 for the SHA256
    ripemd160_bpk = hashlib.new('ripemd160')
    ripemd160_bpk.update(sha256_bpk_digest)
    ripemd160_bpk_digest = ripemd160_bpk.digest()
    ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
        # Return RIPEMD160 hash
    return ripemd160_bpk_hex.decode("utf-8")

    # Logic is same, but the public key is COMPRESSED: 
    # used only 32 bytes of the public key with "bitcoin code" set to
    # '03' or '02' based on the sign of the other unused 32 bytes
def pass_to_hash_c_p2pkh(passphrase):
    private_key = str(hashlib.sha256(passphrase.encode('utf-8')).hexdigest())
    private_key_bytes = codecs.decode(private_key, 'hex')

    key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    
    if key_bytes[-1] & 1:
        bitcoin_byte = b'03'
    else:
        bitcoin_byte = b'02'
            
    key_bytes =  key_bytes[0:32]    
    key_hex = codecs.encode(key_bytes, 'hex')

    public_key = bitcoin_byte + key_hex

    public_key_bytes = codecs.decode(public_key, 'hex')
    sha256_bpk = hashlib.sha256(public_key_bytes)
    sha256_bpk_digest = sha256_bpk.digest()
    ripemd160_bpk = hashlib.new('ripemd160')
    ripemd160_bpk.update(sha256_bpk_digest)
    ripemd160_bpk_digest = ripemd160_bpk.digest()
    ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')  
      
    return ripemd160_bpk_hex.decode("utf-8")

    # Download the RIPEMD160 database of non-zero P2PKH BTC addresses
print('Download the P2PKH hashes database....\n')

num_lines = 0
with open('P2PKH_hash.txt', 'r') as fp:
    num_lines = sum(1 for line in fp)
    
count = 0
P2PKH_dictionary = {}
with open('P2PKH_hash.txt', 'r') as fp:
    while True:
        count += 1
        
        hash_line = fp.readline()  
        
        if not  hash_line:
            break       
        hash_line =  hash_line.rstrip('\n')
        P2PKH_dictionary[hash_line] = 1
        
        if((count % 1000000) == 0):
            print(f'{round(100*(count/num_lines),2)} %')
    print(f'{round(100*(count/num_lines),2)} %')
            
print('P2PKH hashes database loaded and prepared to use\n')

    # Run the bruteforce of BrainWallet passphrases
    # (that is read from <pass_list.txt> file
print('Experiment with brute P2PKH....')

num_lines = 0
with open('pass_list.txt', 'r') as fp:
    num_lines = sum(1 for line in fp)

count = 0
passphrase_buffer = []
with open('pass_list.txt') as fp:
    while True:
        t_start = time.time()
        
        for i in range(10_000):
            count += 1            
            try:
                passphrase = fp.readline()  
                if not passphrase:
                    break       
                passphrase = passphrase.rstrip('\n')
                passphrase_buffer.append(passphrase)
            except:
                print(f'Some error on line [{count}]\n')
                continue
        if len(passphrase_buffer) == 0:
            break
        
        p_num = len(passphrase_buffer)
        
        while len(passphrase_buffer) > 0:
            passphrase = passphrase_buffer.pop()
        
            pass_hash = pass_to_hash_unc_p2pkh(passphrase)
            res = P2PKH_dictionary.get(pass_hash, 0)
        
            if( res == 1):
                print(f'[{passphrase}] seems promising\n');
                with open('found.txt', 'a') as result:
                    result.write(f'{passphrase}\n')

            pass_hash = pass_to_hash_c_p2pkh(passphrase) 
            res = P2PKH_dictionary.get(pass_hash, 0)
        
            if( res == 1):
                print(f'[{passphrase}] seems promising\n');
                with open('found.txt', 'a') as result:
                    result.write(f'{passphrase}\n')      
        
        
        t_end = time.time()
        print(f"{round(p_num / (t_end - t_start))} pass/s | {round((count / num_lines)*100,2)} % ")
    print(f"{round((count / num_lines)*100,2)} % ")

        
