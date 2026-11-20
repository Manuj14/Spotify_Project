# Spotify_Project
Spotify_Data_Engineer_Project


After ADF lands the data in ADLS Gen2, Azure Databricks handles transformation
and modelling using a medallion architecture.

**Architecture:** Azure SQL / source → ADF (incremental load with CDC) →
ADLS Gen2 (bronze) → Databricks (silver) → Databricks DLT (gold)

**What I built**
- **Unity Catalog setup:** access connector with managed identity, storage
  credential, external location and a `spotify_cata` catalog with
  bronze/silver/gold schemas.
- **Bronze → Silver:** incremental ingestion with Auto Loader (`cloudFiles`)
  and Structured Streaming, using checkpoints and schema locations.
- **Transformations:** PySpark logic such as standardising names, dropping
  rescued-data columns and deriving fields (e.g. album status from release
  date), organised in reusable helper classes.
- **Dimensional model:** `DimUser`, `DimTrack`, `DimArtist` and `FactStream`
  stored as Delta tables.
- **Dynamic SQL with Jinja:** a config-driven approach that generates
  fact-to-dimension join queries from a parameters list, so adding a new
  dimension needs only a config change.
- **Gold layer with Delta Live Tables:** declarative pipelines for
  analytics-ready tables.
- **Deployment:** Databricks Asset Bundles (`databricks.yml`) to validate and
  deploy pipelines as code.

**Tech stack:** Azure Data Factory, ADLS Gen2, Azure Databricks, Unity Catalog,
PySpark, Delta Lake, Delta Live Tables, Jinja2, Databricks Asset Bundles, Git
