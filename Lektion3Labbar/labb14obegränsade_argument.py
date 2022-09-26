def obegränsat_antal_argument(*args):
    for argument in args:
        print(argument)

obegränsat_antal_argument()

obegränsat_antal_argument(1, 2, 3)

obegränsat_antal_argument(1, 2, 3, "sdf", True, False, 0.521)