class India():
    def captital(self):
            print ("New Dehli is capital of India")

    def language(self):
          print ("Hindi is the most spoken language in India")

    def type(self):
          print ("India is a developing country")

class USA():
    def captital(self):
        print ("Washington, DC is capital of USA")

    def language(self):
          print ("English is the spoken language in USA")

    def type(self):
          print ("USA is a developed country")

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
      country.captital()
      country.language()
      country.type()