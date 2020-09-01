# A simple, locally-saved Anki clone
For several years I have been a heavy user of [Anki](https://apps.ankiweb.net) to help me remember what I study.
This usually works well, but sometimes I want to study something that should be kept in a closed system.

This very simple Anki clone solves the problem by running locally on a single machine.

## What is Anki?
Anki allows a user to study flashcards using spaced repetition.

Flashcards (each made up of a 'question' and an 'answer') are added to Anki and the user is periodically prompted to review them.
These reviews are scheduled at ever increasing time intervals.
For example, the first reviews of a card may take place after 1 day, 3 days, 5 days, 11 days, 25 days, and so on.

The only exception is if a review of a card is incorrect. In this case, the review frequency drops back to 1 day, so the card can be learnt from scratch.

To learn more, the [Anki](https://apps.ankiweb.net) website has excellent documentation.

## Quickstart
Clone the repo or copy `anki_lite.py` to your machine.

Add cards to the database using `python anki_lite.py --add` or `python anki_lite.py -a`.

Review all cards that are due for review using `python anki_lite.py --review` or `python anki_lite.py -r`.

## Implementation details
To reduce dependencies and to save time this project has been made as simple as possible.

A csv file (`data.csv`) is used as the the database.
To edit cards that have already been added, or delete them, simply edit this file.

Whenever the program is run:
* `data.csv` is updated as required
* A new backup of the database is stored in the `backups` folder
* Metadata (run time, run duration) is stored in `backups/meta.csv`

A card will be reviewed if:
* The last review was incorrect
* Card has never been reviewed
* Card correctly reviewed once & last review more than 5 minutes ago
* Card correctly reviewed twice & last review was yesterday or earlier
* Card correctly reviewed x  times (where `x >= 3`) & `log_base_2(current date - review date) > x - 1`
