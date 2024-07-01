AUTHOR NAME: Baptiste Humeau
DATE: 06/21/2024

This project is written entirely using jupyter notebook and python and therefore requires python to be installed on the user's machine.

-------------------------------------------------------------------------
DEPENDENCIES
-------------------------------------------------------------------------

Below is a full list of dependencies:

	jupyter 
	numpy
	tensorflow
	tkinter
	pillow
	matplotlib (if you wish to retrain the model and plot the evaluations)


-------------------------------------------------------------------------
FILE STRUCTURE
-------------------------------------------------------------------------

This .zip folder contains:

FILE: ModelTester.py ==> A python script to use the CNN model with the user's own input. 
NOTE: This file must be run from within a code editor. Command line will not work. 
Alternatively, the "working_files" folder contains a "ModelTester_Dialogue.ipynb" file that runs the same script.

FILE: Semester Project_Convolutional Neural Networks and Cloud Classification.pdf ==> The final report pdf for this project.

FILE: Demonstration.mp4 ==> A video rundown of the file structure and demonstration of the model being used.

FILE: README.txt ==> This file.

FOLDER: working_files ==> contains all .ipynb files used to process data and create the CNN model.
"Clouds2.ipynb" and "ModelTester_Dialogue.ipynb" are most relevant.

FOLDER: testImages ==> Cloud images gathered from the web and taken from the real world to test "ModelTester.py"

FOLDER: models ==> contains all the models iterations. Most current is "cloud_classification_model_simplified4.keras"
NOTE: Model names that contain "simplified" use 3 base classes. Otherwise, the model uses the original 11.
This is taken into account in the tester file.

FOLDER: CCSN_v2 ==> The original dataset from https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/CADDPD
		
FOLDER: CCSN_v3 ==> The dataset containing only cumulus, cirrus, and stratus clouds.

-------------------------------------------------------------------------
RUNNING INSTRUCTIONS
-------------------------------------------------------------------------

In Visual Studio Code, open the ModelTester.py file and run. This will take a moment (under a minute) to open. You will be prompted to 
browse to an image (I recommend using the images located in the testImages folder, browsing to your own cloud images in .jpg format).

Alternatively, assuming you have jupyter installed, you can:
	1. Open the directory in a terminal
	2. Run the command: jupyter notebook
	3. In the resulting browser, navigate to working_files > "ModelTester_Dialogue.ipynb"
	4. Run the only cell in this file
This will result in the same prompt as above.

In either of these files, it is possible to change the model to be used by changing the path of the 'model_name' variable. 
They are currently set to target 'cloud_classification_model_simplified4.keras,' which is the best performing model.

You can re-run any of the working files if you wish, but it is not necessary as the models are already trained and saved.







