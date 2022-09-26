

def kan_ta_olika_typer(argument):
    if isinstance(argument, str):
        print(f'Detta är en sträng med värdet:{argument}.')
    if isinstance(argument, int):
        print(f'Detta är ett heltal med värdet:{argument}.')
    if isinstance(argument, float):
        print(f'Detta är ett flyttal med värdet:{argument}.')
    if isinstance(argument, bool):
        print(f'Detta är en boolean med värdet:{argument}.')

kan_ta_olika_typer(True)
print(type(True))


variabelnamn = 10
print(type(str(variabelnamn)))



# print(kan_ta_olika_typer("hejsan"))
# print(kan_ta_olika_typer(5))
# print(kan_ta_olika_typer(0.524))

# def skriv_ut_hej():
#     print("Hej")

# skriv_ut_hej()
# skriv_ut_hej()

# def sätt_ihop_två_strängar(argument1, argument2):
# 	print(f"{argument1}{argument2}")
	
# sätt_ihop_två_strängar("FörstaArgumentet", "AndraArgumentet")

# def trippel_addition(tal1, tal2, tal3):
# 	return tal1 + tal2 + tal3
 
# resultat = trippel_addition(6, 9, 100)
# print(resultat)




# h = blake2b()
# h.update(b'Hello world')
# string = h.hexdigest()
# print(string)
# print(hash_three_arguments("Åke","Bjerregaard", "1234"))
# print(hash_three_arguments("Åke","Bjerregaard", "1235"))