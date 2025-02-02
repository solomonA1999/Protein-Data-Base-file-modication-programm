import Bio.PDB
from Bio.PDB import PDBList
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB import PDBList, PDBParser, PDBIO
import numpy as np
from sklearn.metrics import pairwise_distances
from numpy.lib.npyio import savetxt
import matplotlib.pyplot as plt


def user_input():
    ''''Ask's the user for 4 character PDB identification'''
    global PDB_id
    PDB_id = input('Please enter 4 character PDB iD code ').lower()
    return PDB_id


def get_pdb(x):
    ''''Retrieves requested PDB from inputs'''
    #parser and Structure is made global as it is accessed through out the script
    global parser
    parser = PDBParser(QUIET=True)
    
    pdbl = PDBList()
    pdbl.retrieve_pdb_file( x , pdir='.', file_format='pdb')
    
    global structure 
    structure = parser.get_structure(x, 'pdb'+x+'.ent')
     

def get_coords(x):
    '''Retrieves all x, y and z coordinates for all atoms in pdb'''
    structure = parser.get_structure(x, 'pdb'+x+'.ent')
    #Creates empty list
    atom_coords = []
    #Accessing atom coordinates by looping through the pdb file
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    x = (atom.coord[0])
                    y = (atom.coord[1])
                    z = (atom.coord[2])
                    #Adds all the atom coordinates to the empty list above
                    atom_coords.append([x,y,z])
    return atom_coords


def matrix_creation(x):
    '''Creates distance matrix from atom coordinates'''
    #Making an multidimensional array from atom coordinates
    atom_matrix_array = np.array(x)
    #Pairwise_distances uses euclidean distance sqrt((x1-x2)^2+(y1-y2)^2+(z1-z2)^2)
    #to calculate distnaces
    output = pairwise_distances(atom_matrix_array)
    return output


def CAlpha_matrix(x):
    '''Creates distance matrix from C Alpha coordinates of the first protein chain'''
    #Creating empty lists
    atom_coordss = []
    chain_list = []

    #Loopping through the pdb to retrieve chain id's
    for chain in structure.get_chains():
        #Adds all chain id's to empty list
        chain_list.append(chain)
    
    #Makes the first chain id a string as it is a list 
    first_chain = str(chain_list[0])
    #Indexing to get the specific letter of the chain
    chain_letter = first_chain[10]
    
    #opens the retrieved PDB file
    with open('pdb'+PDB_id +'.ent') as file:
        content = file.readlines()
        #Looping through the pdb using the pdb columns
        #If line contain ATOM, CA and the first chain then store the coordinates in the empty list
        for lines in content:
            if lines[0:4] == 'ATOM':
                if lines[12:15] == ' CA':
                    if lines[21] == chain_letter: 
                        x = lines[30:37]
                        y = lines[38:45]
                        z = lines [46:53]
                        atom_coordss.append([x, y, z])
    return atom_coordss


def Generating_CA_files(x):
    '''Generates output files and saves them to the outputs folder'''

    #Saves C Alpha distance matrix as a csv file
    distance_matrix = savetxt('outputs/'+PDB_id+'_CA_distance_matrix.csv',x, delimiter=',')
    
    #Visualisation of the C alpha distance matrix using viridis
    plt.matshow(x)
    plt.colorbar()
    plt.xlabel('Atom number')
    plt.ylabel('Atom number')
    plt.savefig('outputs/'+PDB_id+'_CA_matrix.png')
    plt.show()
    return print('Files generated')


def Generating_atom_files(x):
    '''Generates output files and saves them to the outputs folder'''
    #Saves all atom distance matrix as a csv
    distance_matrix = savetxt('outputs/'+PDB_id+'_atom_distance_matrix.csv',x, delimiter=',')
    
    #Visualisation of the C alpha distance matrix using viridis
    plt.matshow(x)
    plt.colorbar()
    plt.xlabel('Atom number')
    plt.ylabel('Atom number')
    plt.savefig('outputs/'+PDB_id+'_atom_matrix.png')
    plt.show()
    return print('Files generated')


def Average_protein_structure(x):
    ''''Finds the average atom distance of a PDB file with multiple models'''
    # Creates a list of unique atom identifers that created from model the first model 'model 0'
    # while ignoring all hetero residues of a pdb file with 'if a.parent.id[0]
    atom_id = [a.parent.parent.id + '-' + str(a.parent.id[1]) + '-' +  a.name for a in structure[0].get_atoms() if a.parent.id[0] == ' '] 
    
    #Average atom distance of all models in the selected pdb file entered into the empty dictionary
    atom_averages = {}
    for all_atoms in atom_id:
        atom_averages[all_atoms] = []
        
        #Average atom distance calculated 
        for model in structure:
            atom_ = all_atoms.split('-')
            coordinates = model[atom_[0]][int(atom_[1])][atom_[2]].coord
            
            #Adds atom coordinates to the emtpy list
            atom_averages[all_atoms].append(coordinates)
        atom_averages[all_atoms] = sum(atom_averages[all_atoms]) / len(atom_averages[all_atoms])  

    #Creation of the new PDB file with average distance of atoms
    new_structure = Bio.PDB.StructureBuilder.Structure('id='+x) 
    
    #Adds the first model to the new structure and loops through the new structure while adding the atoms and the atom coordinates
    new_structure.add(structure[0])  
    for atoms in new_structure[0].get_atoms():
        chain = atoms.parent.parent
        residue = atoms.parent   
        #Removes the hetres from the new structure
        if residue.id[0] != ' ':
            chain.detach_child(residue)
        else:
            coordinates = atom_averages[chain.id + '-' + str(residue.id[1]) + '-' + atoms.name]
            atoms.coord = coordinates
    
    #Writing of the new PDB
    io = Bio.PDB.PDBIO()
    io.set_structure(new_structure)
    io.save('outputs/Average_'+x+'_protein_model.pdb')
    return print(f"Protein structure '{x}' average conformation saved")


def chain_renaming(x):
    '''Renames the chains of 6gch.pdb'''
    
    #Function input x is the dictionary where the user can select to change chain names
    #Looping through the PDB file and accessing chain id's of all atoms 
    for model in structure:
        for chain in model:

            #Allows user to rename the chain to a already used for a sibling of the entity
            chain.parent =None
            old_name = chain.get_id()
            new_name = x.get(old_name)
            if new_name:
                print(f"The following chain will be ranmed {old_name} to {new_name}")
                chain.id = new_name
            else:
                print(f"Keeping the following chain names: {old_name}")
    
    #Saves the PDB file atom entries with chain edits the user has specified
    io = PDBIO()
    io.set_structure(structure)
    io.save('outputs/6gch_chain_edit.pdb')
    return print("\n" + 'The ammended 6gch.pdb file has been saved' + "\n")