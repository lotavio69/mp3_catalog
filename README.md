# The MP3 Catalog Project

This document attempts to decribe the development plan for the MP3 catalog project. The main goal is to convert my colletion of 20+ years of MP3 to a database, and then reorganize my Amazon files in the same fashion, but with legal files, that contain all the ID3 fields as they are supposed to be displayed.

## How to get there

The components of the process so far are:

* List all the files in the old directory structure
* Create a database containing at least file paths, and then the existing ID3 information as additional columns in the table
* Run mpck to check files for Layer information and issues with files, add that to the DB as additional columns per record
* For files that could not be re-obtained from Amazon, use mp3val to fix them. Ensure "fix" does not destry mp3 data or make the file unplayable.
* Find a way of identifying songs that are not complete and end abruptly.

## Tools used for this process

* Python as the programming language
* MongoDB as the database
* PyMongo as the library to connect both
* mpck as the tool to check files info and issues
* mp3val as the MP3 fix tool
