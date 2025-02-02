from source_scripts import matrix_creation, user_input, CAlpha_matrix, get_pdb, Generating_CA_files

# main() function prevents module from instantly executing 
def main():
    """Creates C Alpha matrix from user input and saves outputs"""
    pdb_code = user_input()

    get_pdb(pdb_code)

    C_alpha_matrix_cooridnates = CAlpha_matrix(pdb_code)

    Matrix = matrix_creation(C_alpha_matrix_cooridnates)

    Generating_CA_files(Matrix)
    
    if __name__ == '__main__':
        main()
