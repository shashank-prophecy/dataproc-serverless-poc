from airflow.decorators import task

db_pipeline_id_to_path_dict = {
    "pipelines/customer_test": "dbfs:/FileStore/prophecy/artifacts/newbeta1/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customer_test-1.0-py3-none-any.whl"
}
dp_pipeline_id_to_path_dict = {
    "pipelines/customer_test": "gs://dataproc-cluster-bucket-prophecy/prophecy/artifacts/newbeta1/cp/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customer_test-1.0-py3-none-any.whl"
}


def task_wrapper(task_id):

    def decorator(func):

        @task(task_id = task_id)
        def wrapper(*args, **context):
            ## running the actual method.
            return func(*args, **context).execute(context)

        return wrapper

    return decorator

pipeline_package_name = {"pipelines/customer_test" : "customer_test"}
