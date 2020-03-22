#!/usr/bin/python3

try:
    import base64
except ImportError:
    print("Error importing 'base64'")
    exit()

try:
    import hashlib
except ImportError:
    print("Error importing 'hashlib'")
    exit()

print("Bitup 2019 CTF #Atomic Write-Up")
print("Write-up Interactivo x 1v4n\n")
print("The challenge Encoding says:")
print("""Pass the string "binary rules" to base64
and use the resulting value as the flag.
Example: bitup19{text_in_other_base}. [Enter]: """)
f = input(" ")
print("We encode the string binary rules in base64. [Enter]: ")
f = input(" ")
encoding="binary rules"
m = base64.b64encode(encoding.encode("utf-8"))
print("\nThe result_function_encoding is: {}".format(str(m, "utf-8")))
exit()
