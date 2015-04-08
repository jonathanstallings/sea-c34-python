import cipher


def test_encrypt_decrypt():
    message = u"this is totally a secret"
    cipher_text = cipher.encrypt(message)
    assert message == cipher.decrypt(cipher_text)

