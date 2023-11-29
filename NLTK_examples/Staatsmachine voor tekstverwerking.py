# Een state machine gaat over het ontwerpen van een programma om de stroom in een applicatie te controleren.
# het is een gerichte graaf, bestaande uit een reeks knooppunten en een reeks overgangsfuncties.
# Het verwerken van een tekstbestand bestaat vaak uit het opeenvolgend lezen van elk deel van een tekstbestand en het doen van iets als reactie op elk gelezen deel.
# De betekenis van een chunk hangt af van welke soorten chunks ervoor aanwezig waren en welke chunks erna komen.
# De machine gaat over het ontwerpen van een programma om de stroom in een applicatie te controleren. het is een gerichte graaf,
# bestaande uit een reeks knooppunten en een reeks overgangsfuncties.
# Het verwerken van een tekstbestand bestaat vaak uit het opeenvolgend lezen van elk deel van een tekstbestand en het doen van iets als reactie op elk gelezen deel.
# De betekenis van een chunk hangt af van welke soorten chunks ervoor aanwezig waren en welke chunks erna komen.

# Beschouw een scenario waarin de geplaatste tekst een continue reeks herhalingen van de reeks AGC moet zijn (gebruikt bij eiwitanalyse).
# Als deze specifieke volgorde in de invoerreeks wordt gehandhaafd, blijft de toestand van de machine WAAR, maar zodra de volgorde afwijkt,
# wordt de toestand van de machine ONWAAR en blijft daarna ONWAAR. Dit zorgt ervoor dat de verdere verwerking wordt gestopt,
# ook al zijn er later mogelijk meer delen van de juiste reeksen beschikbaar.

# Het onderstaande programma definieert een toestandsmachine die functies heeft om de machine te starten,
# invoer te nemen voor het verwerken van de tekst en de verwerking te doorlopen.


class StateMachine:

# Initialize 
    def start(self):
        self.state = self.startState

# Step through the input
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

# Loop through the input		
    def feeder(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

# Determine the TRUE or FALSE state
class TextSeq(StateMachine):
    startState = 0
    def getNextValues(self, state, inp):
        if state == 0 and inp == 'A':
            return (1, True)
        elif state == 1 and inp == 'G':
            return (2, True)
        elif state == 2 and inp == 'C':
            return (0, True)
        else:
            return (3, False)


InSeq = TextSeq()

x = InSeq.feeder(['A','A','A'])
print (x)

y = InSeq.feeder(['A', 'G', 'C', 'A', 'C', 'A', 'G'])
print (y)

