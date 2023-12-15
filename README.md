# PowerBEV - Woven Dataset
* Contributors : Aman Sharma , Vyshnav Achuthan , Neha Madhekar , Rishikesh Jadhav , Wu Xiyang 



![](.github/PowerBev2.jpg)


## Contents
- [PowerBEV2](#powerbev)
  - [Setup](#️-setup)
  - [Dataset](#-dataset)
  - [Pre-trained models](#-pre-trained-models)
  - [Training](#-training)
  - [Prediction](#-prediction)
    - [Evaluation](#evaluation)
    - [Visualisation](#visualisation)
  - [Credits](#-credits)
  - [Citation](#-citation)

## Setup
Create the [conda](https://docs.conda.io/en/latest/miniconda.html) environment by running 
```
conda env create -f environment.yml
```

## Dataset
- Download the full [*Toyota Woven Planet Perception datset*](https://woven.toyota/en/perception-dataset/), which includes the *Mini dataset* and the *Train and Test dataset*.
- Extract the tar files to a directory named `lyft2/` . The files should be organized in the following structure:
  ```
  lyft2/
  ├──── train/
  │     ├──── maps/
  │     ├──── images/
  │     ├──── train_lidar/
  │     └──── train_data/
  ```

## Pre-trained models (Comparision)
The config file can be found in [`powerbev/configs`](powerbev/configs) . You can download the pre-trained models which are finetuned for nuscenes dataset using the below links:

|Weights | Dataset | BEV Size | IoU | VPQ |
|-|-|-|:-:|:-:|
|[`PowerBEV_long.ckpt`](https://drive.google.com/file/d/1P33nD6nt8IjnvKTd4WlTKWbarFdCE34f/view?usp=sharing) | NuScenes| 100m x 100m (50cm res.) | 39.3 | 33.8 |
| [`PowerBEV_short.ckpt`](https://drive.google.com/file/d/1-T4R6vC2HHhqxXeUeUg-CuViA5XdQEcV/view?usp=sharing) | NuScenes| 30m x 30m (15cm res.) | 62.5 | 55.5 |  
| [`PowerBEV_static_long.ckpt`]((https://drive.google.com/file/d/16bnG3kI_J3JkFGGxMuQfz879QFz7SVhj/view?usp=sharing))| None | 100m x 100m (50cm res.) | 39.3 | 33.8 |
| [`PowerBEV_static_short.ckpt`](https://drive.google.com/file/d/1Jwb2UjNEuamwNmBZ_R-DAW91dhxi4_6J/view?usp=sharing)| None | 30m x 30m (15cm res.) | 62.5 | 55.5 |  

## Training
To train the model from scratch on Woven, run

```
python train.py --config powerbev/configs/powerbev.yml
```
and make sure you make the respective changes on the config.yaml file inside configs folder.
### For running on pretrained weights

```
python train.py --config powerbev/configs/powerbev.yml \
                PRETRAINED.LOAD_WEIGHTS True \
                PRETRAINED.PATH $YOUR_PRETRAINED_STATIC_WEIGHTS_PATH
```


## Prediction
### Evaluation
To run from the model which was trained from scratch just search for the tensorboard log file which will have the ckpt file and add that ckpt
file path as your pretrained weights path.

```
python test.py --config powerbev/configs/powerbev.yml \
                PRETRAINED.LOAD_WEIGHTS True \
                PRETRAINED.PATH $YOUR_PRETRAINED_WEIGHTS_PATH
```

### Visualisation
To run from the model which was trained from scratch just search for the tensorboard log file which will have the ckpt file and add that ckpt
file path as your pretrained weights path.
```
python visualise.py --config powerbev/configs/powerbev.yml \
                PRETRAINED.LOAD_WEIGHTS True \
                PRETRAINED.PATH $YOUR_PRETRAINED_WEIGHTS_PATH \
                BATCHSIZE 1
```
This will render predictions from the network and save them to an `visualization_outputs` folder.

## License
PowerBEV is released under the MIT license. Please see the [LICENSE](LICENSE) file for more information.

## Credits
This is the official PyTorch implementation of the paper: 
> [**PowerBEV: A Powerful yet Lightweight Framework for Instance Prediction in Bird's-Eye View**](https://www.ijcai.org/proceedings/2023/0120.pdf)  
> Peizheng Li, Shuxiao Ding,Xieyuanli Chen,Niklas Hanselmann,Marius Cordts,Jürgen Gall
