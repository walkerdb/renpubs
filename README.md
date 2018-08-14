A repository for semi-structured representations of renaissance music publications. Scope for the inital part of this project
is limited to the publications described in the Nuovo Vogel series.
 
### Data structure

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