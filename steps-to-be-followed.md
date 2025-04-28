################################################################################################# 
# Tools to be Installed
#################################################################################################

# 1. Install Visual Studio Code (Editor)
- Download and install Visual Studio Code from [https://code.visualstudio.com/](https://code.visualstudio.com/).

# 2. Install Git (Version Control System)
- Download and install Git from [https://git-scm.com/](https://git-scm.com/).

# 3. Set up GitHub (For Git Repositories)
- Create an account or log in to [GitHub](https://github.com/).

# 4. Install Java JDK
- Download Java JDK 17 from [Oracle's website](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html).
- Set environment variables:
   - `JAVA_HOME`: Path to the Java installation directory (e.g., `C:\Program Files\Java\jdk-17\`).
   - Add `%JAVA_HOME%\bin` to the `PATH` variable.

# 5. Install Python
- Download and install Python from [https://www.python.org/](https://www.python.org/).
- Add Python to the `PATH` (e.g., `C:\python`).

# 6. Install Jupyter Lab
- Open a terminal and run:
   ```bash
   pip install jupyterlab
   pip install notebook
   ```

# 7. Install PySpark
- Open a terminal and run:
   ```bash
   pip install pyspark
   ```

# 8. Install Numpy and Pandas
- Open a terminal and run:
   ```bash
   pip install numpy
   pip install pandas
   ```

# 9. Install Matplotlib
- Open a terminal and run:
   ```bash
   pip install matplotlib
   ```

# 10. Install Scikit-Learn
- Open a terminal and run:
   ```bash
   pip install scikit-learn
   ```

# 11. Install Flask
- Open a terminal and run:
   ```bash
   pip install flask
   ```

# To Test:
- Use [Postman](https://www.postman.com/) or `curl` to test your setup:
   ```bash
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"rooms": 2, "area": 5000}'
   ```

# For Kubernetes Deployments
$ kind version
$ kind get clusters
$ kind create cluster --name main-k8s-cluster
$ kubectl version
$ kubectl get pods
$ kubectl get nodes -o wide
$ kubectl get deployments
$ kubectl get services

# To create Pods/Deployments/Services
$ kubectl apply -f manifests
$ kubectl port-forward svc/kumarns-mlapp-service 7000:6000

##############################################################################
USING JENKINS FOR 00_USING_KUBERENTES
##############################################################################

# USE JENKINS 
- Create Job2
 - Task1:
    $ python model.py
  - $ aws s3 cp model/rental_prediction_model.pkl s3://<bucket-name>>/model/rental_prediction_model.pkl 

 - Task2:
   $ docker build . -t <<dockerhub-name>>/<<registry-name>>  
   $ docker push <<dockerhub-name>>/<<registry-name>>:latest

# USE JENKINS
- Create Job2
 - Task1:
    $ kubectl delete -f manifests/

 - Task2:
    $ kubectl apply -f manifests/


##############################################################################
USING JENKINS FOR 01_USING_KUBEFLOW
##############################################################################

# USE JENKINS FOR KUBEFLOW
- Create Job1 : 01-build-model-using-kubeflow

 - Task1: (Model Download)
   $ cd 01_using_kubeflow
   $ mkdir model
   $ python model.py
   $ aws s3 cp s3://sigma-bucket-us-east-2/model/rental_prediction_model.pkl model/rental_prediction_model.pkl


 - Task2: (Docker Build)
   $ cd 01_using_kubeflow
   $ docker build . -t ssadcloud/mlapp
   $ docker push ssadcloud/mlapp:latest

# USE JENKINS
- Create Job2
 - Task1:
    $ cd 01_using_kubeflow
    $ kubectl delete -f manifests/

 - Task2:
    $ cd 01_using_kubeflow
    $ kubectl apply -f manifests/

=================================================================================
# Loggging and Monitoring with Prometheus and Grafana
=================================================================================

- For Prometheus Installation
 $ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
 $ helm repo update
 $ helm install main-prometheus prometheus-community/prometheus


NAME: main-prometheus
LAST DEPLOYED: Sat Apr 26 05:20:55 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The Prometheus server can be accessed via port 80 on the following DNS name from within your cluster:
main-prometheus-server.default.svc.cluster.local


Get the Prometheus server URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=main-prometheus" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace default port-forward $POD_NAME 9090


The Prometheus alertmanager can be accessed via port 9093 on the following DNS name from within your cluster:
main-prometheus-alertmanager.default.svc.cluster.local


Get the Alertmanager URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=alertmanager,app.kubernetes.io/instance=main-prometheus" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace default port-forward $POD_NAME 9093
#################################################################################
######   WARNING: Pod Security Policy has been disabled by default since    #####
######            it deprecated after k8s 1.25+. use                        #####
######            (index .Values "prometheus-node-exporter" "rbac"          #####
###### .          "pspEnabled") with (index .Values                         #####
######            "prometheus-node-exporter" "rbac" "pspAnnotations")       #####
######            in case you still need it.                                #####
#################################################################################


The Prometheus PushGateway can be accessed via port 9091 on the following DNS name from within your cluster:
main-prometheus-prometheus-pushgateway.default.svc.cluster.local


Get the PushGateway URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus-pushgateway,component=pushgateway" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace default port-forward $POD_NAME 9091

For more information on running Prometheus, visit:
https://prometheus.io/


# For GRAFANA

$ helm repo add grafana https://grafana.github.io/helm-charts
$ helm repo update
$ helm install main-release grafana/grafana

NAME: main-release
LAST DEPLOYED: Sat Apr 26 05:24:59 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
1. Get your 'admin' user password by running:

   kubectl get secret --namespace default main-release-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
   
2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

   main-release-grafana.default.svc.cluster.local

   Get the Grafana URL to visit by running these commands in the same shell:
     export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=main-release" -o jsonpath="{.items[0].metadata.name}")
     kubectl --namespace default port-forward $POD_NAME 3000

3. Login with the password from step 1 and the username: admin
#################################################################################
######   WARNING: Persistence is disabled!!! You will lose your data when   #####
######            the Grafana pod is terminated.                            #####
#################################################################################













####################################################################################
# Commonly Used API From Kubeflow Pipelines
####################################################################################
list_of_apis.py
   ```python

   # Library Imports
   import kfp
   import logging

   # Configure logging
   logging.basicConfig(level=logging.INFO)

   # Set your Kubeflow Pipelines endpoint here
   kfp_endpoint = None
   client = kfp.Client(host=kfp_endpoint)

   # Experiment name
   experiment_name = "My Experiment"

   # Create a new experiment
   def create_experiment(client, experiment_name):
      experiment = client.create_experiment(name=experiment_name)
      logging.info(f"Created experiment: {experiment.name}")
      return experiment


   # List all experiments
   def list_experiments(client):
      experiments = client.list_experiments()
      logging.info(f"Experiments: {experiments}")
      return experiments

   # Create a Run from a pipeline function
   def create_run_from_pipeline_func(client, pipeline_func, experiment_name, enable_caching=False):
      run = client.create_run_from_pipeline_func(
         pipeline_func,
         experiment_name=experiment_name,
         enable_caching=enable_caching
      )
      logging.info("Pipeline run initiated")
      return run

   # List all runs for a given experiment
   def list_runs(client, experiment_id):
      runs = client.list_runs(experiment_id=experiment_id)
      logging.info(f"Runs: {runs}")
      return runs

   # Delete a specific run by run_id
   def delete_run(client, run_id):
      client.delete_run(run_id)
      logging.info(f"Deleted run: {run_id}")

   # List all runs for a given experiment and delete the first run
   def delete_previous_run(client, experiment_id):
      runs = list_runs(client, experiment_id)
      if runs and runs.runs:
         run_id = runs.runs[0].run_id
         logging.info(f"Deleting run: {run_id}")
         delete_run(client, run_id)

   # Delete a specific experiment by experiment_id
   def delete_experiment(client, experiment_id):
      client.delete_experiment(experiment_id)
      logging.info(f"Deleted experiment: {experiment_id}")


   # Example usage
   # experiment = create_experiment(client, "New Experiment")
   # experiments = list_experiments(client)
   # runs = list_runs(client, experiment.experiment_id)
   # delete_run(client, runs.runs[0].run_id)
   # delete_previous_run(client, experiment.experiment_id)
   # delete_experiment(client, experiment.experiment_id)

   ```
