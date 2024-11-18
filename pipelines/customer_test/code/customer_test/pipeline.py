from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from customer_test.config.ConfigStore import *
from customer_test.functions import *
from prophecy.utils import *
from customer_test.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customer_read = customer_read(spark)
    df_Filter = Filter(spark, df_customer_read)
    customer_write(spark, df_Filter)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("customer_test")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customer_test")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/customer_test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
