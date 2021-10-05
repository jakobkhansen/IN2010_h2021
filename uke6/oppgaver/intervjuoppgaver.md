# Intervju oppgaver

På en del utviklerfirmaer er det vanlig å ha kodetester og kodespørsmål som en del av et teknisk intervju. Da kan man få spørsmål om å lage et system, sette opp en arkitektur, og spesielt ofte får man problemløsningsoppgaver der algoritmer og datastrukturer er viktig. Her er en liste med intervjuspørsmål som jeg har vært borti. Merk at ikke alle disse er direkte knyttet opp mot pensum i IN2010, men at de er relevante med tanke på å løse problemer med bruk av algoritmer og algoritmedesign.

Du kan finne veldig mange slike korte oppgaver som er rettet mot intervjuer her: https://leetcode.com/

Tekstlig løsningsforslag finner du under hver oppgave, kodeimplementasjon av de fleste oppgavene finner du [her](../losninger/intervjuoppgaver.py)

### Strenger

#### Streng-permutasjoner

Lag en algoritme som tar inn to strenger og sjekker om de er permutasjoner av hverandre. En permutasjon av en streng er en omstokking av de samme bokstavene. Metoden skal returnere true/false.

Eksempler:


```
"test", "tset" => true
"hello", "goodbye" => false
"algorithm", "logarithm" => true
"data", "dat" => true
"something", "" => false
"", "" => true
```

Hva er kompleksiteten på løsningen din?

<details>
    <summary>Løsningsforslag</summary>

    En ganske enkel måte å løse dette på er å "sortere" begge strenger alfabetisk og så sammenlikne de strengene. 
    Det vil være en O(n log n) løsning der n er lengden på strengene. 
    Dette er en ganske god løsning og ville absolutt vært god nok, men vi kan gjøre dette litt bedre.
    
    Lag en dictionary/HashMap som skal telle bokstaver. Nøkkel er bokstav, verdi er antall ganger vi har sett den bokstaven. 
    Loop over hver bokstav i den første strengen og tell opp bokstaver. Loop så over den andre strengen og tell ned bokstaver.
    Hvis du sitter igjen med en dictionary/hashmap der verdiene til alle nøkler er 0, så er dette en permutasjon. 
    Hvis du har positive verdier så betyr det at det finnes bokstaver i 
    den første strengen som ikke finnes i den andre, og hvis du har negative verdier er det motsatt.

    Dette er en O(n) løsning der n er lengden på strengene.
</details>

#### Dokument-søk

##### Del 1

Gitt et dokument (lang streng) og et søkeord (kortere streng), lag en algoritme som teller antall ganger søkeordet forekommer i dokumentet.  Prøv å ikke bruk for mange "snarveier" som du finner i Python. Anta for eksempel at du bare kan sammenlikne en og en bokstav, ikke hele ord.

Eksempler:
```
"This is a very very long document", "very" => 2
"Hello World Goodbye World", "Hello" => 1
"Not a long document", "very" => 0
```

Hva er kompleksiteten på løsningen din? La oss si at dokument-lengden er `n` og søkeord-lengden er `m`. Merk at hvis man gjør `"Ord" == "Ord"` så er det en `O(m)` operasjon der hver bokstav sammenliknes

<details>
    <summary>Løsningsforslag</summary>

    Dette er et ganske kjent problem innenfor informatikk. Det finnes mange gode algoritmer for å løse dette problemet, 
    som for eksempel Knut-Morris-Pratt, Boyer-Moore-Horspool, og flere, men disse er utenfor skopet av dette kurset.

    Vi skal implementere en enkel `brute-force` metode som sjekker på enhver indeks i dokumentet om det er starten på ordet vi leter etter.
    Vi begynner å sammenlikne fra indeks 0 i søkeordet og hvis vi kommer helt til slutten uten å finne en bokstav 
    som ikke matcher med søkeordet, så har vi funnet ordet i teksten. 
    Merk at vi kan og burde stoppe å lete når vi er på slutten av dokumentet, 
    der ordet vi leter etter er for langt til å ha plass i de resterende bokstavene.

    Denne algoritmen er en dobbel for-løkke der den ytterste løkka går over hele dokumentet (minus lengden på søkeordet) og 
    den innerste løkka går fra punktet der den ytterste for-løkka er, og går lengden av ordet fremover. 
    Se for deg at dette er et slags "vindu" på størrelsen av søkeordet, som vi forskyver en plass bortover i
    hver iterasjon av den ytterste løkka.

    Kompleksiteten på dette blir O(n*m) der n er lengden på dokumentet og m er lengden på søkeordet.
</details>

##### Del 2

Du vil nå optimisere dette slik at du bare trenger å se gjennom dokumentet en gang, og så hente ut antallet for et tilfeldig ord uten å måte lete gjennom dokumentet en gang til. Ideen er da at man har lyst til å prosessere dokumentet bare 1 gang, men hente ut antallet til mange forskjellige ord etterpå. Hvordan skal du få til dette?

Tips: Å sette inn og hente ut fra en dictionary/HashMap er i `O(1)` kjøretid.

<details>
    <summary>Løsningsforslag</summary>

    Vi har altså lyst til å bygge opp en "cache" av ord forekomster, som vi kan bruke senere når vi trenger å vite hvor mange ganger et visst ord forekommer.
    Dette er ikke vanskeligere enn å telle alle forekomster av et ord i en dictionary/HashMap. Når vi har gjort det så kan vi hente antall forekomster av
    et ord i O(1) tid.

    En litt kul og bedre datastruktur man kunne ha brukt for dette er en Trie, den lagrer en samling av ord veldig effektivt med tanke på minne,
    da ord som har samme prefiks (starter med samme bokstaver) blir "slått sammen". Interessant, men ikke del av pensum :)
</details>

#### Bygge lang streng

I denne oppgaven skal vi bygge lange strenger som følger noen regler. Gitt at du har et visst antall 'A', 'B' og 'C' bokstaver, hva er den lengste strengen du kan bygge uten å repetere samme bokstav mer enn 2 ganger? Input er 3 integers, som definerer hvor mange 'A', 'B' og 'C' du har tilgjengelig.

Eksempler:
```
1,2,3 => 'cabccb'
3,3,3 => 'abbcaabcc'
1,1,99 => 'ccaccbcc'
5,5,0 => 'ababababab'
```

Her er det også ofte flere gyldige løsninger for samme input. Kompleksitet er ikke viktig på denne oppgaven, korrekthet er viktigere.

<details>
    <summary>Løsningsforslag</summary>

    Vi ønsker åpenbart å bygge så lang streng som mulig, og for å få til det er vi nødt til å holde mulighetene våre åpne. 
    Derfor er vi nødt til å alltid velge den bokstaven vi har mest av som vi har lov til å bruke. 

    En løsning blir da som følger: 
    Hold styr på hvor mange bokstaver du har igjen å bruke, samt hvor mange ganger en bokstav har blitt brukt på rad.
    Filtrer ut de bokstavene du ikke har lov til å bruke (2 ganger på rad før eller 0 igjen) 
    og velg den bokstaven du har flest av igjen av disse.
    Fortsett sånn til det ikke er noen bokstaver du har lov å bruke, da har du den lengste strengen som er mulig å bygge.
</details>


### Arrayer


##### Null-sum array
Gitt et tall N, lag en algoritme som returnerer en liste med N unike elementer, som summerer til 0. `0 <= N <= 100`, alle elementer E i arrayet skal være `-100 <= E <= 100`.

Eksempler:

```
N = 3 => [2,3,-5]
N = 5 => [2, 3, -4, 6, -7]
N = 1 => [0]
N = 2 => [10, -10]

```

Her er det veldig mange korrekte svar for de fleste inputs.

<details>
    <summary>Løsningsforslag</summary>

    Det er en ganske enkel løsning på denne, men det krever noe kreativ-tenkning. 
    Vi ønsker å annullere alle positive tall med et negativt tall og vi vet jo alltid at i-i = 0. 
    Derfor kan du legge til først 1 og -1, så 2 og -2 osv. Hvis N er oddetall kan vi legge til 0 først.
</details>


##### Two-sum to N

Gitt et array og et tall N, finn to elementer i listen som summerer til N og returner indeksen. Det er garantert at det finnes minst et par i arrayet som summerer til N. Du kan ikke bruke samme indeks to ganger, men samme tall hvis tallet forekommer to ganger i listen.
Prøv å lag en algoritme som løser dette i lineær-tid.

Eksempler:

```
[1,2,3], 5 => 1,2 (elementene på indeks 1 og 2 summerer til 5)
[5, 10, 11, 3, 5, -2, 3], 1 => 3,5 (-2 + 3 = 1), 5,6 også gyldig
[1, 1], 2 => 0,1
[4, 11, 21, 15, 6], 21 => 3,4 (15 + 6 = 21)
```

<details>
    <summary>Løsningsforslag</summary>

    Hvis vi lagrer hvert tall vi har sett tidligere i en dictionary/HashMap er det lett å finne tilbake til om vi har sett et tall eller ikke før. 
    Når vi da kommer til et tall kan vi sjekke i denne om det er dette tallet vi trenger for å summere til N sammen med tallet vi nå ser på.
    Altså når vi ser på tallet i kan vi se om vi har sett N-i tidligere, siden det er tallet vi trenger å summere i med for å få N.
</details>

### Spesiell oppgave

##### Finn punkt med satellitt

Se for deg et kart som viser et område. Du leter etter et spesifikt punkt på dette kartet og er nødt til å bruke en sattelitt for å finne det. Sattelitten har et veldig primitivt interface og du kan kun spørre den om en ting: Gitt et område (delområde av kartet) er punktet innenfor dette området? Sattelitten kan bare svare ja eller nei hvis området er for stort, men kan gi deg eksakte koordinater dersom området er lite nok.

Eksempel:

```
|-----------------|
|                 |
|                 |
|                 |
|                 |
|  x              |
|                 |
|-----------------|

Dette er kartet, og x er punktet vi leter etter. Hvis vi gjør følgende spørring på satellitten:


|-----------------|
|                 |
|     |---|       |
|     |   |       |
|     |---|       |
|  x              |
|                 |
|-----------------|

Vil vi få tilbake false, siden punktet ikke er innenfor området.


Hvis vi gjør denne spørringen:

|-----------------|
|                 |
||----------|     |
||          |     |
||          |     |
|| x        |     |
||----------|     |
|-----------------|

Vil vi få tilbake true, siden punktet innenfor området, men vi vil ikke få selve koordinatene, 
siden området er ganske stort.


Hvis vi gjør denne spørringen:

|-----------------|
|                 |
|                 |
|                 |
||----|           |
|| x  |           |
||----|           |
|-----------------|

Vil vi få tilbake eksakte koordinater til punktet, siden området er lite nok. 
Det er dette vi til slutt har lyst til å få.
```

Oppgaven er altså: Design en algoritme (ikke implementer) som vil finne punktet med så få spørringer som mulig.
Du kan anta at du vet hvor stort kartet er (bredde, høyde) og hvor lite området må være (areal?) før du får eksakte koordinater av sattelitten

<details>
    <summary>Løsningsforslag</summary>

    Ideen her er at vi burde gjøre et slags 2D binærsøk.

    Vi starter med å sjekke halvparten av området:

    
    |-----------------|
    |        |        |
    |        |        |
    |        |        |
    |        |        |
    |  x     |        |
    |        |        |
    |-----------------|

    Uansett hvilken side vi sjekker her får vi vite hvilken side punktet ligger på. Hvis vi sjekker høyre og får
    false, vet vi at det er venstre-side og hvis vi sjekker venstre og får true vet vi at det er venstre-side.

    Nå kan vi fortsette med denne ideen, men nå er det nok lurt å dele området horisontalt istedet:

    |-----------------|
    |        |        |
    |        |        |
    |--------|        |
    |        |        |
    |  x     |        |
    |        |        |
    |-----------------|

    Nå sjekker vi altså øvre og nedre halvdel av den siden vi fant ut at punktet var i. Igjen kan vi eliminere en side
    basert på hva vi får som output på en av disse sidene.

    Og en gang til:

    |-----------------|
    |        |        |
    |        |        |
    |--------|        |
    |   |    |        |
    |  x|    |        |
    |   |    |        |
    |-----------------|


    Slik kan vi nå fortsette helt til vi sitter igjen med to halvdeler som er mindre enn kravet for å få eksakte koordinater.
    Da kan vi spørre på begge disse to områdene, og en av de er garantert å gi oss eksakte koordinater til punktet.


</details>
