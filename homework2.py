"""
Author: Liang-Shih Lin
Description: A file containing variables representing my favourite song.
"""

# Homework 1
# Details of the song
Name = "What A Catch, Donnie"
Artist = "Fall Out Boy"
Album = "Flie a Deux"
Duration = (4 * 60) + 51
Genre = [
    'Alternative Rock',
    'Pop punk',
    'Pop rock',
    'Pop',
    'Emo pop',
    'Emo'
]
Year = 2008
WrittenBy = [
    "Andrew Hurley",
    "Joe Trohman",
    "Patrick Stump",
    "Pete Wentz"
]
ProducedBy = "Neal Avron"

# Displaying of the details
print(Name)
print(Artist)
print(Album)
print(Genre)
print(Year)
print(Duration)
print(WrittenBy)
print(ProducedBy)

# Homework 2

def genre():
    return Genre

def artist():
    return Artist

def year():
    return Year

def favourite():
    return True

print(genre())
print(artist())
print(year())
print(favourite())
