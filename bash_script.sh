#!/bin/bash
clear
echo "STARTING THE SCRIPT"
echo "MAKE new_dataset FOLDER"
mkdir new_dataset
echo "CREATING FOLDER DONE"
echo "RUN THE PYTHON SCRIPT TO DO SIMPLE TRANSFORMATION"
python transform_data.py
echo "TRANSFORMATION DONE... LOAD IT TO GCS BUCKET"
gsutil -m cp -r C:/Users/jomen/Documents/self_project/dataproc-sparkjob/new_dataset gs://week-3-spark-job-dataproc
echo "CREATE CLUSTER DATAPROC"
gcloud dataproc clusters create \
	--num-workers=2 \
	--master-machine-type=n1-standard-2 \
	--worker-machine-type=n1-standard-2 \
	--master-boot-disk-size=20 \
	--worker-boot-disk-size 20 \
	--enable-component-gateway \
	--optional-components=ANACONDA,JUPYTER \
	--zone=us-east1-b \
	--region=us-east1 \
	--image-version=1.3-ubuntu18 \
	jomen034-cluster
echo "CREATING CLUSTER DONE"
echo "SUBMIT SPARKJOB"
gcloud dataproc jobs submit pyspark sparkjob.py \
	--cluster=jomen034-cluster \
	--region=us-east1 \
	--jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar
echo "SUBMITING SPARKJOB DONE"
echo "NOW DELET THE CLUSTER"
gcloud dataproc clusters delete jomen034-cluster --region=us-east1
echo "DELETING CLUSTER DONE"
echo "END OF THE SCRIPT"