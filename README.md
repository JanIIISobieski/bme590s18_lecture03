# README

The program reads the individual CSV files, concatenates them, and then combines them into one large CSV file.
Team names are analyzed for spaces and for being in CamelCase.
CSV files of the wrong shape are not imported.
Ignored CSV files are not imported.
Additionally, a JSON file is created for each individual CSV file of the right shape. 

## Program organization

This program is organized such that the Python files reside
in one directory, the CSV files in another, and the JSON files
in another. The program handles both reading from and writing to
the appropriate directory. By definition, the CSV and JSON directories
are located one level up from the `compile_class_info.py` program.

## Exceptions

1. This program allows for exceptions to the imported files.
Every `filename.csv` that matches a `filename.csv` added to the `name_exceptions` variable will not be imported. 
Files that were ignored in this manner will be printed to STDOUT to let the user know that 
a file was ignored and not imported.

2. Each imported CSV file is checked for the appropriate size (five entries). If an imported
file is not of the right size, it is ignored and a message is written to the STDOUT that
`filename.csv has wrong shape`.


## Analysis of CSV files

1. The program attempts to find spaces in team names. Trailing spaces after the comma delimiter
are ignored. If a team name contains a non-leading space, it is written to STDOUT that
`filename.csv team name contains a space`.

2. The program counts the occurrence of CamelCase in team names. CamelCase is defined as the presence
of both lower and upper case characters in the team name. A single-word name like "Team" would be considered
to be in CamelCase by the program, but "team" or "TEAM" would not be. "AwesomeTeam" contains both upper and lower
case characters, and would be identified to be in CamelCase. An exception is that a team name such as "tEAM" 
would also be considered CamelCase by the program, though this team name is obviously not in CamelCase.

