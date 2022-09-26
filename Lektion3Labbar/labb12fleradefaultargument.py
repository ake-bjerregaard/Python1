def flera_default_argument(arg1 = 5, arg2 = "hej", arg3 = 0.5):
    print("Argument 1 är: ", arg1)
    print("Argument 2 är: ", arg2)
    print("Argument 3 är: ", arg3)

flera_default_argument()
flera_default_argument(0.1)
flera_default_argument(0.1, "tjena")
flera_default_argument(0.1, "tjena", "nåt")
