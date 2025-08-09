# Nicolas Valdez Tue Aug  5 13:34:20 2025
# NicolasValdezRSASystem
# Creates a complete RSA crypto system
# Input(s):
# p, prime number, 9<p<1000
# q, prime number, 9<q<1000
# M, string
# e, np.gcd(e,t)=1
# Output:
# Private key pair
# Public key pair
# M, encrypted
# M, decrypted
# Main Formulas:
# Totient function,
# Greatest common denominator,
# Encryption,
# Modular Multiplicative Inverse,
# Decryption

import pyinputplus as pyip # https://pypi.org/project/PyInputPlus/
import numpy as np # https://pypi.org/project/numpy/
import euler_maths as euler # https://pypi.org/project/euler-maths/

# Welcoming Statement
print('Creates a complete RSA crypto system.')

# Input validation
min_num=10
max_num=999
def is_prime(n,min_num=min_num,max_num=max_num):
    '''Check if number is prime. Returns true if prime, else false.'''
    n=float(n)
    prime=euler.is_prime(n)
    if n!=int(n):
        raise Exception('Number must be an integer.')
    if prime==False:
        raise Exception('Number must be a prime number.')
    if n<min_num:
        raise Exception(f'Number must be at least {min_num}.')
    if n>max_num:
        raise Exception(f'Number must be at least {max_num}.')

# Get values p and q
prompt_1='Give a prime number: '
p=int(pyip.inputCustom(is_prime,prompt=prompt_1))
q=int(pyip.inputCustom(is_prime,prompt=prompt_1))

# Get modulus and totient
modulus=p*q
t=euler.euler_totient(modulus,[p,q])

# Input validation
def is_coprime(n,t=t):
    '''Check if number is coprime to the totient function value.'''
    n=float(n)
    if n!=int(n):
        raise Exception('Number must be an integer.')
    n=int(n)
    g=np.gcd(n,t)
    if g!=1:
        raise Exception(f'Number must be coprime to {t}.')

# Get value e
prompt_2=f'Give a number coprime to {t}: '
e=int(pyip.inputCustom(is_coprime,prompt=prompt_2))

# Get multiplicative modular inverse
d=euler.modular_inverse(e,t)

# Get message to be encrypted
M=pyip.inputStr('Give a message to encrypt: ')

# Convert character to ascii values
def convert(char):
    conv=ord(char)
    return(conv)

# Encrypt message
enc_chars=[]
enc_message=''
for char in M:
    ascii_char=convert(char)
    enc_char=pow(ascii_char,e,modulus)
    enc_chars.append(enc_char)
    enc_message+=str(enc_char)

dec_message=''
for enc_char in enc_chars:
    enc_char=int(enc_char)
    dec_char=chr(pow(enc_char,d,modulus))
    dec_message+=dec_char

# Form keys
private_key=(d,modulus)
public_key=(e,modulus)

# Print information
print(f'Encrypted Message: {enc_message}')
print(f'Decrypted Message: {dec_message}')
print(f'Public Key Pair: {public_key}')
print(f'Private Key Pair: {private_key}')

# Ending Note
print('Program Ends')