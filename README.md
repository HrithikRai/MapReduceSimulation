# MapReduceSimulation
A demonstration of MapReduce to be run in local Python IDE...
Please find the dataset here[https://github.com/CodeMangler/udacity-hadoop-course/blob/master/Datasets/purchases.txt.gz]

Playing around with BigData should be an Integral part of Data Science. 

* If you are familiar with Hadoop, you know it is mainly made up of MapReduce and HDFS. 
* HDFS keeps track of data blocks through data nodes and name node. 
* MapReduce does the heavy job of compressing the Data and giving you your insights.

## MapReduce :

* First a mapper will map your requirements in a key,value pair. The output is called Intermediate Records.
* A shuffle and sort will arrange the output data from the mapper.
* The sorted data is now presented to the reducer which will do the required mathematical operation and give the user, the insights needed.

### Setting up a Hadoop ecosystem requires a Azure account or a local hadoop installation on virtual machine. This program will directly run on your local python IDE. Just download the dataset in your home directory of python and run !

#### NOTE - There are three functions in the program. You are advised to run them one by one to better understand the process.
