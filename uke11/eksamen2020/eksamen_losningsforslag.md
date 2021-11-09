@document.meta
  title: exam
  description: 
  author: jakob
  categories: 
  created: 2021-11-09
  version: 0.0.8
@end

# Oppvarming
  * Algoritme
    * Sekvens av steg for å oppnå et resultat
    * Oppskrift
  * Datastruktur
    * En beholder av data i en strukturert form

# Binære søketrær
* a: C
* b: 5
* c: Nei
* d: Ja

# Grafegenskaper
* a: Nei, G er sammenhengende
* b: Ja, fjerne kanter
* c: Ja, G er ikke et tre, så vi må fjerne kanter
* d: G er ikke et tre
* e: Nei, H, er en DAG
* f: Ja, H er en dag, så vi må legge til kanter for at det ikke skal være det
* g: Ja, H er ikke sterkt-sammenhengende, legg til kanter
* h: Nei, H er ikke sterkt-sammenhengende

# Linear probing

* [29,0,0,93,74,13,45,0,48,99]


# Søk

* Insersection2 kan gi feil svar siden A ikke er sortert

### Oppgavene
* Hvis B inneholder ett element, altså k = 1, hvilken prosedyre gir riktig svar med
minimal kjøretidskompleksitet?
    * Intersection1, siden vi bare går over 1 element i B og sjekker om det er i A 

* Hvis B inneholder log(n), elementer, altså k = log(n), hvilken prosedyre gir riktig
svar med minimal kjøretidskompleksitet?
    * Intersection1 og Intersection3 er like, O(n log n)

* Hvis B inneholder n elementer, altså k = n, hvilken prosedyre gir riktig
svar med minimal kjøretidskompleksitet?
    * Intersection3, O(n log n), best
    * Intersection1 er O(n²)

* Hvis B inneholder n² elementer, altså k = n², hvilken prosedyre gir riktig
svar med minimal kjøretidskompleksitet?
    * Intersection3 er O(n² * log n), best
    * Intersection1 er O(n³)



# AVL
* a: Se bilde
* b: 4
* c: Ja
* d: 2

# Subanagram

### a
* O(s*(w + w)) = O(s*w)

### b

```python
def IsSubanagramOf2(W,S):
  F = FreqTable(W)
  G = FreqTable(S)

  for char in W:
    if (F.get(char) > G.get(char)):
      return False
  return True
```

### c
* Strategi 1 sin kjøretid vil vokse i forhold til antall ord i ordlista
* Strategi 2 sin kjøretid vil vokse i forhold til antall bokstaver vi har på brettet
    * Strategi 2 vokser derimot helt forferdelig i forhold til S 

### d
* Radix sort, kan bruke en hashmap til å sortere


# Fire typer grafer
### a
```python
def Type2Verifier(G, C):
  visited = set()
  visited.add(C[0])        

  for i in range(1, len(C)):
    if not (C[i], C[i-1]) in G.E or C[i] in visited:
      return False
    visited.add(C[i])
  # Tror Lars glemte å sjekke at lengden på stien stemmer i løsningen
  return len(visited) == len(C) and (C[0], C[-1]) in G.E:        
```

### b
NP er ofte definert som at man kan verifisere en JA-instans i polynomiell tid. Vi har
laget en algoritme som verifiserer en JA/NEI instans i polynomiell tid, derfor er
Type2 i NP

### c
Siden type 2 alltid er en stor sykel (hamiltonsykel), vil det alltid være 2
(disjunkte) stier å komme seg til en node på. Dersom en node i en av stiene blir
borte, kan man fortsatt komme seg til en node via den andre stien.

### d

```python
def TwoPaths(G,C,s,t):
s_index = C.indexOf(s)

# Path 1
for i in range(len(C)):
  curr_index = (s_index + i) % len(C)
  print(curr_index)
  if C[curr_index] == t:
    break

# Path 2
for i in range(len(C)):
  curr_index = (s_index - i) % len(C)
  print(C[curr_index])
  if C[curr_index] == t:
    break
```

### e
* Se bilde

### f
* Nei, hvis det er flere kanter som får samme vekt, så er det ikke nødvendigvis bare
en billigste måte
* Nei, siden G_4 ikke er sammenhengende, kan vi ikke få et spenntre
* Ja, det stemmer, siden type 3 er et tre (sammenhengende) og den har mindre vekter
enn 2 og 1.
* 3

### g
* Hvis grafen er av type 1 og kantene har vekt 10, så kan vi bare returnere 10. Dette
er fordi type 1 er en komplett graf, og vi vet da at den korteste stien er å reise 1
kant, som alltid har vekt 10.
* Hvis grafen er at type 2 kan vi bruke BFS shortest path

### h
* A: 0,
* B: 2,
* C: 2,
* D: 1,
* E: 4,
* F: 7,
* G: 8,
* H: 10,

# HTML
### a
```python
def goodDivs(A):
  div_count = 0
  for tag in A:
    if tag == "<div>":
      div_count += 1
    else:
      div_count -= 1

    if div_count < 0:
      return False
  return div_count == 0    
@end
```

### b
```python
def goodTags(A):
  stack = []
  for tag in A:
    if isOpen(tag):
      stack.append(tag)
    else:
      if len(stack) == 0 or TagType(stack[-1]) != TagType(tag):
        return False
      else:
        stack.pop()
return len(stack) == 0
@end
```
