from shlex import split


def read_file_content(filename):
    filename = open('story.txt', 'r')
    print(filename.read())
    filename.close
    
read_file_content('story.txt')



def count_words():
    text = open('story.txt', 'r')
    letter = split(text)
    dict = {}
    for x in letter:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
            
    print (dict)
    
count_words()
        
        
        
    