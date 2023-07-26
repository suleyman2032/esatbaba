meme_dict = {
            "LOL": "komik bir şeye verilen cevap",
            "CRINGE": "garip ya da utandırıcı bir şey",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("o kelimenin anlamı bu",meme_dict[word])
    
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("yanlış girdin")
