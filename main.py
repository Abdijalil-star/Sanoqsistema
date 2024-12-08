def ikki_likdan_onniga(ikkilik_son):
    onlik_son = 0
    daraja = 0
    for raqam in reversed(ikkilik_son):
        if raqam == '1':
            onlik_son += 2 ** daraja
        daraja += 1
    return onlik_son
def ikki_likdan_olti_onalik(ikkilik_son):
    onlik_son = ikki_likdan_onniga(ikkilik_son)
    if onlik_son == 0:
        return '0'
    heksadesimal_son = ''
    while onlik_son > 0:
        qolgan = onlik_son % 16
        if qolgan < 10:
            heksadesimal_son = str(qolgan) + heksadesimal_son
        else:
            heksadesimal_son = chr(ord('A') + qolgan - 10) + heksadesimal_son
        onlik_son //= 16
    return heksadesimal_son
ikkilik_son = input("Ikkilik sonni kiriting: ")
onnilik_son = ikki_likdan_onniga(ikkilik_son)
heksadesimal_son = ikki_likdan_olti_onalik(ikkilik_son)
print(f"{ikkilik_son} 2-lik soni {onnilik_son} 10-lik soniga teng.")
print(f"{ikkilik_son} 2-lik soni {heksadesimal_son} 16-lik soniga teng.")