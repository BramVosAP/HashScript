import sys
from passlib.hash import argon2

#Variabelen declareren
plaintextInput1 = input("Voer je wachtwoord in plaintext in: ");
hasher = PasswordHasher();

#Hash van het paswoord uitvoeren
hash1 = hasher.hash(plaintextInput1);
print("De encryptie van je wachtwoord is uitgevoerd.");
print("De hash van je wachtwoord is: " + hash1);

#Invoer van controlehash
plaintextInput2 = input("Voer je wachtwoord in plaintext in: ");
hashInput = input("Voer de hash van je wachtwoord in: ");

#Controleren of hash hetzelfde is
if plaintextInput2 == plaintextInput1:
     argon2.verify(hash1, hashInput);
else:
    print("Je wachtwoord en hash klomen niet overeen.");