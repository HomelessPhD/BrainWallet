import os

b58_powers = [0] * 34;
for i in range(34):
    b58_powers[i] = 58 ** i
    
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'   
 
def base58_to_hash_unc_p2pkh(b58_string):
    
    leading_ones = len(b58_string) - len(b58_string.lstrip('1'))
    
    address_dec = 0
    for i in range(len(b58_string)):
        address_dec = address_dec + alphabet.index(b58_string[-(i+1)]) * b58_powers[i]
        
    address_hex = hex(address_dec)[2:]
    
        # Add '00' for each 1 leading '1'
    for one in range(leading_ones):
        address_hex = '00' + address_hex
    return address_hex[2:-8]


num_lines = 0
with open('bitcoin_addresses_and_balance_04.08.23.txt', 'r') as fp:
    num_lines = sum(1 for line in fp)

print("------transform BTC addresses to P2PKH hashes-------")
if os.path.exists('P2PKH_hash.txt'):
  os.remove('P2PKH_hash.txt')
  
count = 0
with open('bitcoin_addresses_and_balance_04.08.23.txt') as fp:
    while True:
        balance_line = fp.readline()
        if not balance_line:
            break       
        balance_line = balance_line.rstrip('\n')
        count += 1
    
        address_base58 = balance_line.split('\t')[0];
        balance = balance_line.split('\t')[1];
        
            # Check if address P2PKH
        if(address_base58[0]=='1'):
                # Revert P2PKH address to the closest hash - to number
            with open('P2PKH_hash.txt', 'a') as result:
                hash_val = base58_to_hash_unc_p2pkh(address_base58)
                result.write(f'{hash_val}\n')
        
        if((count % 1000000) == 0):
            print(f"{round((count / num_lines)*100,2)} % ")
            
print(f"{round((count / num_lines)*100,2)} % ")
print("------transform BTC addresses to P2PKH hashes FINISHED -------")

