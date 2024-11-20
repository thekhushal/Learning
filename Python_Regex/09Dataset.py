import kagglehub

# Download latest version
path = kagglehub.dataset_download("octopusteam/full-hulu-dataset")

print("Path to dataset files:", path)