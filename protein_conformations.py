from source_scripts import Average_protein_structure, get_pdb

# main() function prevents module from instantly executing 
def main():
    '''Allows the user to select 1 of 4 pdb files and create altered pdb file with average distances of all atom models'''
    
    print('\n' + 'There are 4 pdb files that have mutliple structure please select one.' + '\n')
    print('1 - 2ita - PufX from Rhodobacter sphaeroides')
    print('2 - 2dw3 - Rhodobacter sphaeroides PufX membrane protein')
    print('3 - 7acs - SARS-CoV-2 nucleocapsid phosphoprotein N-terminal domain in complex with 7mer dsRNA')
    print('4 - 2m7e - Calmodulin-binding domain of plant calcium-ATPase ACA2')
    
    #Allows the user to make a selection of 4 pdb files to find the average atom distances
    # 1-3 have mutliple models and 4 has only one where the atom distance is
    
    while True:
        choice = input('Enter choice (1/2/3/4): ')
        if choice in ('1','2','3','4'):

            if choice == '1':
                choice_1 = '2ita'
                get_pdb(choice_1) 

                Average_protein_structure(choice_1)    

            elif choice == '2':
                choice_2 = '2dw3'
                get_pdb(choice_2)

                Average_protein_structure(choice_2)    
            
            elif choice == '3':
                choice_3 = '7acs'
                get_pdb(choice_3) 

                Average_protein_structure(choice_3)   
            
            elif choice == '4':
                choice_4 = '2m7e'
                get_pdb(choice_4) 

                Average_protein_structure(choice_4)
            
            #Allows the user to select if they want to find out the average protein structure of the same protein or different 
            next_choice = input('Do you want to try another pdb? (y/n): ' + '\n' )
            if next_choice == 'y':
                continue
            
            elif next_choice == 'n':
                break  
                
        else:
            print('Invalid input')

    if __name__ == '__main__':
        main()