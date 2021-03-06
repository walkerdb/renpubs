from nvdomain.printer import Printer

LOCATIONS = {
    "Amsterdam": "Amsterdam",
    "Anvers ": "Antwerp",
    "Anvers.": "Antwerp",
    "Anversa": "Antwerp",
    "Augusta": "Augsburg",
    "Bologna": "Bologna",
    "Bracciano": "Bracciano",
    "Cremona": "Cremona",
    "Cologne": "Cologne",
    "Dilinga": "Dillingen",
    "Dresda": "Dresden",
    "Duaco": "Douai",
    "Duaci": "Douai",
    "Ferrara": "Ferrara",
    "Firenze": "Florence",
    "Fiorenza": "Florence",
    "Francoforti": "Frankfurt",
    "Lovain": "Leuven",
    "Louvain": "Leuven",
    "Lucca": "Lucca",
    "Mantova": "Mantua",
    "Milan": "Milan",
    "Milano": "Milan",
    "Monaco": "Munich",
    "Monachij": "Munich",
    "Napoli": "Naples",
    "Noribergae": "Nuremberg",
    "Norimberga": "Nuremberg",
    "Norimbergae": "Nuremberg",
    "Nürnberg": "Nuremberg",
    "Orvieto": "Orvieto",
    "Palermo": "Palermo",
    "Paris": "Paris",
    "Parigi": "Paris",
    "Perugia": "Perugia",
    "Roma": "Rome",
    "Rotterdamo": "Rotterdam",
    "Rotterodamo": "Rotterdam",
    "Vinegia": "Venice",
    "Vineggia": "Venice",
    "Vinetia": "Venice",
    "Verona": "Verona",
    "Venet.": "Venice",
    "Veneta": "Venice",
    "Venegia": "Venice",
    "Venetia": "Venice",
    "Venetijs": "Venice",
    "Venetiis": "Venice"
}

MONTHS = {
    "I": "Jan.",
    "II": "Feb.",
    "III": "Mar.",
    "IV": "Apr.",
    "V": "May",
    "VI": "June",
    "VII": "July",
    "VIII": "Aug.",
    "IX": "Sept.",
    "X": "Oct.",
    "XI": "Nov.",
    "XII": "Dec."
}

PRINTERS = {
    "Henrico Aertssens": Printer("Henrico Aertssens"),
    "Pierre Attaingnant": Printer("Pierre Attaingnant"),
    "Pierre Attaignant": Printer("Pierre Attaingnant"),
    "Ricciardo Amadino": Printer("Ricciardo Amadino"),
    "Giorgio Angelieri": Printer("Giorgio Angelieri"),
    "Vittorio Baldini": Printer("Vittorio Baldini"),
    "Pierre Ballard": Printer("Pierre Ballard"),
    "Pietro Ballard": Printer("Pierre Ballard"),
    "P. Ballard": Printer("Pierre Ballard"),
    "Roberto Ballard": Printer("Robert Ballard"),
    "Robert Ballard": Printer("Robert Ballard"),
    "R. Ballard": Printer("Robert Ballard"),
    "Antonio Barré": Printer("Antonio Barré"),
    "Antonio Barre": Printer("Antonio Barré"),
    "Barezzo Barezzi": Printer("Barezzo Barezzi"),
    "Matthijs Bastiansz": Printer("Matthijs Bastiansz"),
    "Jean Bellère": Printer("Jean Bellère"),
    "Jean Bellere": Printer("Jean Bellère"),
    "Giovanni Bellero": Printer("Jean Bellère"),
    "Amadeo Belmonte": Printer("Amadeo Belmonte"),
    "Ottavio Beltrano": Printer("Ottavio Beltrano"),
    "Ottavio Beltramo": Printer("Ottavio Beltrano"),
    "Adam Berg": Printer("Adam Berg"),
    "Adamo Berg": Printer("Adam Berg"),
    "Adamus Berg": Printer("Adam Berg"),
    "Melchior Bergen": Printer("Melchior Bergen"),
    "Melchio Bergen": Printer("Melchior Bergen"),
    "Gio. Francesco Besozzo": Printer("Giovanni Francesco Besozzo"),
    "Vincenzo Bianchi": Printer("Vincenzo Bianchi"),
    "Antonio Blado": Printer("Antonio Blado"),
    "Giovanni Bogardo": Printer("Giovanni Bogardo"),
    "Scipione Bonino": Printer("Scipione Bonino"),
    "Novello de Bonis": Printer("Novello de Bonis"),
    "Pietro Brea": Printer("Pietro Brea"),
    "Giovanni De Bulghat": Printer("Giovanni De Bulghat"),
    "Henrigo De Campis": Printer("Henrico De Campis"),
    "Henrico De Campis": Printer("Henrico De Campis"),
    "Matteo Cancer": Printer("Matteo Cancer"),
    "Giacomo Carlino": Printer("Giovanni Giacomo Carlino"),
    "Iacomo Carlino": Printer("Giovanni Giacomo Carlino"),
    "G. C. Carlino": Printer("Giovanni Giacomo Carlino"),
    "Pietro Cecconcelli": Printer("Pietro Cecconcelli"),
    "Everardo Cloppenburch": Printer("Everardo Cloppenburch"),
    "Francesco Dalle Donne": Printer("Francesco Dalle Donne"),
    "Francesco dalle Donne": Printer("Francesco Dalle Donne"),
    "Valerio Dorico": Printer("Valerio Dorico"),
    "Valerio et Luygi": Printer("Valerio Dorico"),
    "Luygi Dorici": Printer("Luigi Dorico"),
    "Andrea Fei": Printer("Andrea Fei"),
    "Gratiadio Ferioli": Printer("Gratiadio Ferioli"),
    "Gio. Antonio de Franceschi": Printer("Giovanni Antonio de Franceschi"),
    "Alessandro Gardano": Printer("Alessandro Gardano"),
    "Alessandro Gardane": Printer("Alessandro Gardano"),
    "Angelo Gardano": Printer("Angelo Gardano"),
    "Angelum Gardanum": Printer("Angelo Gardano"),
    "Antonio Gardano": Printer("Antonio Gardano", "Venice"),
    "Antonio Gardane": Printer("Antonio Gardano", "Venice"),
    "d'Antonio Gardane": Printer("Antonio Gardano", "Venice"),
    "Antoine Gardane": Printer("Antonio Gardano", "Venice"),
    "Antonium Gardane": Printer("Antonio Gardano", "Venice"),
    "Ant. Gard.": Printer("Antonio Gardano", "Venice"),
    "Catherine Gerlach": Printer("Catherine Gerlach"),
    "Catharinae Gerlachiae": Printer("Catherine Gerlach"),
    "Gerardo Greuenbruch": Printer("Gerardo Greuenbruch"),
    "Giuseppe Guglielmo": Printer("Giuseppe Guglielmo"),
    "Antonio Hucher": Printer("Antonio Hucher"),
    "Paulo Kaufmann": Printer("Paul Kauffmann"),
    "Paulo Kauffman": Printer("Paul Kauffmann"),
    "Paulus Kauffmannus": Printer("Paul Kauffmann"),
    "Paul Kauffmanns": Printer("Paul Kauffmann"),
    "Gio. Batista Landini": Printer("Giovanni Batista Landini"),
    "Batista Landini": Printer("Giovanni Batista Landini"),
    "Filippo Lomazzo": Printer("Filippo Lomazzo"),
    "Philippum Lomatium": Printer("Filippo Lomazzo"),
    "Ambrosio Magnetta": Printer("Ambrosio Magnetta"),
    "Bartholomeo Magni": Printer("Bartolomeo Magni"),
    "Bartolomeo Magni": Printer("Bartolomeo Magni"),
    "Bartholomaei Magni": Printer("Bartolomeo Magni"),
    "Bartholomei Magni": Printer("Bartolomeo Magni"),
    "Paul Marceau": Printer("Paul Marceau"),
    "Cristofano Marescotti": Printer("Cristofano Marescotti"),
    "Cristoforo Marescotti": Printer("Cristofano Marescotti"),
    "Giorgio Marescotti": Printer("Giorgio Marescotti"),
    "Paulus Matthysz": Printer("Paulus Matthysz"),
    "Paulus Matthihsz": Printer("Paulus Matthysz"),
    "Pietro Maria Marchetti": Printer("Pietro Maria Marchetti"),
    "Gio. Battista Maringo": Printer("Giovanni Battista Maringo"),
    "Paolo Masotti": Printer("Paolo Masotti"),
    "Mascardi": Printer("Giacomo Mascardi"),
    "Adamo Meltzer": Printer("Adam Meltzer"),
    "Claudio Merulo": Printer("Claudio Merulo"),
    "Claudio da Correggio": Printer("Claudio Merulo"),
    "Claudio da Coreggio": Printer("Claudio Merulo"),
    "Gioseffo Micheletti": Printer("Gioseffo Micheletti"),
    "Iacopo Moderno": Printer("Jacques Moderne"),
    # "Iacobum Modernum": Printer("Jacques Moderne"),
    "Pier-maria Monti": Printer("Pietro Maria Monti"),
    "Pietro Maria Monti": Printer("Pietro Maria Monti"),
    "Giacomo Monti": Printer("Giacomo Monti"),
    "Lodovico Monza": Printer("Lodovico Monza"),
    "Francesco Moschenio": Printer("Francesco Moscheni"),
    "Francesco et Simone Moscheni": Printer("Francesco and Simone Moscheni"),
    "Nicolò Mutij": Printer("Nicolò Mutii"),
    "Francesco Osanna": Printer("Francesco Osanna"),
    "e Paci,": Printer("Giacinto Paci"),
    "Pietroiacomo Petrucci": Printer("Pietro Giacomo Petrucci"),
    "Octavianum Petrutium": Printer("Ottaviano Petrucci"),
    "Pierre Phalese": Printer("Pierre Phalèse"),
    "Petro Phalesio": Printer("Pierre Phalèse"),
    "Pietro Phalesio": Printer("Pierre Phalèse"),
    "i Pieri,": Printer("Bernardino Pieri"),
    "Christofle Plantin": Printer("Christophe Plantin"),
    "Plinio Pietrasanta": Printer("Plinio Pietrasanta"),
    "Zanobi Pignoni": Printer("Zanobi Pignoni"),
    "Pacifico Pontio": Printer("Pacifico da Ponte"),
    "Cesare Porro": Printer("Cesare Porro"),
    "Cesare Pozzo": Printer("Cesare Pozzo"),
    "Gio. Pretorio": Printer("Giovanni Pretorio"),
    "Francesco Rampazetto": Printer("Francesco Rampazetto"),
    "Francesco Rampazzetto": Printer("Francesco Rampazetto"),
    "Francesco Ramazetto": Printer("Francesco Rampazetto"),
    "Alessandro Raverij": Printer("Alessandro Raverii"),
    "Alessandro Raverii": Printer("Alessandro Raverii"),
    "Gioseffo Ricci": Printer("Gioseffo Ricci"),
    "Battista Robletti": Printer("Giovanni Battista Robletti"),
    "Gio. Batt. Robletti": Printer("Giovanni Battista Robletti"),
    "heredi di Francesco Rossi": Printer("heredi di Francesco Rossi"),
    "Giovanni de' Rossi": Printer("Giovanni de' Rossi"),
    "Adrian le Roy": Printer("Adrian le Roy"),
    "Adriano le Roy": Printer("Adrian le Roy"),
    "Rinaldo Ruuli": Printer("Rinaldo Ruuli"),
    "Vincenzo Sabbio": Printer("Vincenzo Sabbio"),
    "Gioseppe Sala": Printer("Giuseppe Sala"),
    "Valerio Salviano": Printer("Valerio Salviano"),
    "Valentin Schönigk": Printer("Valentin Schönigk"),
    "Gerolamo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Giolamo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Girolamo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Girolamo Scoto": Printer("Girolamo Scotto", "Venice"),
    "Gierolamo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Gieronimo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Hieronymo Scotto": Printer("Girolamo Scotto", "Venice"),
    "Hieronymus Scotus": Printer("Girolamo Scotto", "Venice"),
    "Hieronymum Scotum": Printer("Girolamo Scotto", "Venice"),
    "Hieronymum Scottum": Printer("Girolamo Scotto", "Venice"),
    "Hieronimum Scotum": Printer("Girolamo Scotto", "Venice"),
    "Marino Silvani": Printer("Marino Silvani"),
    "Luca Antonio Soldi": Printer("Luca Antonio Soldi"),
    "Gio. Battista Sottile": Printer("Giovanni Battista Sottile"),
    "Nicolao Stenio": Printer("Nicolao Stenio", "Frankfurt"),
    "Tylman Susato": Printer("Tielman Susato"),
    "Tielman Susato": Printer("Tielman Susato"),
    "Tilman Susato": Printer("Tielman Susato"),
    "Sottile": Printer("Giovanni Battista Sottile"),
    "Simon Tini": Printer("Simon Tini"),
    "Simonus Tini": Printer("Simon Tini"),
    "Agostino Tradate": Printer("Agostino Tradate"),
    "Paulo Tortorino": Printer("Paulo Tortorino"),
    "Simone Verovio": Printer("Simone Verovio"),
    "Giacomo Vincenti": Printer("Giacomo Vincenti"),
    "Giacomo Vincenci": Printer("Giacomo Vincenti"),
    "Giacomo Vincenzi": Printer("Giacomo Vincenti"),
    "Iacomo Vincenti": Printer("Giacomo Vincenti"),
    "Giamo (sic) Vincenti": Printer("Giacomo Vincenti"),
    "Alessandro Vincenti": Printer("Alessandro Vincenti"),
    "Alessanro Vincenti": Printer("Alessandro Vincenti"),
    "Constantino Vitale": Printer("Constantino Vitale"),
    "Costantino Vitale": Printer("Constantino Vitale"),
    "C. Vitale": Printer("Constantino Vitale"),
    "Joh. Christoph Weigel": Printer("Johann Christoph Weigel", "Nuremberg"),
    "Isaaco Wesbergio": Printer("Isaaco Wesbergio"),
    "Vvillem Iansz. Vvijngaert": Printer("Willem Jansz Wyngaert"),
    "Bartolomeo Zannetti": Printer("Bartolomeo Zanetti"),
    "Bartholomeo Zannetti": Printer("Bartolomeo Zanetti"),
    "Luigi Zannetti": Printer("Luigi Zanetti"),
    "Alessandro Zatta": Printer("Alessandro Zatta")
}

CATALOG_VARIANTS = {
    "RISM": "RISM I",
    "Brown": "Brown",
    "Sartori": "Sartori",
    "Haar": "Haar",
    "Pass": "Pass",
    "RMI": "RMI",
    "Boetticher": "Boetticher",
    "Lesure": "Lesure",
    "Lesure e": "Lesure & Thibault"
}
# missing Sartori & Petrucci

MUSIC_GENRES = {
    "d'Aria": "Arias",
    "Aria": "Arias",
    "Balletti": "Balletti",
    "Balletten": "Balletti",
    "Cantate": "Songs",
    "Canzonette": "Canzonette",
    # "Canzoni": "Canzons",
    # "Canzon spirituale": "Spiritual songs",
    # "Canzoni francese": "Chansons",
    "Chanson": "Chansons",
    "Chanson spirituale": "Spiritual Chansons",
    "Concenti musicali": "Concerted music",
    "Lieder": "Lieder",
    "Madrigale": "Madrigals",
    "Madregali": "Madrigals",
    "Madrigal": "Madrigals",
    "Madrigali spirituale": "Spiritual Madrigals",
    "Mascherate": "Mascherata",
    "Motetti": "Motets",
    "Musiche": "Musiche",
    "Ricercari": "Ricercars",
    "Vilanelle": "Villanelle",
    "Villanelle": "Villanelle",
    "Villanesche": "Villanesche",
    "Villotte alla padoana": "Paduan Villotte",
    "Villotte alla Napolitane": "Neapolitan Villotte",
    "alcune Napolitane": "Neapolitan Villotte",
}

ITALIAN_NUMBERS = {
    " Uno ": 1,
    " Una ": 1,
    " voce sola": 1,
    " Due ": 2,
    " Doi ": 2,
    " Tre ": 3,
    " Quattro ": 4,
    " Quatro ": 4,
    " Cinque ": 5,
    " Sei ": 6,
    " Sette ": 7,
    " Otto ": 8,
    " Nove ": 9,
    " Dieci ": 10,
    " Undici ": 11,
    " Dodici ": 12,
    " Tredici ": 13,
    " Quattordici ": 14,
    " Quindici ": 15,
    " Sedici ": 16,
    " Diciassette ": 17,
    " Diciotto ": 18,
    " Diciannove ": 19,
    " Venti ": 20,
    " Uno, ": 1,
    " voce sola, ": 1,
    " Due, ": 2,
    " Tre, ": 3,
    " Quattro, ": 4,
    " Quatro, ": 4,
    " Cinque, ": 5,
    " Sei, ": 6,
    " Sette, ": 7,
    " Otto, ": 8,
    " Nove, ": 9,
    " Dieci, ": 10,
    " Undici, ": 11,
    " Dodici, ": 12,
    " Tredici, ": 13,
    " Quattordici, ": 14,
    " Quindici, ": 15,
    " Sedici, ": 16,
    " Diciassette, ": 17,
    " Diciotto, ": 18,
    " Diciannove, ": 19,
    " Venti, ": 20,
    " 1 ": 1,
    " 2 ": 2,
    " 3 ": 3,
    " 4 ": 4,
    " 5 ": 5,
    " 6 ": 6,
    " 7 ": 7,
    " 8 ": 8,
    " 9 ": 9,
    " 10 ": 10,
    " 11 ": 11,
    " 12 ": 12,
    " 13 ": 13,
    " 14 ": 14,
    " 1, ": 1,
    " 2, ": 2,
    " 3, ": 3,
    " 4, ": 4,
    " 5, ": 5,
    " 6, ": 6,
    " 7, ": 7,
    " 8, ": 8,
    " 9, ": 9,
    " 10, ": 10,
    " 11, ": 11,
    " 12, ": 12,
    " 13, ": 13,
    " 14, ": 14,
    " 1. ": 1,
    " 2. ": 2,
    " 3. ": 3,
    " 4. ": 4,
    " 5. ": 5,
    " 6. ": 6,
    " 7. ": 7,
    " 8. ": 8,
    " 9. ": 9,
    " 10. ": 10,
    " 11. ": 11,
    " 12. ": 12,
    " 13. ": 13,
    " 14. ": 14,
    " I. ": 1,
    " II. ": 2,
    " III. ": 3,
    " IV. ": 4,
    " V. ": 5,
    " VI. ": 6,
    " VII. ": 7,
    " VIII. ": 8,
    " IX. ": 9,
    " X. ": 10,
    " XI. ": 11,
    " XII. ": 12,
    " XIII. ": 13,
    " XIV. ": 14,
    " XV. ": 15,
    " XVI. ": 16,
    " I, ": 1,
    " II, ": 2,
    " III, ": 3,
    " IV, ": 4,
    " V, ": 5,
    " VI, ": 6,
    " VII, ": 7,
    " VIII, ": 8,
    " IX, ": 9,
    " X, ": 10,
    " XI, ": 11,
    " XII, ": 12,
    " XIII, ": 13,
    " XIV, ": 14,
    " XV, ": 15,
    " XVI, ": 16,

}

ITALIAN_NUMBERS_ORDINAL = {
    " Primo": 1,
    " Secondo": 2,
    " Terzo": 3,
    " Quarto": 4,
    " Quinto": 5,
    " Sesto": 6,
    " Settimo": 7,
    " l'Ottavo": 8,
    " Ottavo": 8,
    " Nono": 9,
    " Decimo": 10,
    " l'Undecimo": 11,
    " Undecimo": 11,
    " Undicesimo": 11,
    " Dodicesimo": 12,
    " Duodecimo": 12,
    " Tredicescimo": 13,
    " Quattordicesimo": 14,
    " Quartadecima": 14,
    " Decimaquinta": 15,
    " Decimasettima": 17
}
