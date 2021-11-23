# Plan

Denne uka blir repetisjonstime, og denne gruppa har temaet hashing :). Vi går gjennom alt av hashing på nytt, også ser vi på noen oppgaver hvis det blir tid for det. Hvis vi rekker og dere vil gå gjennom noe annet så kan vi gjøre det og.

Hashmap kode ligger under [uke10](../uke10)

# Oppgaver

Her er noen hashing baserte oppgaver som dere skal få gjøre under gruppetimen:

### HashMap innsetting/sletting

##### a - Linear probing

```
Tabell størrelse: 8
Hash(x) = x % 8
Kollisjonshåndtering: Linear probing

Sett inn: 3, 5, 11, 8, 19
```

Tegn opp hvordan tabellen ser ut etter innsetting

##### b - Separate chaining

```
Tabell størrelse: 8
Hash(x) = x*3 % 8
Kollisjonshåndtering: Separate chaining

Sett inn: 7, 15, 0, 12, 8, 9
```

Tegn opp hvordan tabellen (bøttene) ser ut etter innsetting


##### c - Sletting med linear probing

```
Ta utgangspunkt i tabellen etter innsetting i oppgave a.
Slettestrategi: "Fylle hullet"

Slett: 3
```

Tegn opp hvordan tabellen ser ut etter sletting


### Ekstraoppgave - Vanlig eksamensoppgave pattern

```
Gitt ett mønster p og en streng av ord s, finn ut om ordene i s følger samme mønster som p.

Eksempel input/output:

Input: p = "abba", s = "dog cat cat dog"
Output: true

Input: p = "abba", s = "dog cat cat fish"
Output: false

Input: p = "aaaa", s = "dog cat cat dog"
Output: false

Input: p = "abba", s = "dog dog dog dog"
Output: false
```

### Ekstraoppgave - O-notasjon

Jeg lagde noen flere O-notasjon oppgaver forrige uke [her](../uke12/code/big_o_advanced.py)
