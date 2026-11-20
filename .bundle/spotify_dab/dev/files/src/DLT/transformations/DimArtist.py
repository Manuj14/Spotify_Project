import dlt

#### DimArtist

@dlt.table
def dimartist_Stg():
    df = spark.readStream.table("spotify_cata.silver.dimartist")
    return df


dlt.create_streaming_table("dimartist")


dlt.create_auto_cdc_flow(
  target = "dimartist",
  source = "dimartist_Stg",
  keys = ["artist_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = "2", 
  name = None, # optional
  once = False # optional
)