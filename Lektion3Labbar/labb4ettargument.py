def kan_ta_olika_typer(argument):
    if isinstance(argument, str):
        print(f'Detta är en sträng med värdet:{argument}.')
    elif isinstance(argument, bool):
        print(f'Detta är en boolean med värdet:{argument}.')
    elif isinstance(argument, int):
        print(f'Detta är ett heltal med värdet:{argument}.')
    elif isinstance(argument, float):
        print(f'Detta är ett flyttal med värdet:{argument}.')

kan_ta_olika_typer(True)
print("Sista raden")
