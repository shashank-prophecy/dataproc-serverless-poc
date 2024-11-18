from beta_shashank_dataproc_serverless_poc_dataproc_serverles.utils import *

@task_wrapper(task_id = "DataprocPipeline_0")
def DataprocPipeline_0(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.google.cloud.operators.dataproc import DataprocCreateBatchOperator
    job_metadata = {
        "reference": {"project_id" : "prophecy-field"}, 
        "placement": {"cluster_name" : "hadoop-cluster-iceberg-5"}, 
        "pyspark_job": {
          "python_file_uris": ["gs://prophecy-public-gcp/prophecy-python-libs/prophecy_libs-1.9.16-py3-none-any.whl",                                 "gs://prophecy-public-gcp/prophecy-python-libs/pyhocon-0.3.60-py3-none-any.whl",                                 "gs://prophecy-public-gcp/prophecy-python-libs/pyparsing-3.1.0-py3-none-any.whl",                                 "gs://dataproc-cluster-bucket-prophecy/prophecy/artifacts/newbeta1/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customer_test-1.0-py3-none-any.whl",                                 "gs://dataproc-cluster-bucket-prophecy/prophecy/artifacts/newbeta1/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customer_test/launcher.py"], 
          "main_python_file_uri": "gs://dataproc-cluster-bucket-prophecy/prophecy/artifacts/newbeta1/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customer_test/launcher.py", 
          "properties": {
            "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/dataproc_serverles", 
            "spark.prophecy.metadata.is.interactive.run": "false", 
            "spark.prophecy.metadata.fabric.id": "195", 
            "spark.prophecy.tasks": "H4sIAAAAAAAAAKuuBQBDv6ajAgAAAA==", 
            "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
            "spark.prophecy.metadata.user.id": "81", 
            "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
            "spark.prophecy.execution.metrics.disabled": "true", 
            "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
            "spark.prophecy.execution.service.url": "wss://beta.prophecy.io/execution/eventws"
          }, 
          "args": ["-i", "testing", "-O", "{\"country_code\":\"RU\"}"], 
          "jar_file_uris": ["gs://prophecy-public-gcp/prophecy-scala-libs/prophecy-libs-assembly-3.3.0-8.2.1.jar"], 
          "file_uris": []
        }
    }
    serverless_job = {
        "pyspark_batch": {
          "main_python_file_uri": job_metadata["pyspark_job"].get("main_python_file_uri", ""),
          "python_file_uris": job_metadata["pyspark_job"].get("python_file_uris", []) + [],
          "jar_file_uris": job_metadata["pyspark_job"].get("jar_file_uris", []) + [],
          "args": job_metadata["pyspark_job"].get("args", []),
        },
        "runtime_config": {
"container_image" : None, "version" : "1.2", },
        "environment_config": {
          "execution_config": {
"service_account" : "prophecy-field-bq-fabric@prophecy-field.iam.gserviceaccount.com", }
        },
    }

    return DataprocCreateBatchOperator(
        task_id = "DataprocPipeline_0",
        batch = serverless_job,
        batch_id = "test-batch-prophecy",
        region = "us-central1",
        project_id = "prophecy-field",
        gcp_conn_id = "google_cloud_default",
    )
