from source_scripts import chain_renaming, get_pdb, user_input

# main() function prevents module from instantly executing 
def main():
    '''Allows the user to change or keep the chain id of the pdb file'''
    print('\n' + 'Chain renaming functionality' + '\n')


    pdb_code = '6gch'
    get_pdb(pdb_code)

    #Using user input to change chain name, if user specifies "n" then chain name is not changed
    chain_E = input('\n' + 'Please enter a single character to replace chain E. To keep E the same type "x" ')
    if chain_E == 'x':
        chain_E = ''
    chain_F = input('\n' + 'Please enter a single character to replace chain F. To keep F the same type "x" ')
    if chain_F == 'x':
        chain_F = ''
    chain_G = input('\n' + 'Please enter a single character to replace chain G. To keep G the same type "x" ')
    if chain_G == 'x':
        chain_G = ''

    print()

    #User input feeds into the dictionary with chain names
    new_chain_inputs  = {    
        'E': chain_E,
        'F': chain_F,
        'G': chain_G
    }
    #Chain id's are altered based of user inputs
    chain_renaming(new_chain_inputs)

    if __name__ == '__main__':
        main()
          