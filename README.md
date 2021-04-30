# Sparkjob Dataproc
The problem in this project is “How can we process a huge amount of data automatically without writing a script repeatedly?”. With a huge amount of data from local computer, we should transform the data and store them into BigQuery as the Data Warehouse

# Overview

**The workflow for this sparkjob with dataproc**

![image](https://user-images.githubusercontent.com/71366136/116716945-89979000-aa02-11eb-8333-ce14bf6a1ae9.png)

The data is about flight record contains:
* `flight_date `
* `airline_code`
* `flight_num`
* `source_airport`
* `destination_airport`
* `departure_time`
* `departure_delay`
* `arrival_time`
* `arrival_delay`
* `airtime`
* `distance`
* `id`

I do some action with the data
* Cause the data come from past, I change the `flight_date` to current date, also save it with the new name, **one day after the `flight_date`**
* I do simple process to obtain the information whether the airport categorized as `most_come_from` and `most_visited`

**And then the data is processed into bigquery by sparkjob**


# Installation
Clone this repository

```
git clone https://github.com/Jomen034/dataproc-sparkjob.git
```

To be able to work with this repo, do the following steps:
1. Create free trial [GCP](https://cloud.google.com/) account
2. Enable the **Cloud Dataproc APIs**
3. Install the [Google Cloude SDK](https://cloud.google.com/sdk/docs/install) to be able work with your GCP Console from your command prompt
4. Set your gcloud SDK by running `gcloud init`. Just follow the steps after that
6. Set up is done

# Usage
* Go to the directory you saved this cloned repo. 
* Open the gcloud sdk terminal
* execute the `bash_script.sh`
* That script will do several jobs below:
  * create the `new_dataset` folder
  * run the `transform_data.py` to do transformation on the data
  * load the result to your GCS Bucket
  * create cluster on dataproc
  * submit the sparkjob
  * delete the cluster
 
If all is going well, you will see this output:

**The bash script executed well**

![image](https://user-images.githubusercontent.com/71366136/116719611-75a15d80-aa05-11eb-9ba1-af4f8be54eaa.png)

If running well, then the cluster will be deleted. And it will ask you to continue deleting the cluster or not. 


**And now, go to the GCP console and check your bigquery table**

![image](https://user-images.githubusercontent.com/71366136/116691063-7ece0280-a9e4-11eb-80e7-5434ffcc2137.png)


# Conclusion
* with **sparkjob**, the jobs are being processed with parallel processing to save more time 
* Meanwhile, **dataproc** is a managed Spark and Hadoop service that lets you take advantage of open source data tools for batch processing, querying, streaming, and machine learning. Dataproc automation helps you create clusters quickly, manage them easily, and save money by turning clusters off when you don't need them.
