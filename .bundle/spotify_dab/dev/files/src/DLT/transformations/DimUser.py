

import dlt

#### DimUser

expectations = {

  "rule_1" : "user_id IS NOT NULL"
}

@dlt.table
@dlt.expect_all(expectations)
def dimuser_Stg():
    df = spark.readStream.table("spotify_cata.silver.dimuser")
    return df


dlt.create_streaming_table("dimuser")


dlt.create_auto_cdc_flow(
  target = "dimuser",
  source = "dimuser_Stg",
  keys = ["user_id"],
  sequence_by = "updated_at",
  stored_as_scd_type = "2", 
  name = None, # optional
  once = False # optional
)



