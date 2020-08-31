A simple, locally-saved reimplementation of Anki.

For several years I have been a heavy user of [Anki](https://apps.ankiweb.net) to help me remember what I study.

However, sometimes I am unable to add information I would like - typically, information protected as intellectual property, which should not leave the originating network. This very simple Anki clone solves this problem by running locally on the machine.

## Quickstart
`python anki_lite.py`

Every run of anki-lite will first allow the user to add new questions if desired. After this, all cards that are due will be presented for review.

## Details
For simplicity, a csv file (`data.csv`) is used as the the database.

Whenever the program is run:
* `data.csv` is updated as required
* A new backup of the database is stored in the `backups` folder
* Metadata (run time, run duration) is stored in `backups/meta.csv`.

A card will be reviewed if:
* The last review was incorrect
* Card has never been reviewed
* Card correctly reviewed once & last review more than 5 minutes ago
* Card correctly reviewed twice & last review was yesterday or earlier
* Card correctly reviewed x  times (where `x >= 3`) & `log_base_2(current date - review date) > x - 1`
