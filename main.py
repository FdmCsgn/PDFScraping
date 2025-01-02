from datasets import load_dataset

# JSON dosyasını Hugging Face Dataset formatına yükleyin
dataset = load_dataset("json", data_files="output.json")

# Verinin ilk birkaç satırını görüntüleyerek kontrol edebilirsiniz
print(dataset["train"][0])
