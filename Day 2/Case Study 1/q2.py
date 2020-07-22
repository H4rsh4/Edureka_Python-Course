'''
Obj:
    Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.

Assuming the input is structured as : "A C B F"
'''
query = str(input('>'))
#->The following statement SPLITs the given string with the given seperator(' ') and returns a list of spliced blocks
#-> and then SORTs alphabetically -> Then the elements of the list are printed with space seperation
print(' '.join(sorted(query.split(' '))))

