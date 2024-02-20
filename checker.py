def read_eligible_list(file_path):
    eligible_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            address, summ = line.strip().split(',')
            eligible_dict[address] = float(summ)
    return eligible_dict

def read_wallets(file_path):
    wallets = []
    with open(file_path, 'r') as file:
        for line in file:
            wallets.append(line.strip())
    return wallets

def check_address(eligible_dict, address):
    if address in eligible_dict:
        return eligible_dict[address]
    else:
        return 0

if __name__ == "__main__":
    # Step 1: Read eligible list and convert to dictionary
    eligible_dict = read_eligible_list("eligible_list.txt")

    # Step 2: Read wallets file and convert to list
    wallets = read_wallets("wallets.txt")

    # Step 3: Iterate over wallets and print results
    for address in wallets:
        summ = check_address(eligible_dict, address)
        print(f"Address: {address}, Summ: {summ}")
