A repository for semi-structured representations of renaissance music publications.

The current project largely follows the Nuovo Vogel bibliography. Once enough data has been collected, the plan is to transform this metadata into a more common and formal datastructure.

##Reading the files
Each file consists of four primary parts:

1. The Nuovo Vogel numerical designation and a transcription of the frontispiece
2. A description of the physical attributes of original object (size, page counts, number of books, etc.)
3. A structured (tab-delineated) listing of each work in the publication, including text authors if known
4. A listing of institutions known to hold copies of the publication, including which specific parts are in their collection

###Reading the works table
For every work in the works list there are 6 data points, all separated by one or more tabs. Empty data-points are delineated with a ```-``` character.

The headings:
```
Number of voices	Text incipit	Comments from the source	Composer if not primary composer	Text author		Page number
```

Heading detail:

* __Number of voices__: Described in the Italian style, ie ```A 5``` for 5 voices. If a ```-``` ever appears in a voice data point, the number of voices for that work is assumed to be whatever the most recent given value was. Often a listing will only have a written-out value for the first work, with the remainder ```-```, meaning that all works are 5 voices.
* __Text incipit__: The first line of text in the piece. If the work is one of a multi-piece set, then its number in that set precedes the incipit. E.g. ```1. Cruda amarilli [...]```.
* __Comments from source__: If the source contains any comments for that work, such as part number or dedicatee, then that information appears here.
* __Composer__: Only populated if the composer for the piece is not the primary composer of the publication. Otherwise its value is ```-```.
* __Text author__: The author of the text set for the work. Often unknown (and given a ```-``` value)
* __Page number__: The page number at which the work begins, most often taken from the Canto book.

Here is an example row from the works table (with completely made up values):
```
A 5		1. Dunque romper la fè, dunque deggio io lasciar Alcippo mio	Prima parte		Orlando di Lasso	Francesco Petrarca		12
```