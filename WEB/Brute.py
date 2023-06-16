from BrainWallet import BrainWallet
from requests import get
from time import sleep


wallet = BrainWallet()

count = 0
with open("pass_list.txt") as fp:
    while True:
        count += 1
        passphrase = fp.readline()  
        if not passphrase:
            break       
        passphrase = passphrase.rstrip('\n')
        
        private_key, address = wallet.generate_address_from_passphrase(passphrase)

        try:
            received =  int(get(f'https://blockchain.info/q/getreceivedbyaddress/{address}/').text)/100000000.0
            print('Sleeping for 11 seconds...\n')
            sleep(11)
            if(received > 0):            
                balance = int(get(f'https://blockchain.info/q/addressbalance/{address}/').text)/100000000.0
                print('Sleeping for 11 seconds...\n')
                sleep(11)
            else:
                balance = 0
        except ValueError:
            print(f'Instance: [{passphrase}] - ValueError address: {address}\n')
            continue

        print(f'Instance: [{passphrase}] - Generated: {address} recieved: {received}, now balance: {balance}\n')
        if received > 0:
            with open('found.txt', 'a') as result:
                result.write(f'{balance} | {received} | {passphrase} | {address} | {private_key}\n')
            print(f'Instance: [{passphrase}] - Added address to found.txt\n')


