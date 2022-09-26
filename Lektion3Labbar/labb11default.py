from xml.dom.pulldom import START_DOCUMENT


def ett_default_argument(arg1 = 42):
    print(arg1)

ett_default_argument()

ett_default_argument(2022)

ett_default_argument("Hello!")