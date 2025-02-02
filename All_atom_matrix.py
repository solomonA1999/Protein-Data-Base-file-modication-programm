from source_scripts import Generating_atom_files, get_pdb, matrix_creation, user_input, get_coords

# main() function prevents module from instantly executing 
def main():
    ''''Creates distance matrix of all atoms'''
    pdb_code = user_input()

    get_pdb(pdb_code)

    All_atom_coordinates = get_coords(pdb_code)

    Matrix = matrix_creation(All_atom_coordinates)

    Generating_atom_files(Matrix)
    
    
    if __name__ == '__main__':
        main()
          