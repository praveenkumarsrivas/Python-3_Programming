class Praveen():
    names_list = []

    def __init__(self, name):
        self.name = name
        self.names_list.append(self.name)

    def show(self):
        print(self.names_list)


p = Praveen('pks')
p = Praveen('kumar')
p = Praveen('srivas')
p = Praveen('palera')
p.show()
