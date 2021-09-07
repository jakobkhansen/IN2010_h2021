# Uke 2

### Plan

* Litt repetisjon om binære søketrær og sletting som vi ikke rakk forrige gang
* Balanserte trær (AVL, litt Rødsvarte)
* Forhåpentligvis rekke å se litt på Kattis, og eventuelt snakke om obligen og gjøre
    oppgaver

### Oppgaver

* [Prøv deg på Kattis](../kattis)
* [Ukeoppgaver](https://www.uio.no/studier/emner/matnat/ifi/IN2010/h21/ukesoppgaver/uke36.pdf) -  Unngå oppgaver som fokuserer på rødsvarte trær, disse ble laget da disse var hovedpensumet om balanserte trær 
* Finn et rødsvart tre som ikke er et AVL tre.


##### Implementere AVL innsetting

[Her](kode/BinarySearchTree.py) ligger et skall på et binært søketre, der søking og
innsetting er implementert for et ubalansert BST. Oppgave til deg er å utvide dette
kodeskallet slik at innsettingen gjøres slik som i AVL. Altså vil vi at innsetting i treet
skal balanseres, slik at vi får en lavere høyde på treet. 

Tenkeoppgave: Hvorfor tror du at vi har valgt å implementere dette rekursivt og ikke
iterativt? Hvorfor er det vanskeligere å implementere dette iterativt?

En mulig løsning finner du [her](losninger/BinarySearchTree.py)
