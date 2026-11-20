import dlt

#### DimDate

@dlt.table
def dimdate_Stg():
    df = spark.readStream.table("spotify_cata.silver.dimdate")
    return df

dlt.create_streaming_table("dimdate")


dlt.create_auto_cdc_flow(
  target = "dimdate",
  source = "dimdate_Stg",
  keys = ["date_key"],
  sequence_by = "date",
  stored_as_scd_type = "2", 
  name = None, # optional
  once = False # optional
)