import papermill as pm
from time import gmtime, strftime

current_time = strftime('%Y%m%d%H%M%S', gmtime())

pm.execute_notebook(
   './notebooks/etl_job.ipynb',
   f'./outputs/etl_job_{current_time}.ipynb',
   parameters=dict(
      research_datasets_file='data/research_datasets.zip'
   )
)