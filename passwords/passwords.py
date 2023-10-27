import hashlib
import binascii

'''
==========PART 1==========
'''
dict = {}
words = [line.strip().lower() for line in open('passwords.txt')]

# Puts all possible password digests into dictionary
for word in words:
    encoded = word.encode('utf-8')
    hash = hashlib.sha256(encoded)
    digest = hash.digest()
    digest_as_hex = binascii.hexlify(digest)
    digest_as_hex_string = digest_as_hex.decode('utf-8')
    dict[digest_as_hex_string] = word

cracked_passwords = {}
f1 = open("cracked1.txt", "w")

# Looks for password in dictionary and gives word
for line in open('part1.txt'):
    fields = line.split(":")
    user = fields[0]
    hash = fields[1]
    password = dict[hash]
    cracked_passwords[user] = password
    f1.writelines([user, ":", password, "\n"])


'''
==========PART 2==========
'''  
dict = {}
user_pass = {}
words = [line.strip().lower() for line in open('passwords.txt')]
f2 = open("cracked2.txt", "w")

# Place all passwords and usernames into hash
for line in open('part2.txt'):
    fields = line.split(":")
    user = fields[0]
    hash1 = fields[1]
    user_pass[hash1] = user

# Nested for loop to get concatenation for two word passwords
for word1 in words:
    for word2 in words:
        concatenate = word1 + word2
        encoded = concatenate.encode('utf-8')
        hash = hashlib.sha256(encoded)
        digest = hash.digest() 
        digest_as_hex = binascii.hexlify(digest)
        digest_as_hex_string = digest_as_hex.decode('utf-8')

        # Checks if two word password is in dictionary
        if (digest_as_hex_string in user_pass.keys()):
            f2.writelines([user_pass[digest_as_hex_string], ":", concatenate, "\n"])
            print(user_pass[digest_as_hex_string], ":", concatenate)

'''
==========PART 3==========
'''
f3 = open("cracked3.txt", "w")

# Parse passwords for part 3
for line in open('part3.txt'):
    fields = line.split(":")
    user = fields[0]
    full_salt = fields[1]

    # Parse salt
    split_salt = full_salt.split("$")
    salt = split_salt[2]
    password = split_salt[3]
    
    # Concatenates salt with each word and checks if it matches digest_as_hex_string
    for word in words:
        salt_word = salt + word
        encoded = salt_word.encode('utf-8')
        hash = hashlib.sha256(encoded)
        digest = hash.digest()
        digest_as_hex = binascii.hexlify(digest)
        digest_as_hex_string = digest_as_hex.decode('utf-8')

        if (password == digest_as_hex_string):
            print(user, ":", word)
            f3.writelines([user, ":", word, "\n"])