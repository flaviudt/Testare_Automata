"""
1) Testarea arată prezența defectelor, nu absența lor
    - Faptul ca nu mai găsim bug-uri, nu înseamnă neapărat că ele nu exista deloc

2) Testarea timpurie (Early testing)
    - Cu cât testarea începe mai repede, cu atât posibilitatea de apariție a bug-urilor este mai mică.

3) Testarea exhaustivă nu este posibilă
    - Adică nu este posibil să testăm toate funcționalitățile & toate combinațiile valide și nevalide de date de intrare.

4) Testarea este dependentă de context
    - Riscul asociat fiecărui tip de aplicație este diferit, prin urmare nu este eficient să se utilizeze aceeași metodă,
    tehnică și tip de testare pentru a testa toate tipurile de aplicații.

5) Gruparea defectelor (Clustering)
    - În timpul testării, se poate întâmpla ca majoritatea defectelor găsite să fie legate de un număr mic de module
    dezvoltate de către developeri.

6) Paradoxul pesticidelor (pesticide paradox)
    - Principiul paradoxului pesticidelor spune că, dacă același set de cazuri de testare sunt executate din nou și
    din nou pe parcursul perioadei de timp, atunci aceste seturi de teste nu sunt suficient de capabile să identifice
    noi defecte ale sistemului.

    Se referă mai ales la cazurile când re-testăm un bug.
    La fel cum gâzele devin imune la pesticide (astfel fiind nevoie de pesticide noi),
    si bug-urile dintr-o aplicatie pot fi rezolvate in așa fel încat sa acopere doar cazul raportat.
    Retestarea bug-urilor ar trebui să fie făcută (și) cu date noi.

7) Absența erorii este o aberație
    - Dacă software-ul este testat complet și dacă nu se găsesc defecte înainte de lansare,
    atunci putem spune că software-ul este 99% fără defecte.
"""