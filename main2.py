class Regex:
    def __init__(self, litera=None, iterator=None):
        self.graf = []
        self.stare_finala = None
        if litera is None and iterator is None:
            self.graf = [["q0", "§", "q1"]]
            self.stare_finala = "q1"
            self.iterator = 1
        elif litera == "§":
            self.graf = [["q0", "§", "q0"]]
            self.stare_finala = "q0"
            self.iterator = 0
        else:
            nod = "q" + str(iterator)
            nod1 = "q" + str(iterator + 1)
            self.graf = [[nod, litera, nod1]]
            self.stare_finala = nod1
            self.iterator = iterator + 1

    def afis(self):
        print("Graf:")
        for tranzitie in self.graf:
            print(tranzitie)
        print("Stare finala:", self.stare_finala)


def concatenare(stiva, r1, r2):
    graf1 = r1.graf
    stare_finala1 = r1.stare_finala
    iterator1 = r1.iterator
    graf2 = r2.graf
    stare_finala2 = r2.stare_finala
    iterator2 = r2.iterator

    graf1.append([stare_finala1, "§", graf2[0][0]])
    graf = graf1 + graf2[1:]
    stare_finala = stare_finala2
    stiva.append(Regex(iterator=iterator2, litera=None))
    stiva[-1].graf = graf
    stiva[-1].stare_finala = stare_finala


def reuniune(stiva, r1, r2):
    graf1 = r1.graf
    stare_finala1 = r1.stare_finala
    iterator1 = r1.iterator
    graf2 = r2.graf
    stare_finala2 = r2.stare_finala
    iterator2 = r2.iterator

    nod1 = "q" + str(iterator1)
    nod2 = "q" + str(iterator2 + iterator1)
    graf1.append(["q0", "§", nod1])
    graf2.append(["q0", "§", nod1])
    graf1.append([stare_finala1, "§", nod2])
    graf2.append([stare_finala2, "§", nod2])
    graf = graf1 + graf2[1:]
    stare_finala = nod2
    stiva.append(Regex(iterator=iterator2 + iterator1, litera=None))
    stiva[-1].graf = graf
    stiva[-1].stare_finala = stare_finala


def stelare(stiva, r):
    graf = r.graf
    stare_finala = r.stare_finala
    iterator = r.iterator

    graf.append([stare_finala, "§", "q1"])
    iterator += 1
    nod = "q" + str(iterator)
    graf.append(["q0", "§", nod])
    graf.append([stare_finala, "§", nod])
    stare_finala = nod
    stiva.append(Regex(iterator=iterator, litera=None))
    stiva[-1].graf = graf
    stiva[-1].stare_finala = stare_finala


def converteste_in_delta_nfa(regex):
    stiva = []
    stiva_operatori = []

    for caracter in regex:
        if caracter == "(":
            stiva_operatori.append(caracter)
        elif caracter == ")":
            while stiva_operatori[-1] != "(":
                operator = stiva_operatori.pop()
                if operator == "*":
                    stelare(stiva, stiva.pop())
                elif operator == "+":
                    r2 = stiva.pop()
                    r1 = stiva.pop()
                    reuniune(stiva, r1, r2)
                elif operator == ".":
                    r2 = stiva.pop()
                    r1 = stiva.pop()
                    concatenare(stiva, r1, r2)
            stiva_operatori.pop()
        elif caracter in "*+.":
            stiva_operatori.append(caracter)
        else:
            stiva.append(Regex(litera=caracter, iterator=len(stiva)))

    while stiva_operatori:
        operator = stiva_operatori.pop()
        if operator == "*":
            stelare(stiva, stiva.pop())
        elif operator == "+":
            r2 = stiva.pop()
            r1 = stiva.pop()
            reuniune(stiva, r1, r2)
        elif operator == ".":
            r2 = stiva.pop()
            r1 = stiva.pop()
            concatenare(stiva, r1, r2)

    return stiva[0].graf, stiva[0].stare_finala


regex = "(a+b)*.c"
graf, stare_finala = converteste_in_delta_nfa(regex)
r = Regex()
r.graf = graf
r.stare_finala = stare_finala
r.afis()
