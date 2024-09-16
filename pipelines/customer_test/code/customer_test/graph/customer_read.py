from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_test.config.ConfigStore import *
from customer_test.functions import *

def customer_read(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/b29457372e98b68c8e1b4253dfcdcdaf/CustomersDatasetInput.csv")
