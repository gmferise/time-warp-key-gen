import hashlib
import hmac
import secrets

# Program params
SECURITY_LEVEL = 1  # bytes in a secret/key
HASH_ALGO = hashlib.sha256  # hashing algo used to verify keys

MANUFACTURER_SECRET = secrets.token_hex(SECURITY_LEVEL)

def generate_key():
    # Generate a random number as hex
    key_number = secrets.token_hex(SECURITY_LEVEL)

    # Get both our key and secret as bytes
    bin_secret = bytes(MANUFACTURER_SECRET, 'utf-8')
    bin_key = bytes(key_number, 'utf-8')

    # Hash them to get the hex digest
    hash = hmac.new(bin_secret, bin_key, HASH_ALGO)
    key_check = hash.hexdigest()

    # The final key is the combination
    return key_number + key_check

def validate_key(key):
    # Get both our key and secret as bytes
    bin_secret = bytes(MANUFACTURER_SECRET, 'utf-8')
    bin_key = bytes(key[:SECURITY_LEVEL*2], 'utf-8')

    # Hash them to get the hex digest
    hash = hmac.new(bin_secret, bin_key, HASH_ALGO)
    key_check = hash.hexdigest()

    # Check that they're the same!
    return key_check == key[SECURITY_LEVEL*2:]

if __name__ == '__main__':
    # Check some real keys
    print('Real keys:')
    for _ in range(100):
        key = generate_key()
        is_valid = validate_key(key)
        valid_str = 'is valid' if is_valid else 'is not valid'
        print(f'"{key}" {valid_str}')
    
    print('Fake keys:')
    # Try to make our own key!
    for _ in range(100):
        fake_key = secrets.token_hex(len(key) // 2)
        is_valid = validate_key(fake_key)
        valid_str = 'is valid' if is_valid else 'is not valid'
        print(f'"{fake_key}" {valid_str}')
