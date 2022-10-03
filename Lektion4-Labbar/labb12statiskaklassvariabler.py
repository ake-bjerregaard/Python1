class StatisktExempel:
    variabel = "Hej"
    
    def __init__(self, argument1):
        self.en_annan_variabel = argument1


print(StatisktExempel.variabel)

enInstans = StatisktExempel("instans variabel")
enInstans.variabel = "då"

print(StatisktExempel.variabel)
print(enInstans.variabel)


print(enInstans.en_annan_variabel)