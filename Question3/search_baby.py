
import importlib
import subprocess
import sys

def install_packages():
    package = ['regex']
    for p in package:
        try:
            importlib.import_module(p)
            print(f'{p} is already installed')
        except ImportError:
            print('Standby for Installation of required packages')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', p])

import re
html = None

# Please adopt use of path as reciding in your file manager.
path_to_html_file = 'C:/Users/USER/2nd Contact Session Assign/Question3/baby2008.html'

with open(path_to_html_file, 'r') as file:
    if file:
        html = file.read()
        
items = re.findall(r'<tr align="right"><td>(\d+)</td><td>(.*?)</td><td>(.*?)</td>\n</tr>', html)

items_dict = [
    {
        'rank':i[0],
        'male_name':i[1],
        'female_name':i[2],
    }
    for i in items
]


class Note:
    def __init__(self, rank, male, female):
        self.rank = rank
        self.male = male
        self.female = female
        
    def __str__(self):
        return f'\nRank = {self.rank} \nMale = {self.male} \nFemale = {self.female}'
        
        

def sort_merger(ar, kw):
    if len(ar) <= 1:
        return ar
    
    mid = len(ar) // 2
    
    left = sort_merger(ar[:mid], kw)
    right = sort_merger(ar[mid:], kw)
    
    return merge(left, right, kw)



def merge(left, right, kw):
    result = []
    
    while left and right:
        if left[0][kw].lower() <= right[0][kw].lower():
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    result.extend(left)
    result.extend(right)
            
    return result



def binary_search(ar, target, kw):
    low = 0
    high = len(ar) -1
    
    while low <= high:
        mid = (low + high) // 2
        if ar[mid][kw].lower() == target.lower():
            return ar[mid]
        
        elif ar[mid][kw].lower() < target.lower():
            low = mid + 1
        
        else:
            high = mid - 1
            
    return -1



def main():
    install_packages()
    
    while True:
        kw = None
        jd = None
                
        print('\nThis is a Sort and Search app, Welcome')
        print('1. Sort through the list')
        print('2. Search through the list')
        print('3. Quit')
        value = input("Choose from '1-3': ")
        
        if value == '3':
            break
        
        if value == '1' or value == '2':
            while True:
                if value == '1':
                    print('\n1. Sort by Rank')
                    print('2. Sort by Male Name')
                    print('3. Sort by Female Name')
                elif value == '2':
                    print('\n1. Search by Rank')
                    print('2. Search by Male Name')
                    print('3. Search by Female Name')
                    
                print('4. Back to main menu')
                jd = input("Choose from '1-4': ")
                
                if jd == '4':
                    break
                
                if jd == '1':
                    kw = 'rank'
                    break
                elif jd == '2':
                    kw = 'male_name'
                    break
                elif jd == '3':
                    kw = 'female_name'
                    break
                
                else:
                    print('Invalid option, try again')
                    continue
        else:
            print('Invalid input, try again.')
            continue
                
        
        if value == '1':
            if kw is not None:
                sorted = sort_merger(items_dict, kw)
                for i in sorted:
                    note = Note(i.get('rank'), i.get('male_name'), i.get('female_name'))
                    print(note)
                
        elif value == '2':
            if kw is not None:
                target = None
                
                if kw == 'rank':
                    target = input('Pick a rank to search for: ')
                else:
                    target = input('Type a name to search for: ')
                
                sorted = sort_merger(items_dict, kw)
                search = binary_search(sorted, target, kw)
                if search == -1:
                    continue
                
                note = Note(search.get('rank'), search.get('male_name'), search.get('female_name'))
                
                print("\nSearch Result:")
                print(note)



if __name__ == "__main__":
    main()