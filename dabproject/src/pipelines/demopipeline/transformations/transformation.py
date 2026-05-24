import dlt

@dlt.table
def transfomrmed():
    return spark.range(10)