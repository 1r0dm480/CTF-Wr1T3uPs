#!/usr/bin/python3

try:
    import hashlib
except ImportError:
    print("Error importing 'hashlib'")
    exit()

print("Bitup 2019 CTF #Atomic Write-Up")
print("Write-up Interactivo x 1v4n\n")
print("The challenge Hashing V1 says:")
print("""Apply the hash function to the
"bitup, por y para estudiantes" password, and use
that resulting hash value of 40 characters as a flag.
Example: bitup19{result_function_hash}. [Enter]: """)
f = input(" ")
print("We encode the string bitup, por y para estudiantes in SHA1. [Enter]: ")
f = input(" ")
hashingv1="bitup, por y para estudiantes"
m = hashlib.sha1()
m.update(hashingv1.encode('utf-8'))
print("\nThe result_function_hash is: {}".format(m.hexdigest()))
exit()
