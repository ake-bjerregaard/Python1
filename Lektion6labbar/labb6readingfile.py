import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("Os fel: {0}".format(err))
except ValueError:
    print("Kunde inte konvertera data till ett heltal")
except BaseException as err:
    print(f"Oväntat {err=}, {type(err)=}")
    raise

print("Talet var ", i)