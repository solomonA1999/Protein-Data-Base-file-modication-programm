 User guide 


Number of files: 6
Name of files: Main_script.py, All_atom_matrix.py, Calpha_matrix.py, protein_confomrations.py, chain_renaming.py and source_scripts.py

Modules

The modules required for the scripts to run are listed below followed by their download instruction pages. 
    • Biopython -https://biopython.org/wiki/Download 
    • numpy - https://numpy.org/install/
    • sklearn -https://scikit-learn.org/stable/install.html
        ◦ Recommended method of install either:
            ▪ sudo apt-get install python3-sklearn
            ▪ pip3 install -U scikit-learn
    • matplotlib - https://matplotlib.org/3.4.3/index.html


How to use the scripts

The user will only have to run 1 script ‘Main_script.py’.
$ python3  Main_script.py

This script will give the user the options to run 1 of 4 scripts at a time that have specific functionalities that save their outputs into the outputs folder. After the user has entered a pdb identifier code or inputted a specific letter or number hit enter to continue

Selection 1 -Atom distance matrix of a pdb file
	Asks for the user to input a protein pdb identifier (enter a 4 digit pdb identifier code) 	and creates a distance matrix of all atoms in the specified pdb file. Creates a .csv of 	the distance matrix in the outputs folder and saves a visualisation of the distance 	matrix as a .png . A pop up window with the visualisation of the distance matrix also 	appears.

Selection 2 – C Alpha distance matrix of a pdb file
	Asks for the user to input a protein pdb identifier (enter a 4 digit pdb identifier code) 	and creates a distance matrix of C alpha atom of the first chain in the specified pdb 	file. Creates a .csv of the distance matrix in the outputs folder and saves a 	visualisation of the distance matrix as a .png. A pop up window with the visualisation 	of the 	distance matrix also appears.

Selection 3 – Chain renaming of pdb file 6gch
	Asks the user to select a single character to replace the specified chain ID for the 3 	chains in the pdb file. Typing “x” keeps the chain id the same.  After 3 inputs have 	been given, a message of what chain names will be kept and changed will appear 	followed by the pdb file being saved to the outputs folder, the pdb file contains all 	the atoms with the user input edits. Chain names can be changed to number or 	letters apart from “x”




Selection 4 -  Computing average protein structure with multiple models
	Provides the user with a list of 4 pdb files that have multiple models. User can select 	the 1 of the 4 pdb files by typing the numbers 1-4 and hitting enter. Depending on 	selection the script will load the pdb file and compute the average protein structure. 	After computation the output file is saved as a pdb file containing the atom entries 	with the average computed coordinates and is saved to the outputs folder.

The source script contains a number of functions that are called by the 4 above.

    1.  user_input – asks the user to input 4 character PDB identifier code
       
    2.  get_pdb(x) – using the user input retrieves the specified PDB
       
    3.  get_coords(x) – using the specified PDB, retrieves atom coordinates of the retrieved pdb file (retrieved using get_pdb)
        
    4. Calpha_matrix(x) – creates a distance matrix of C alpha atom using the first chain of the pdb file
       
    5.  matrix_creation(x) – creates a distance matrix from the atom coordinates retrieved from get_coords and Calpa_matrix
       

    6.  Generating_CA_files(x) – generates output files, .csv and .png 
       
    7.  Generating_atom_files(x) – generates output files, .csv and .png
       
    8. Average_protein_structure(x) – computes the average atom distances of a selected pdb file and saves the newly edited atom entries as a .pdb 
       
    9.  chain_renaming(x) – renames the chain id of pfb file 6gch


Data flow

The data flow and interaction between scripts is demonstrated below ← → represent the flow of data.

User input →

	 	←  Main_script.py →
	
						      ← All_atom_matrix.py, → 
						      ← Calpha_matrix.py, →
 						      ← protein_confomrations.py  →
						      ← chain_renaming.py →

										       ← source_scripts.py

		
