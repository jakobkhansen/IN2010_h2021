# Kattis

Kattis er en nettside der du kan løse mange algoritmiske og logiske problemer der
algoritmer og datastrukturer er helt sentralt for å få til oppgavene. For å virkelig bli
god i IN2010 er du nødt til å kunne anvende pensumet slik at du kan avgjøre hvilke
algoritmer og/eller datastrukturer du trenger for å løse et problem, og det er akkurat
dette som Kattis utfordrer deg på.

### Løse din første oppgave

Oppgavene fungerer slik at du får en oppgavebeskrivelse om et eller annet problem som skal
løses.  Oppgaven skal da løses slik at programmet ditt leser inn noen linjer fra standard
input ([Java](https://www.geeksforgeeks.org/ways-to-read-input-from-console-in-java/),
[Python](https://www.geeksforgeeks.org/take-input-from-stdin-in-python/)), som er det
samme som å lese inn via en `Scanner` i Java, eller `input()` i Python.  Det du leser inn
er det som oppgaven beskriver, og du skal ut ifra denne inputten løse problemet beskrevet
i oppgaven og skrive ut svaret ditt til standard output (`System.out.println()` i Java
eller `print()` i Python).

##### Soda Slurper

La oss prøve å løse oppgaven [Soda Slurper](https://open.kattis.com/problems/sodaslurper).
Oppgaven går ut på at en person har lyst til å drikke så mye brus som mulig på en dag ved
å pante tomflasker, kjøpe brus og drikke de, og så bruke panten igjen. Du skal regne ut
hvor mange flasker denne personen klarer å drikke, gitt at personen har `e` tomflasker fra
før, finner `f` tomflasker i løpet av dagen og en brus koster `c` tomflasker i pant.
`e,f,c` er tall som du leser inn fra terminalen.

Prøv å løs denne oppgaven selv, du kan se formatet og noen eksempler på riktig output for
en gitt input på Kattis-linken. [Her](kodeskall/) finner du et kodeskall for Python og
Java som du kan bruke som et utgangspunkt. Alt som skjer i denne koden er at alle linjer
blir lest inn fra standard input inn i et array som du så kan bruke til å løse oppgaven i
`solution` metoden. Du kan for eksempel hente første linje ved å gjøre `lines[0]`

Hvis du sitter helt fast eller sliter med input/output, se løsningen her:
[Java](kattis/oppgaver/SodaSlurper.java), [Python](kattis/oppgaver/SodaSlurper.py)

##### Teste koden din

For å teste koden din er du nødt til å sende inn en fil som input til kommandolinjen.
Dette kan gjøres i terminal slik `java Program < inputfil.txt` der `inputfil.txt` inneholder
for eksempel `9 0 3` som i "Soda Slurper" oppgaven. (Du kan også laste ned alle
eksempelfilene fra Kattis under submit knappen!)

En annen måte å gjøre det på er å rett og slett skrive inn det som skal være input til
programmet etter at du har gjort `java Program`, problemet da er at programmet ikke
slutter å lese inn linjer før den får en "slutt på fil" (EOF) symbol. Da kan du på Linux
og Mac hvertfall trykke på `Ctrl + D` for å sende EOF, men dette er vanskeligere å få til
på Windows.

##### Sende inn koden

Når du har løst oppgaven og testet at du får riktig svar for "test-casene" under
beskrivelsen, kan du prøve å sende inn programmet ditt ved å trykke på submit og da vil
Kattis serveren kjøre programmet ditt med mange tester, som tester både at programmet ditt
gir riktig output, men også at programmet ditt er raskt nok. Noen løsninger kan være
korrekte, men ikke raske nok til å løse problemet effektivt, og dette skal du lære om i
IN2010!

### Oppgaver

Her er en liste med Kattis oppgaver som kan løses ved hjelp av pensumet i IN2010. Husk at
kategorien oppgaven er plassert i ikke nødvendigvis er den raskeste løsningen og det er
ofte flere måter å løse en oppgave på! Bruk vanskelighetsgraden på oppgaven som en
pekepinn, oppgaver som er 4+ vanskelighetsgrad begynner å bli ganske kompliserte!

##### Introduksjonsoppgaver

Her er først en liste med litt enklere problemer som ikke krever noe særlig av pensumet i
IN2010, men er ment for å introdusere deg til hvordan oppgavene på Kattis ser ut og få
løst noen oppgaver.

* [trik](https://open.kattis.com/problems/trik)
* [fizzbuzz](https://open.kattis.com/problems/fizzbuzz) - Veldig vanlig intervjuspørsmål

##### Binærsøk

* [guess](https://open.kattis.com/problems/guess) - Litt spesiell

##### Trær, binære søketrær, balanserte søketrær

* [boxes](https://open.kattis.com/problems/boxes) - Veldig bra!

##### Kø, stack, prioritetskø, heap

##### Grafer, Graftraversering, DFS/BFS
* [weak vertices](https://open.kattis.com/problems/weakvertices)
* [horror](https://open.kattis.com/problems/horror)

##### Topologisk sortering
* [pick up sticks](https://open.kattis.com/problems/pickupsticks)
* [build dependencies](https://open.kattis.com/problems/builddeps) - Ganske krevende

##### Shortest path, Dijkstra's algoritme med mer

##### Spenntrær

##### Sterkt sammenhengende komponenter

##### Sortering

* [DA-sort](https://open.kattis.com/problems/dasort)
