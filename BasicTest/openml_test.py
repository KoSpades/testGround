import openml

mnist_openml = openml.datasets.get_dataset(554)
Xy, _, _, _ = mnist_openml.get_data(dataset_format="array")
print(type(Xy))

