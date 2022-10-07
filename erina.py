dict={'saya' : 'kaji','kamu' : 'sia','mandi' : 'maneng','makan' : 'mangan','tidur' : 'tunung'}
artikan=input("Masukkan kata yang ingin di artikan: ")
if artikan=='saya':
    print(f"Saya : {dict['saya']}")
elif artikan=='kamu':
    print(f"Kamu : {dict['kamu']}")
elif artikan=='mandi':
    print(f"Mandi : {dict['mandi']}")
elif artikan=='makan':
    print(f"Makan : {dict['makan']}")
elif artikan=='tidur':
    print(f"Tidur : {dict['tidur']}")
else:
    print("INVALID")