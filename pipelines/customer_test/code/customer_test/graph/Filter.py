from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_test.config.ConfigStore import *
from customer_test.functions import *

def Filter(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("country_code") == lit(Config.country_code)))
