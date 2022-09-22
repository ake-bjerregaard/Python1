
class Sign(object):
    arithmetic = False
    swedish = True

    def __init__(self, *args):
        self.sign = args[0]
        self.names_dict = args[1]
    
    def __key(self):
        # return (self.attr_a, self.attr_b, self.attr_c)
        return self.sign

    def __hash__(self):
        # return hash(self.__key())
        return hash(self.sign)

    def __eq__(self, other):
        if isinstance(other, Sign):
            return self.__key() == other.__key()
        elif(other is str):
            return self.__key() == other.__key()
        return NotImplemented
        
    def __str__(self):
        if(Sign.arithmetic):
            if(Sign.swedish):
                if(self.names_dict.has_key("sv_arithmetic")):
                    return self.names_dict["sv_arithmetic"][0]
            elif(self.names_dict.has_key("en_arithmetic")):
                return self.names_dict["en_arithmetic"][0]
        if(Sign.swedish):
            return self.names_dict["svenska"][0]
        else:
            return self.names_dict["english"][0]
        # return "foo"
    
    def full_info(self):
        return ""

def programming_signs():
    
    signs = [
    Sign("+", 
    {"svenska" : ["plustecken"], 
    "english" : ["plus sign"],
    "sv_arithmetic" : ["addition", "plus", "adderat med"],
    "en_arithmetic" : ["addition", "plus", "add"]
    }
    ),
    

    Sign("-", 
    {"svenska" : ["bindelsestreck", "divis"], 
    "english" : ["dash", "hyphen"],
    "sv_arithmetic" : ["subtraktion, minus"],
    "en_arithmetic" : ["subtraction, minus"]
    }
    ),
    
    Sign("*", 
    {"svenska" : ["stjärna"], 
    "english" : ["star"],
    "sv_arithmetic" : ["multiplikation", "gånger"],
    "en_arithmetic" : ["multiplication", "times"],
    "modkey" : ["shift"]
    }
    ),

    Sign("/", 
    {"svenska" : ["snedstreck"], 
    "english" : ["slash"],
    "sv_arithmetic" : ["division", "delat", "delat med"],
    "en_arithmetic" : ["division", "divided", "divided by"],
    "modkey" : ["shift"]
    }
    ),
    

    
    Sign("\\", 
    {"svenska" : ["bakstreck", "omvänt snedstreck"], 
    "english" : ["backslash"],
    "modkey" : ["alt gr"]
    }
    ),
    
    # Round brackets
    Sign("(", 
    {"svenska" : ["startparantes"], 
    "english" : ["open paranthesis"],
    "modkey" : ["shift"],
    "pair-matched" : ")",
    "start" : True
    }
    ),
    
       
    Sign(")", 
    {"svenska" : ["slutparantes"], 
    "english" : ["close paranthesis"],
    "modkey" : ["shift"],
    "pair-matched" : "(",
    "end" : True
    }
    ),

    Sign("{", 
    {"svenska" : ["startmåsvinge", "startklammerparantes"], 
    "english" : ["open curly bracket"],
    "modkey" : ["alt gr"],
    "pair-matched" : "}",
    "start" : True
    }
    ),
    
    Sign("}", 
    {"svenska" : ["slutmåsvinge", "slutklammerparantes"], 
    "english" : ["close curly bracket"],
    "modkey" : ["alt gr"],
    "pair-matched" : "{",
    "end" : True
    }
    ),
    
    Sign("[", 
    {"svenska" : ["starthakparentes"], 
    "english" : ["open bracket"],
    "modkey" : ["alt gr"],
    "pair-matched" : "]",
    "start" : True
    }
    ),
    
    Sign("]", 
    {"svenska" : ["sluthakparentes"], 
    "english" : ["close bracket"],
    "modkey" : ["alt gr"],
    "pair-matched" : "[",
    "end" : True
    }
    ),
    
    Sign(":", 
    {"svenska" : ["kolon"], 
    "english" : ["colon"],
    "modkey" : ["shift"]
    }
    ),
    
    Sign(";", 
    {"svenska" : ["semikolon"], 
    "english" : ["semi-colon"],
    "modkey" : ["shift"]
    }
    ),
    
    Sign("'", 
    {"svenska" : ["apostrof"], 
    "english" : ["apostrophe"],
    "pair-matched" : "'",
    }
    ),
    
    Sign('"', 
    {"svenska" : ["citattecken"], 
    "english" : ["quotation marks"],
    "modkey" : ["shift"],
    "pair-matched" : '"',
    }
    ),
    
    Sign('.', 
    {"svenska" : ["punkt"], 
    "english" : ["dot"],
    
    }
    ),
    
    Sign(',', 
    {"svenska" : ["komma", "kommatecken"], 
    "english" : ["comma"],
    
    }
    ),
    
    Sign('=', 
    {"svenska" : ["likamed", "likamedtecken", "tilldelning"], 
    "english" : ["equals", "assignment"],
    "modkey" : ["shift"],
    }
    ),
    
    Sign('==', 
    {"svenska" : ["jämförelse"], 
    "english" : ["equivalence"],
    
    }
    ),
    
    Sign('>', 
    {"svenska" : ["större än"], 
    "english" : ["greater than", "larger than"],
    "modkey" : ["shift"],
    }
    ),
    
    Sign('<', 
    {"svenska" : ["mindre än"], 
    "english" : ["smaller than", "less than"],
    
    }
    ),
    
    Sign('>=', 
    {"svenska" : ["större eller likamed"], 
    "english" : ["greater than or equals", "larger than or equals"],
    
    }
    ),
    
    Sign('<=', 
    {"svenska" : ["mindre än eller likamed"], 
    "english" : ["smaller than or equals", "less than or equals"],
    
    }
    ),
    
    Sign('and', 
    {"svenska" : ["och", "boolskt och"], 
    "english" : ["and", "boolean and"],
    
    }
    ),
    
    Sign('or', 
    {"svenska" : ["eller", "boolskt eller"], 
    "english" : ["or", "boolean or"],
    
    }
    ),
    
    Sign('not', 
    {"svenska" : ["inte", "negation", "motsatsen", "ej"], 
    "english" : ["not", "negation", "opposite"],
    
    }
    ),
    

    
    ]
    
    # print(signs["\\"])
    signs2 = {}
    for sign in signs:
        signs2[sign.sign] = sign
        # print(signet.sign)
        # signs2["hello"] = 5
    
    return signs2
    

# signs = programming_signs()
# # print(someSign)
# # print(signs)

# for k, v in signs.items():
    # print(k, v)
# Sign.swedish = False
# for k, v in signs.items():
    # print(k, v)

# # citat = Sign()


# svenska_tecken_namn = {
# "\\": ["snedstreck", "delat", "division"]
# }



# class Sign(object):
  # # def __init__(self, **args):
  # def __init__(self, *args):
    # # sign = ""
    # self.sign = args[0]
    # self.names_dict = args[1]
    # # if(args.has_key("sign")):
       # # sign = args["sign"]
    
    # # mysillyobject.name = name
    # # mysillyobject.age = age