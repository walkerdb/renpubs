# Renaissance Vocal Music
A repository containing structured data detailing the contents of printed vocal part-books from the Renaissance. 
Scope for this project is limited to the publications described in the Nuovo Vogel series.

Current publication count: 640 / ~5100  
Total works: 17406
 
### Data structure
`publications.json` contains an array of structured data for each publication. Each publication has the following structure: 

```json
{
    "title": "",
    "year": "",
    "composers": [],
    "printing_info": {
        "printers": [{
          "modern": "Modern spelling of the name",
          "original": "Spelling as appeared in original publication"
        }],
        "location": ""
    },
    "genres": [],
    "series_number": 0,
    "voices": [],
    "physical_description": {
        "number_of_books": 0,
        "book_size": "'Quarto' or 'Octavo'",
        "pages": 0,
        "is_oblong": true
    },
    "dedication": {
        "text": "",
        "dedicator": "",
        "dedicatee": "",
        "location": ""
    },
    "works": [{
        "title": "",
        "composer": "",
        "voices": 0,
        "poet": "",
        "part": 0,
        "page": 0
    }],
    "library_locations": [{"siglum": "", "parts": ""}],
    "identifiers": {
      "nuovo_vogel": "1"
    }
}
```

### Publication Counts
Number of publications each composer appears in:

| Composer | Publication Count |
| -------- | -------- |
| Orlando di Lasso | 87 |
| Jacques Archadelt | 77 |
| Giovanni Giacomo Gastoldi | 46 |
| Jacquet de Berchem | 37 |
| Adriano Banchieri | 29 |
| Francesco Corteccia | 28 |
| Giovanni Domenico da Nola | 25 |
| Andrea Gabrieli | 23 |
| Paolo Animuccia | 22 |
| Hector Vidue | 22 |
| Giovanni Battista Bassani | 20 |
| Antonio Barré | 16 |
| Giovanni Matteo Asola | 15 |
| Agostino Agazzari | 14 |
| Felice Anerio | 14 |
| Anonymous | 14 |
| Francesco Roselli | 13 |
| ? | 12 |
| Ludovico Agostini | 12 |
| Stefano Bernardi | 12 |
| Marc'Antonio Ingegneri | 12 |
| Giovanni Lochenburgo | 12 |
| Luca Marenzio | 12 |
| Constantio Porta | 12 |
| Cipriano de Rore | 12 |
| Francesco de Layolle | 11 |
| Giovanni Francesco Anerio | 10 |
| Costanzo Festa | 10 |
| Girolamo Belli | 9 |
| Christian Ameyden | 8 |
| Filippo Azzaiolo | 8 |
| Bartolomeo Barbarino | 8 |
| Ippolito Baccusi | 7 |
| Giovanni Animuccia | 6 |
| Paolo Bellasio | 6 |
| Giulio Belli | 6 |
| Ghirardo da Panico | 6 |
| Lodovico Bellanda | 5 |
| Severo Bonini | 5 |
| Gio. Francesco Caldarino | 5 |
| da Reggio Hoste | 5 |
| Claude Lejeune | 5 |
| Orazio Vecchi | 5 |
| Giovanni Battista Abbatessa | 4 |
| Francesco Adriani | 4 |
| Lelio Bertani | 4 |
| Giuseppe Biffi | 4 |
| Claudin | 4 |
| Courtois | 4 |
| Lheretier | 4 |
| Mathias | 4 |
| Moulu | 4 |
| Ippolito Tartaglino | 4 |
| Philippe Verdelot | 4 |
| Ysore | 4 |
| Innocenzo Alberti | 3 |
| Orazio Angelini | 3 |
| Ludovico Balbi | 3 |
| Costantino Baselli | 3 |
| Vincenzo Bell'Haver | 3 |
| Pietro Benedetti | 3 |
| Francois Du Bois | 3 |
| Valerio Bona | 3 |
| Giulio Bonagiunta | 3 |
| Giovanni Maria Bononcini | 3 |
| Certon | 3 |
| Claudio da Correggio | 3 |
| Cosson | 3 |
| Girolamo Frescobaldi | 3 |
| Gioseffo Guami | 3 |
| Iacotin | 3 |
| Laiolle | 3 |
| Johannes Lupi | 3 |
| Lupus | 3 |
| Philippe de Monte | 3 |
| Morales | 3 |
| Vincenzo Ruffo | 3 |
| Paulo d'Angelo | 3 |
| Giovanni Leonardo dell'Arpa | 3 |
| Gregor Aichinger | 2 |
| Marcello Albano | 2 |
| Filippo Albini | 2 |
| Giovan Francesco Alcarotti | 2 |
| Giovanni Battista Alveri | 2 |
| Costanzo Antegnati | 2 |
| Paolo Aretino | 2 |
| Ottavio Bargnani | 2 |
| Orindio Bartolini | 2 |
| Francesco Antonio Baseo | 2 |
| Lelio Basile | 2 |
| Vincenzo Bastini | 2 |
| Luca Bati | 2 |
| Dionisio Bellante | 2 |
| Domenico Belli | 2 |
| Giovan Pietro Berti | 2 |
| Bernardino Bertolotti | 2 |
| Pier'Antonio Bianchi | 2 |
| Francesco Bianciardi | 2 |
| Giovan Pietro Biandra | 2 |
| Francesco Bifetto | 2 |
| Alfonso Ganassi da Bologna | 2 |
| Francesco Bonardo | 2 |
| Aurelio Bonelli | 2 |
| Caldarino | 2 |
| Pirro Albergati Capacelli | 2 |
| Bizzarro Accademico Capriccioso | 2 |
| Giovanni Battista Falcidio | 2 |
| Giovanni Battista Gabella | 2 |
| Giovanni Gabrieli | 2 |
| Vincenzo Galilei | 2 |
| Giovanni Battista Grillo | 2 |
| Hans Leo Hassler | 2 |
| Da Reggio Hoste | 2 |
| M. Ihan | 2 |
| Scipione Lacorcia | 2 |
| Lamartoretta | 2 |
| Giovanni Tommaso Lambertini | 2 |
| Francesco de Landis | 2 |
| Layole | 2 |
| Leone Leoni | 2 |
| Francesco Londariti | 2 |
| Lupachino | 2 |
| Tiburtio Massaino | 2 |
| Hubert Naich | 2 |
| Benedetto Pallavicino | 2 |
| Pierreson | 2 |
| Dionisio Polato | 2 |
| di Nardò Benedetto Serafico | 2 |
| Antonio Taroni | 2 |
| Ivo de Vento | 2 |
| Phillipe Verdelot | 2 |
| Antonio Il Verso | 2 |
| Alfonso dalla Viola | 2 |
| Yvo | 2 |
| Petrus organista | 2 |
| Antonio Maria Abbatini | 1 |
| Alessandro Aglione | 1 |
| Agostino Agresta | 1 |
| Neri Alberti | 1 |
| Vittoria Aleotti | 1 |
| Lorenzo Allegri | 1 |
| Cataldo Amodei | 1 |
| Domenico Anglesi | 1 |
| Andrea Anglesio | 1 |
| Paulo Animuccia | 1 |
| Padovano Annibale | 1 |
| Anselmo | 1 |
| Abbondio Antonelli | 1 |
| Giovanni Appolloni | 1 |
| Carlo Ardesi | 1 |
| Gio. Paolo Ardesi | 1 |
| Guglielmo Arnoni | 1 |
| Giovan Giacomo Arrigoni | 1 |
| Giovan Mario Artusi | 1 |
| Antonio Artusini | 1 |
| Girolamo Avanzolini | 1 |
| Carlo Agostino Badia | 1 |
| Oliviero Ballis | 1 |
| Simone Balsamino | 1 |
| Rodiano Barera | 1 |
| Antonio Barges | 1 |
| Leonardus Barre | 1 |
| Girolamo Barthei | 1 |
| Giovanni Battista Bartoli | 1 |
| Donato Basile | 1 |
| Paolo Antonio Bassani | 1 |
| Giovanni Bassano | 1 |
| Orazio Battaglioni | 1 |
| Vincenzo Bell'haver | 1 |
| Giovanmaria Benassai | 1 |
| Angelo Berardi | 1 |
| Ercole Bernabei | 1 |
| Pisano Bernardo | 1 |
| Bertoldo Bertoldi | 1 |
| Geronimo Bettino | 1 |
| Catterino Bianchi | 1 |
| Giovanni Battista Bianchi | 1 |
| Antonio Bicci | 1 |
| Luzio Billi | 1 |
| Francesco, detto Primi Boccella | 1 |
| Giovanni Bodeo | 1 |
| F. Du Bois | 1 |
| Bernardo Bolognini | 1 |
| Filippo Bonaffino | 1 |
| Francesco Perissone Bonardo | 1 |
| Iseppo Bonardo | 1 |
| Paolo Antonio Bonfilio | 1 |
| Pier Andrea Bonini | 1 |
| Eliseo Bonizzoni | 1 |
| Giovanni Bononcini | 1 |
| Giovanni Andrea Angelini Bontempi | 1 |
| Giacomo Bonzanini | 1 |
| Nicolo Borboni | 1 |
| Francesco Maria Borelli | 1 |
| Giorgio Borgia | 1 |
| Cesare Borgo | 1 |
| Il Caldarino | 1 |
| Hippolito Camaterò | 1 |
| Geminiano Capilupi | 1 |
| Geminiano Capilupo | 1 |
| Giacom' Antonio Cardillo | 1 |
| Gioanne de Carmeni | 1 |
| Paolo Casanuova | 1 |
| Casson | 1 |
| Scipione Cerreto | 1 |
| Certori | 1 |
| Ippolito Chamaterò | 1 |
| Cipriano | 1 |
| Gioan Contino | 1 |
| Ludovico Cornale | 1 |
| Costanzo | 1 |
| Ghiselino Dancherts | 1 |
| Ghinolfo Dattaro | 1 |
| Scipione Dentici | 1 |
| Baldessar Donato | 1 |
| Mutio Efrem | 1 |
| Stefano Felis | 1 |
| Feraboscho | 1 |
| Vin. Ferro | 1 |
| Giulio Fiesco | 1 |
| Arnoldus Flandrus | 1 |
| Giovanni Florio | 1 |
| D. Paolo Fonghetti | 1 |
| Paolo Fonghetto | 1 |
| Formica | 1 |
| Domenico Gabrielli | 1 |
| Giulio Cesare Gabussi | 1 |
| Bernardo Gaffi | 1 |
| Gregorio Gallino | 1 |
| Mr. H. Goudsteen | 1 |
| Antoni Guelfi | 1 |
| Francesco Maria Guidani | 1 |
| J. Haffner | 1 |
| R. Isaacides. | 1 |
| Jaconri | 1 |
| Jacotin | 1 |
| Luca Kohc | 1 |
| Francesco Lambardi | 1 |
| Lamberto | 1 |
| Francesco Lauro | 1 |
| Cornelis de Leeuw | 1 |
| Lerma | 1 |
| Gio. Girolamo Conte di Lodrone | 1 |
| Giovanni de Macque | 1 |
| Hettorre della Marra | 1 |
| Paolo Masnelli | 1 |
| Pietro Mereschallo | 1 |
| Claudio Merulo | 1 |
| Iacomo Mettula | 1 |
| Giovan Nasco | 1 |
| Paschali Di Negro | 1 |
| Domenico Pace | 1 |
| Annibal Padoano | 1 |
| Giovan Pier Luigi da Palestrina | 1 |
| Andrea Patricio | 1 |
| Fabio Pelusu | 1 |
| Francesco Bonrado de Perissone | 1 |
| Bartolomeo Pifaro | 1 |
| Costanzo Porta | 1 |
| Constanzo Porta | 1 |
| Cornel Piet Pred. | 1 |
| Cornelis Piet. Pred. | 1 |
| Di Cornel Piet Pred.[?] | 1 |
| Cornel. Piet. Pred.[?] | 1 |
| Pietro Ragno | 1 |
| Girolamo Avanzolini da Rimini | 1 |
| Giulio Rinaldi | 1 |
| D. Marsilio Santini | 1 |
| Marsilio Santini | 1 |
| Alessandro Savioli | 1 |
| G. I. Schagen | 1 |
| Gio. Angelo De Sotijs | 1 |
| Spontone | 1 |
| Francesco Stivori | 1 |
| Alessandro Striggio | 1 |
| Pietro Taglia | 1 |
| Luca Valente | 1 |
| Alex Venitiano | 1 |
| Pietro Vinci | 1 |
| P. Vinci | 1 |
| Jacob Vredeman | 1 |
| Giaches Vuert | 1 |
| Adriano Vuillaert | 1 |
| Aniballe bolognese | 1 |
| P. Ambrogio bresciano | 1 |
| P. Ambrogio bruciano | 1 |
| incerto | 1 |