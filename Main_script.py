import Calpha_matrix 
import All_atom_matrix as atom_matrix
import chain_renaming
import protein_conformations
print('Select 1 of 4 scripts to run ' + "\n")

print('1. Atom distance matrix of a pdb file')
print('2. C Alpha distance matrix of a pdb file ')
print('3. Chain renaming of 6gch')
print('4. Computing average protein structure with multiple models')

while True:
    selection = input("\n"+ 'Please select 1 of the 4 scripts to run: ')
    if selection in ('1','2','3','4'):
        
        if selection == '1':
            atom_matrix.main()
        elif selection == '2':
            Calpha_matrix.main()
            
        elif selection == '3':
            chain_renaming.main()
        elif selection == '4':
            protein_conformations.main() 
            

        next_choice = input('Do you want to try another script? (y/n): ' + ('\n'))
        if next_choice == 'y':
            continue
        
        elif next_choice == 'n':
            break  
            
    else:
        print('Invalid selection')