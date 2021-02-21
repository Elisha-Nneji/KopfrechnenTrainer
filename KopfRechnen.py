import random
import time
import sqlite3
from datetime import date

#Zeit richtig zeigen
def timePrint(sec):
    mins = sec // 60
    ms = sec * 10
    ms = ms % 10
    sec = sec % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(mins),int(sec),int(ms)))

#Initialisieren und Deklaieren
richtige = 0
richtige2 = 0
anzLeichteAufgaben = 10
anzSchwereAufgaben = 5

name = input("Name: ")

startTime = time.time()

#einfache Aufgaben
for i in range(anzLeichteAufgaben):
    randInt1 = random.randrange(11,100)
    randInt2 = random.randrange(2, 11)
    ergebniss = randInt1 * randInt2
    eingabe = int(input(str(randInt1) + " * " + str(randInt2) + " = "))
    if ergebniss == eingabe:
        richtige += 1
    else:
        print("falsch.. Richtige Antwort: " + str(ergebniss))

#schwere Aufgaben
for i in range(anzSchwereAufgaben):
    randInt1 = random.randrange(11,100)
    randInt2 = random.randrange(11,100)
    ergebniss = randInt1 * randInt2
    eingabe = int(input(str(randInt1) + " * " + str(randInt2) + " = "))
    if ergebniss == eingabe:
        richtige2 += 1
    else:
        print("falsch... Richtige Antwort: " + str(ergebniss))
        
richtigeProzent = richtige / anzLeichteAufgaben * 100
richtige2Prozent = richtige2 / anzSchwereAufgaben * 100

endTime = time.time()
totalTime = endTime - startTime
timePrint(totalTime)

#Output
print("Du hast " + str(richtigeProzent) + " % der einfachen Rechnungen und "
      + str(richtige2Prozent) + " % der schweren Aufgaben " +
      "richtig gerechnet")

#datum bekommen
datum = date.today()

#SQL-Table
conn = sqlite3.connect("MatheRechnung.db")
cur = conn.cursor()

#create and add to Table
cur.execute("CREATE TABLE IF NOT EXISTS matheHighscores(Name VARCHAR(50) ,EinfacheRechnungenQuote INT,"
            + " SchwereRechnungenQuote INT, Datum DATETIME, Zeit REAL)")

cur.execute("INSERT INTO matheHighscores (Name, EinfacheRechnungenQuote, SchwereRechnungenQuote, Datum, Zeit) VALUES (?,?,?,?,?)",
           (name,richtigeProzent,richtige2Prozent, datum, totalTime))

conn.commit()

#alles Schließen
cur.close()
conn.close()

print("Ergebnisse gespeichert")

