## PEGASUS PreTrained On Arxiv


### General Information

- You can find the official pegasus model [here](https://github.com/google-research/PEGASUS)
- This model is fine tuned for abstract generation for a subset of the arxiv dataset.
- This model gives an average rouge Score of 39.89 over the arxiv test dataset.

### Downloading the pre-trained Model

- Run the following command:

    ```bash
    pip install -r requirements.txt
    ```
- This will install all the pre-requisite libraries for the model.

> Note : It is recommended to create a virtual environment to install the libraries to avoid conflicts.

- After having installed all the models, download the folder from the following link: [PreTrained Model](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/hardik_sharma_students_iiit_ac_in/EpkoXlhASWJEtijThPecvSgBuvoQ12S-UbqyTAZfRt_lKw?e=jWFrUN)

- Make sure that there are three files in total, a `model.safetesnsor` file, and a couple of `.json` files.

- Now, you can run the script, and pass on the text of any research document you want summarized to the model.

- The `inference.py` file contains the relevant code whereas the `train.py` contains the code for training the model. You can use `test.py` to evaluate the $Rouge$ Scores of the pre-trained model on the arxiv dataset.

> Note : To run the test.py file, you need to have the arxiv dataset downloaded, it is not mandatory to do so, but you can find the link to the dataset used [here](https://drive.google.com/file/d/1b3rmCSIoh6VhD4HKWjI4HOW-cSwcwbeC/view). To also use the pubmed dataset, you can download it from [here](https://drive.google.com/file/d/1lvsqvsFi3W-pE1SqNZI0s8NR9rC1tsja/view)

### Running for inference

- The model expects the text from the research paper in a string format. The model then generates an abstractive summary from it.

### ReTraining The Model

- You can adjust the training parameters in the file training.py and train the model again custom to your use, this again requires you to have installed the relevant datasets mentioned above.
