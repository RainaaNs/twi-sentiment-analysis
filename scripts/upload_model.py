from huggingface_hub import upload_folder

from huggingface_hub import HfApi

api = HfApi()


api.create_repo(
    repo_id="rainaans/twi-sentiment-model",
    repo_type="model",
    private=False
)


upload_folder(
    folder_path="model/sentiment_model",
    repo_id="rainaans/twi-sentiment-model",
    repo_type="model"
)




