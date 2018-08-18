# Renaissance Vocal Music
A repository containing structured data detailing the contents of printed vocal part-books from the Renaissance. 
Scope for this project is limited to the publications described in the Nuovo Vogel series.

Current publication count: 622 / ~5100  
Total works: 16972
 
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
