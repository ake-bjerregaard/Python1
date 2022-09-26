def blandat_med_default_argument(måste_anges, måste_också_anges, måste_inte_anges = "default", måste_inte_heller_anges = 5):
    print(måste_anges)
    print(måste_också_anges)
    print(måste_inte_anges)
    print(måste_inte_heller_anges)

blandat_med_default_argument("Åke", "Bjerregaard")
print("-------")
blandat_med_default_argument("Åke", "Bjerregaard", "ej default")
print("-------")
blandat_med_default_argument("Åke", "Bjerregaard", "ej default", "sista argumentet")