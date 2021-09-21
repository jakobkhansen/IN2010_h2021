# Uke 4

### Plan

* Definere grafer og se på masse definisjoner
* Se på to algoritmer for å traversere gjennom grafer (DFS, BFS)
* Se på en algoritme for dependency grafer (Topologisk sortering)
* Oppgaver

### Oppgaver

#### Relevante Kattis oppgaver

##### DFS/BFS

##### Topologisk sortering

* [build dependencies](https://open.kattis.com/problems/builddeps)
* [pickup sticks](https://open.kattis.com/problems/pickupsticks)

#### Studieløp topologisk sortering

Tegn en dependency graf over studieløpet ditt med fagene du har tatt og tenker å ta, for
eksempel en bachelorgrad. La avhengighetene være påkrevde og anbefalte forkunnskaper til
fagene. Finn så en topologisk sortering ved å bruke algoritmen vi har sett på denne uken.

#### Åpen oppgave, anbefalte venner i et sosialt nettverk

La oss si at vi har en graf der noder er brukere i et sosialt nettverk, og urettede kanter
mellom brukere betyr at de to brukerne er venner. Lag en algoritme som tar inn en bruker
(node), og returnerer en liste med anbefalte venner for den brukeren, i prioritert
rekkefølge. Listen kan være for eksempel 50 venneanbefalinger.

Dette er en veldig åpen oppgave med mange gode svar, prøv deg frem!

Ting å tenke på:
* Vi burde ikke gå over alle noder i nettverket, sosiale nettverk er store og å generere
    anbefalte venner for alle brukere vil ta ekstremt lang tid hvis vi går over alle andre
    brukere i nettverket som er `O((|V+E|)²)`
* Algoritmen trenger ikke være perfekt, bare lag en algoritme som du tror vil fungere
    greit i praksis.
