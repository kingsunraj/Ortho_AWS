#@SunainaRajani
#This was created for AWS Blog Post authored by Sunaina Rajani:
#"Orthopedic Pathology Prediction Through Spinal-Pelvic Parameters Using Amazon Machine Learning"
#Data was downloaded from a publicly available spinal pathologies dataset 
#from the University of California, Irvine (UCI). 
#####**


import arff ## install Liac-arff module (https://pypi.python.org/pypi/liac-arff) that implements functions to read and write ARFF files in Python
import csv ## In order to write data to a CSV file for AWS S3 to read
from random import shuffle
data_dict = arff.load(open('column_2C_weka.arff', 'rb')) #Reading ARFF
data = data_dict["data"] #List of Datapoints only
shuffle(data) #Shuffle the patients within the dataset 
attributes_tup = data_dict["attributes"] #Extract attribute tuples
Attributes = []
for i in attributes_tup: #Extract only relevant attribute names
    for tup in i[::2]: 
        Attributes.append(tup)
Ortho_dataset= [Attributes]+ data

for row in Ortho_dataset: ## Changing to binary values : "Abnormal" to 1 and "Normal" to 0
    for i in row: 
        if i == "Abnormal":
            row.remove(i)
            row.append("1")
        if i == "Normal": 
            row.remove(i)
            row.append("0")


def writeCsvFile(filename, dataset): #Writing dataset to CSV 
    """
    @filename: string, filname to save it as
    @dataset: list of list of items

    Write data to file
    """
    mycsv = csv.writer(open(filename, 'wb'))
    for row in dataset:
        mycsv.writerow(row)

writeCsvFile('Ortho_dataset.csv', Ortho_dataset)



