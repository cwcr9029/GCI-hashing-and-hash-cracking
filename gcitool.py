import hashlib

while True:

    option = int(input("Enter 1 to hash, 2 to crack, 3 to exit: "))

    if option == 1:
        hash_type = int(input("1. md5\n2. sha1\n3. sha224\n4. sha256\n5. sha384\n6. sha512\nEnter the number of the hash:"))
        
        word = input("Enter the word to be hashed: ")

        if hash_type == 1: 
            h = hashlib.md5()
            
        elif hash_type == 2: 
            h = hashlib.sha1()
        
        elif hash_type == 3:
            h = hashlib.sha224()
        
        elif hash_type == 4: 
            h = hashlib.sha256()
        
        elif hash_type == 5: 
            h = hashlib.sha384()

        elif hash_type == 6: 
            h = hashlib.sha512()
        h.update(word.encode())
        print(h.hexdigest())
            
    elif option == 2:
        _hash = input("Enter the hash: " )
        filename = input("Please enter the file name of the password list: ")
        wordlist = []
        found = False
        with open(filename,encoding="utf-8") as f:
            for i in f.readlines():
                words = i.strip().split()
                wordlist.extend(words)

        for i in wordlist:
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            sha224 = hashlib.sha224()
            sha256 = hashlib.sha256()
            sha384 = hashlib.sha384()
            sha512 = hashlib.sha512()
        
            md5.update(i.encode())
            sha1.update(i.encode())
            sha224.update(i.encode())
            sha256.update(i.encode())
            sha384.update(i.encode())
            sha512.update(i.encode())

            if md5.hexdigest() == _hash or sha1.hexdigest() == _hash \
            or sha224.hexdigest() == _hash or sha256.hexdigest() == _hash \
            or sha384.hexdigest() == _hash or sha512.hexdigest() == _hash:
                found = True
                print("found {} = {}".format(_hash,i))
                break
        
        if not found:
            print("Cannot be found")
    
    elif option == 3:
        break