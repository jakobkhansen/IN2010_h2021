# Big O oppgaver

Dette er et løsningsforslag til [disse](../kode/bigo_oppgaver.py) oppgavene.

### 1

```python
# 1. n er len(array)
def sum_three_elements(array : list[int]) -> int:
    return array[0] + array[1] + array[2]
```

Her aksesserer vi de tre første elementene av en liste. Uansett hvor stor listen er tar
dette like lang tid, altså er dette `O(1)`

### 2
```python
# 2. n er len(input_string)
def string_contains_space(input_string : str) -> bool:
    for char in input_string:
        if char == ' ':
            return True
    return False
```

Her itererer vi over hver bokstav i en streng. Siden vi analyserer for worst-case, så
antar vi at vi er nødt til å iterere over alle bokstavene før denne terminerer. Siden vi
går over hver bokstav en gang og gjør noen operasjoner, er dette `O(n)`

### 3
```python
# 3. n er n :)
def print_number_many_times(n : int) -> None:
    for _ in range(20):
        print(n)
```

Her printer vi ut et tall et konstant antall ganger, 20. Siden vi alltid printer ut og
gjør like mange operasjoner uansett hvor stort tallet er, så er dette `O(1)`

### 4

```python
# 4. n er len(array)
def contains_duplicate(array : list[int]) -> bool:
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False
```
Her sjekker vi om det finnes noen duplikater i en liste ved å sammenlikne hvert par av
elementer i listen. Siden vi for hvert element i listen går over alle elementene, så er
dette `O(n²)`

### 5

```python
# 5. n er len(array)
def contains_duplicate_smarter(array : list[int]) -> bool:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
    return False
```

Dette er en litt smartere versjon av forrige oppgave, her starter vi ikke på starten av
lista i den innerste løkka, men sammenlikner heller med alle tall til høyre for tallet vi
ser på. Her unngår vi altså å se på duplikate par. Antall par i en liste kan man regne ut
via formelen `(n*(n-1))/2` og dette kan visualiseres slik:

![Bilde](https://i.imgur.com/iMHvCLq.png)

Her skal alle 1'ere symbolere 1 iterasjon av den innerste løkka når input er en liste med
5 elementer. For oppgave 4 er dette ganske greit, vi går gjennom alle elementer for hvert
annet element i lista, som gir oss 25 iterasjoner (5²). I oppgave 6 ser vi at vi går
gjennom færre og færre elementer jo lenger vi kommer, men vi har bare (omtrent) halvert
antall iterasjoner. Siden å halvere antall iterasjoner er en konstant, faller det bort i O
notasjonen, og vi får fortsatt `O(n²)` på oppgave 5, selvom den er litt smartere.


### 6

```python
# 6. n er n :)
def multiply_by_two(n : int) -> None:
    current = 1
    while current <= n:
        print(current)
        current = current * 2

```

Her ganger vi et tall med 2 helt til det er større n, dette er jo omtrent definisjonen av
`O(log n)`! 

Noen lurer ofte på hvorfor vi kan skrive `O(log n)` uten å skrive en base. Forklaringen på
dette kan være at man egentlig har en implisitt base av `e`, den naturlige logaritmen, som
skrives `ln(n)`. Hvis man for eksempel skal ha base 2 fra denne, så er det `ln(n)/ln(2)`,
men dette er jo fortsatt `O(ln(n))`, siden `ln(2)` er en konstant! Dermed kan vi trekke
konklusjonen at hvilken base man konverterer til er en konstant som ikke har mye å si på
veksten av kjøretiden, altså er det en konstant vi abstraherer bort.


### 7

```python
# 7. n er len(array1), m = len(array2)
def sums_multiplied(array1 : list[int], array2 : list[int]) -> int:
    sum1 = 0
    sum2 = 0

    for element in array1:
        sum1 += element

    for element in array2:
        sum2 += element

    return sum1*sum2

```
Her går vi over 2 lister, som betyr at kjøretiden vår nå avhenger av 2 variabler! Siden vi
looper over alle elementer i hver liste, er kjøretiden `O(n+m)`. Vi kan ikke slå sammen
disse siden vi ikke vet noe om størrelsen på disse variablene. Hvis vi for eksempel hadde
visst at `n = m`, kunne vi skrevet `O(2n) = O(n)` eller `O(2m) = O(m)`, men det kan vi altså ikke her.

### 8

```python
# 8. n er len(array1), m er len(array2), k er k :)
def sums_multiplied_k_times(array1 : list[int], array2 : list[int], k : int):
    sum = 0
    for _ in range(k):
        sum += sums_multiplied(array1, array2)

```

Her kaller vi på den forrige metoden k ganger. Her kan det være lurt å først løse hva
oppgave 7. er i, og så sette det sammen med 8. Siden vi fant ut at 7. er `O(n+m)` og vi
kjører denne `k` ganger, får vi `O((n+m)*k)`

### 9 / ekstra

```python
# Ekstra: n er len(array)
# Se her: https://wiki.python.org/moin/TimeComplexity
def get_array_sorted(array : list[int]) -> list[int]:
    return sorted(array)
```
Hvordan vet vi hvor raskt noe er når vi ikke har laget det selv? Det blir ofte en veldig
stor jobb å analysere innebygde funksjoner i et programmeringsspråk eller bibliotek, men
ofte kan man finne noe dokumentasjon på dette. Sortering skal vi se en del på senere i
kurset, og da har vi algoritmer som er både `O(n²)`, `O(n log n)` og `O(n)`. Hvis vi ser
på lenken over (som lett kan finnes ved å google for eksempel "Python list complexity"),
så ser vi at Python sortering bruker en algoritme som kjører i `O(n log n)` tid.
