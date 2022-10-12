
print(" ".isspace()) #mellanslag is space
print("\t".isspace()) #även tabbar räknas som space
print("\n".isspace())  #newline är räknas också som space

sträng = "Åke\n\t Bjerregaard"
print(sträng)
print("Åke\n\t Bjerregaard".isspace()) 

print(sträng.find("Bje")) #returnera index