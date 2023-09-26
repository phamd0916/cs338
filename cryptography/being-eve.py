"""
Doug Pham
being-eve.py

----- DIFFIE HELLMAN -----
How the code works is by using the equation A = g^a mod p and we know that g = 7, p = 61, and A = 30,
it runs through iterations of possible a values that satisfy this equation and the first number that 
satisfies it. It does the same for B = g^b mod p with B = 17 and the values we get from this are a = 41
and b = 23. To check that these two values work is by using these two equations: K = B^a mod p and K = A^b mod p
and by using the values we got, and if both K's are the same then we have successfully created the shared secret
which in this case we have and it is 6. 
If the beginning numbers were much larger, then we would fail in the searching for which a and b values match
because there are infinite combinations of a and b values that would work and since this code just finds the first pair
that satisfies the equation, it would not look to the other valid pairs, so that is where is method falls short.

"""
# Agreed upon g and p values
g = 7
p = 61

# Numbers set back and forth between Alice and Bob
A = 30
B = 17

a = 1
# Loop until we find a that satisfies the equation
while True:
    if (A == (g ** a) % p):
        break
    a += 1

print("First 'a' that satisfies this equation: ", a)

# Equation to determine shared secret for Alice
aKey = (B**a) % p
print("Shared secret: ", aKey)


b = 1
# Loop until we find b that satisfies the equation
while True:
    if (B == (g ** b) % p):
        break
    b += 1

print("First 'b' that satisfies this equation: ", b)

# Equation to deterine shared secret for Bob
bKey = (A ** b) % p
print("Shared secret: ", bKey)


""""
----- RSA -----
Here is the encrypted message: 
Hi Bob. I'm walking from now on. Your pal, Alice. https://foundation.mozilla.org/en/privacynotincluded/articles/its-official-cars-are-the-worst-product-category-we-have-ever-reviewed-for-privacy/
First how the message was encoded was by taking the ASCII value of each character in the original message, x, and
computing x^eB mod nB which Alice has because those are Bob's public key. This gives us the encoded message which
is stored in the data variable. Now to decrypt the message we use the same equation execpt we are solving for what
x is and we know that equations equals whichever encoded item we are decoding. So for the first message our equation
would look like 65426 = x^17 mod 170171. Now to solve for x, we try all values of x incrementing by 1 until we have
a valid solution. This is where this method would fail if we had larger integers because then there would be multiple
possible solutions that satisfy this equations and so using the first solution would not work which would occur in the
while loop. This then would make Alice's encoding insecure if Bob's keys had larger integers because with larger keys
it would take much more computing time to decode having to iterate through all possibilities of what fits in the equation.
Once we have an x that satisfies the equations, we have to split x up into two parts which are 1 byte each so that we
can convert it into ASCII. Using some bitwise operations we can accomplish this and then we append both of these bytes
into our list which we then print after getting through Alice's encrypted message.
I also decrypted this message by finding p and q which was 379 and 449 since they are both prime and multiply to get the
n we were given which was 170171and used the equation lambda(nB) = lcm(p - 1)(q - 1) and got 12096 and similarly using
code found dB using the equation eB*dB mod lambda(nB) = 1. Once I determined what dB was then I could use the equation 
c^d mod n to determine the original message with a process similar to described above with taking the decrypted blocks
and converting it to ASCII
"""
# ------ RSA --------

# Bob's public key
e = 17
n = 170171

# Alice's encrypted message to Bob
data = [65426, 79042, 53889, 42039, 49636, 66493, 41225, 58964,
126715, 67136, 146654, 30668, 159166, 75253, 123703, 138090,
118085, 120912, 117757, 145306, 10450, 135932, 152073, 141695,
42039, 137851, 44057, 16497, 100682, 12397, 92727, 127363,
146760, 5303, 98195, 26070, 110936, 115638, 105827, 152109,
79912, 74036, 26139, 64501, 71977, 128923, 106333, 126715,
111017, 165562, 157545, 149327, 60143, 117253, 21997, 135322,
19408, 36348, 103851, 139973, 35671, 93761, 11423, 41336,
36348, 41336, 156366, 140818, 156366, 93166, 128570, 19681,
26139, 39292, 114290, 19681, 149668, 70117, 163780, 73933,
154421, 156366, 126548, 87726, 41418, 87726, 3486, 151413,
26421, 99611, 157545, 101582, 100345, 60758, 92790, 13012,
100704, 107995]


decoded_data = []
# Loop through every item in data
for num in data:
    x = 1
    # Loop until we get an x that satisfies this equation
    while True:
        if (num == (x ** e) % n):
            break
        x += 1

    # Since ASCII is stored in 2-byte blocks, we have to separate each byte to get ASCII character
    left = x >> 8
    right = x & 0b000000011111111
    decoded_data.append(chr(left))
    decoded_data.append(chr(right))

# Print out decoded message
print("Message: ")
for ch in decoded_data:
    print(ch, end="")
