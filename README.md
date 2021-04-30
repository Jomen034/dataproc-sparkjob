# Sparkjob Dataproc
The problem in this project is “How can we process a huge amount of data automatically without writing a script repeatedly?”. With a huge amount of data from local computer, we should transform the data and store them into BigQuery as the Data Warehouse

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

![image](https://user-images.githubusercontent.com/71366136/116690946-56de9f00-a9e4-11eb-92f0-d689acd94b07.png)

**Check your bigquery table**

![image](https://user-images.githubusercontent.com/71366136/116691063-7ece0280-a9e4-11eb-80e7-5434ffcc2137.png)

