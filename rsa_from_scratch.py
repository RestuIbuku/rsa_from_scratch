import random

# 1. Fungsi mencari Faktor Persekutuan Terbesar (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 2. Algoritma Extended Euclidean untuk mencari Invers Modular (menemukan kunci d)
def mod_inverse(e, phi):
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        r_old, r_new = r_new, r_old - quotient * r_new
        d_old, d_new = d_new, d_old - quotient * d_new
    if r_old > 1:
        return None # Invers tidak ada
    if d_old < 0:
        d_old += phi
    return d_old

# 3. Fungsi sederhana memeriksa bilangan prima
def is_prime(num):
    if num <= 1: return False
    if num <= 3: return True
    if num % 2 == 0 or num % 3 == 0: return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# 4. Fungsi Pembangkitan Kunci (Key Generation)
def generate_keypair(min_val=100, max_val=1000):
    # a. Cari dua bilangan prima acak p dan q
    p = random.randint(min_val, max_val)
    while not is_prime(p):
        p = random.randint(min_val, max_val)
        
    q = random.randint(min_val, max_val)
    while not is_prime(q) or q == p:
        q = random.randint(min_val, max_val)
        
    # b. Hitung n = p * q
    n = p * q
    
    # c. Hitung phi(n)
    phi = (p - 1) * (q - 1)
    
    # d. Pilih e yang coprime dengan phi(n)
    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
        
    # e. Hitung d (private key)
    d = mod_inverse(e, phi)
    
    # Return Public Key (e, n) dan Private Key (d, n)
    return ((e, n), (d, n))

# 5. Proses Enkripsi
def encrypt(public_key, plaintext):
    e, n = public_key
    # Ubah tiap karakter ke representasi ASCII (ord), lalu pangkatkan dengan e modulo n
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# 6. Proses Dekripsi
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Pangkatkan ciphertext dengan d modulo n, lalu kembalikan ke karakter ASCII (chr)
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

# ==========================================
# DEMONSTRASI (Screen Record bagian ini saat jalan)
# ==========================================
if __name__ == '__main__':
    print("=== Demo RSA Dari Awal (From Scratch) ===")
    print("Membangkitkan pasangan kunci RSA...")
    
    # Generate kunci
    public_key, private_key = generate_keypair()
    print(f"Public Key  (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    # Input pesan
    message = input("\nMasukkan pesan yang ingin dienkripsi: ")
    print(f"Pesan asli (Plaintext): {message}")
    
    # Enkripsi
    encrypted_msg = encrypt(public_key, message)
    print(f"Pesan tersandi (Ciphertext): {encrypted_msg}")
    
    # Dekripsi
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"Pesan dikembalikan (Decrypted Plaintext): {decrypted_msg}")