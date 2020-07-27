'''
Unclear Objective:
Data of XYZ company is stored in sorted list. Write a program for searching 
specific data from that list.
'''

Data = []

def search(query):
    return True if query in Data else False

search(str(input('>')))