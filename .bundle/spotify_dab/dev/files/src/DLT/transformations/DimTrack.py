import dlt

#### DimTrack

@dlt.table
def dimtrack_Stg():
    df = spark.readStream.table("spotify_cata.silver.dimtrack")
    return df

dlt.create_streaming_table("dimtrack")


dlt.create_auto_cdc_flow(
  target = "dimtrack",
  source = "dimtrack_Stg",
  keys = ["track_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = "2", 
  name = None, # optional
  once = False # optional
)