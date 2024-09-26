from signLanguage.pipeline.training_pipeline import TrainPipeline
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

obj = TrainPipeline()
obj.run_pipeline()
