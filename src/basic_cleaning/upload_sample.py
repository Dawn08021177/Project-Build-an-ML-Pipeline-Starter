import wandb

run = wandb.init(
    project="Project-Build-an-ML-Pipeline-Starter-src_basic_cleaning",
    job_type="upload_data"
)

artifact = wandb.Artifact(
    name="sample.csv", 
    type="raw_data", 
    description="Raw sample input data"
)

artifact.add_file("sample.csv")
run.log_artifact(artifact)
run.finish()

