import hashlib 


def generate_sha1(string):

    result = hashlib.sha1(string.encode())

    return result.hexdigest()