import dlt

#### FactStream

@dlt.table
def factstream_Stg():
    df = spark.readStream.table("spotify_cata.silver.factstream")
    return df

dlt.create_streaming_table("factstream")


dlt.create_auto_cdc_flow(
  target = "factstream",
  source = "factstream_Stg",
  keys = ["stream_id"],
  sequence_by = "stream_timestamp",
  stored_as_scd_type = "2", 
  name = None, # optional
  once = False # optional
)