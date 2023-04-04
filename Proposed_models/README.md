
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

This Repo Ported and modified from original Repo https://github.com/DanielMagro97/LEXACTUM.git. All credit goes to authors of the original repo for making their code open source.
