import base64


# Encoding Function
def encode(key, txt):
    enc_list = []

    for i in range(len(txt)):
        key_c = key[i % len(key)]
        enc_list.append(chr((ord(txt[i]) + ord(key_c)) % 256))
    # encoding the text using base64.urlsafe_b64encode()
    return base64.urlsafe_b64encode("".join(enc_list).encode()).decode()


# Decoding Function
def decode(key, txt):
    dec_list = []
    # decoding the text using base64.urlsafe_b64decode()
    msg = base64.urlsafe_b64decode(txt).decode()

    for i in range(len(msg)):
        key_c = key[i % len(key)]
        dec_list.append(chr((256 + ord(msg[i]) - ord(key_c)) % 256))
    return "".join(dec_list)
