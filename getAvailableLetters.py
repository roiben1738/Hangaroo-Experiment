def getAvailableLetters(lettersGuessed):
  

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 

                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    

    for x in lettersGuessed:
        
        
        
    
        alphabet.remove(x)
        
    return ' '.join(alphabet)
       

