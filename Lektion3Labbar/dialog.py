

def fråga(info_text, text1, text2, text3, text4, rätt_svar):
    print(info_text)
    print("1", text1)
    print("2", text2)
    print("3", text3)
    print("4", text4)
    print("Skriv rätt svar:")
    svar = int(input())
    if(rätt_svar == svar):
        print("rätt")
    else:
        print("fel")

fråga("Vad heter skaparen av python?", "Guido von Rossum", "Peter Stormare", "Kalle Anka", "Robert Aschberg", 1)
fråga("Vad heter Meriams mamma?", "Sara", "Simone", "Kalle Anka", "Sofia", 4)