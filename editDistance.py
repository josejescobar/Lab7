'''
Jose Escobar
UTEP ID 80536060
CS3 Lab 7: Edit Distance
'''


word1 = "money"
word2 = "monkey"




def editDistance(word1, word2, r1, r2):
    d = [[0 for x in range(r2 + 1)] for x in range(r1 + 1)] #Creates matrix
    #Loops make insertion, deletion and replacement operations
    for i in range(r1+1):
        for j in range(r2+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif word1[i-1] == word2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j],d[i-1][j-1])
    return d[r1][r2]
    
print("The result of Edit Distance method for words " + "'" + word1 + "'" + " and " + "'" + word2 + "'" + ": " + str(editDistance(word1, word2, len(word1), len(word2))))



