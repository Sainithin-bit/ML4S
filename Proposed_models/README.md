
## Installing Dependencies

All the required Python packages can be installed by running this command:
```bash
pip install astropy tensorflow-gpu numpy pandas scikit-learn imgaug matplotlib
```

## Training a New Model

To train a model on the Space set, run the following command, substituting `<>`s with your own values.
```bash
python Space.py --dataset <path_to_dataset> --train_or_load train --model_name <name-of-model> --no_of_epochs <number-of-epochs> 
```


Accepted values for `<name-of-model>` are:\
`lastro_epfl`, `cmu_deeplens`

The trained model will then be saved in the `models` directory as `models/<space/ground>_<model-name>_<number-of-epochs>epochs.h5`.

## Loading a Pre-Trained Model

To run a trained model on the Space set, run the following command, substituting `<>`s with your own values.
```bash
python Space.py --dataset <path_to_dataset> --train_or_load load --model_name <name-of-model> 
```

For `<name-of-model>`, use the name of the `.h5` file stored inside the `models/` folder, excluding `models/`,
but including the extension `.h5`.

## Visualising the Feature Maps of a Trained Model

To visualise the feature maps of a trained model at every convolutional layer, the `visualise_features.py` script can be used.
At around `line 105` of the code, set the variable `model_name` to the name of the trained model inside the `models`
directory that you would like to visualise the convolutional layers of. Do not include `models/`, but do include the
`.h5` extension.
On `line 117`, `sample_image_path` can be set to the path of any image that will be passed through the model, for
which the outputs of the convolutional layers will be visualised. 

Once these variables have been set, the `visualise_features.py` script can be run, and any convolutional layers will be
detected automatically, and displayed at the end.

## Command-Line Arguments

A description of accepted command-line arguments can be found by running:
```bash
python Space.py --help
# or
python Ground.py --help
```

Here is a short description of each recognised parameter
* `--dataset` - The path to the directory containing the dataset
* `--train_or_load` - Whether to train a model, or to load one from disk - Accepted values: `train` or `load`
* `--model_name` - The name of the model to train - Accepted values: `cas_swinburne`, `lastro_epfl`, `cmu_deeplens`,
`wsi_net`, `lens_flow` or `lens_finder`\
Or the name of the file in the models folder to load from disk (including .h5)
* `--no_of_epochs` - The number of epochs to train the model for
* `--batch_size` - Number of images per batch
* `--augment_images` - Whether to perform Image Augmentation on the training data while training - Accepted values: `True` or `False`


