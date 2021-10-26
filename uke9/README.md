# Uke 9

## Plan

* Sortering 2
* Algoritmer i pensum
    * Merge-sort
    * Quicksort
    * Bucket-sort (+ Counting-sort)
    * Radix-sort
* Kanskje noe ekstra?
    * Binary insertion-sort
    * Timsort
    * Implementasjoner i programmeringsspråk
        * [Java](https://newbedev.com/what-is-the-sorting-algorithm-for-java)
        * [Python](https://hackernoon.com/timsort-the-fastest-sorting-algorithm-youve-never-heard-of-36b28417f399) - Fin artikkel om Timsort
* Oppgaver / Oblig

## Ressurser

* [Her](https://www.youtube.com/watch?v=Nz1KZXbghj8) er en fin video som beviser at comparison-basert sortering aldri kan være bedre enn `O(n log n)` worst-case. Snakker også om linear-time sortering (counting-sort, radix). Litt teknisk, men for den ekstra ivrige :)


## Oppgaver

##### Two-phase Multiway Merge-sort

Lag en algoritme som tar inn en liste av sorterte lister med tall som kombinerer disse listene sammen til 1 sortert liste. 
Algoritmen skal fungere slik at den slår sammen 2 og 2 lister helt til det bare er 1 liste igjen. 

Hint: Merge-sort merge + Huffman-koding kø
