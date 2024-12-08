def ikki_likdan_onniga(ikkilik_son):
    onlik_son = 0
    daraja = 0
    for raqam in reversed(ikkilik_son):
        if raqam == '1':
            onlik_son += 2 ** daraja
        daraja += 1
    return onlik_son
ikkilik_son = input("Ikkilik sonni kiriting: ")
onnilik_son = ikki_likdan_onniga(ikkilik_son)
print(f"{ikkilik_son} 2-lik soni {onnilik_son} 10-lik soniga teng.")