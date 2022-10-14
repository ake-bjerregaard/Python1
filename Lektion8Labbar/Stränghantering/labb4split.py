#split delar strängen i flera strängar och returnerar en lista med stränger

en_mening = "Här är en mening som delas upp"
lista_med_ord = en_mening.split() #utan argument så används mellanslag för att splitta strängen

print(lista_med_ord)
print("Det här är antalet strängar i listan:", len(lista_med_ord))

en_mening_med_bindelsestreck = "Här-är-ord-separerade-med-bindelsestreck"
lista_med_ord = en_mening_med_bindelsestreck.split('-')
print(lista_med_ord)
print("Det här är antalet strängar i listan:", len(lista_med_ord))