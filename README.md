## Important Files
**`src\model\fine_tune_resnet.ipynb`** </br>
The main Jupyter notebook for fine-tuning the model.</br></br>

**`src\preprocessing\delete_to_n.py`** </br>
A python script that deletes all files in a target directory until the number of files reaches a certain number **_n_**. It was used to reduce the size of the dataset, evenly, for faster training.</br></br>

**`src\preprocessing\map_class_names.py`** </br>
A python script that converts (change the image and folder names) the dataset's native surface condition classes into OpenStreetMap (OSM) surface smoothness classes. Here is the mapping for conversion:
| RSCD Class Name | OSM Class Name |
| --- | --- |
| smooth | good |
| slight | intermediate |
| severe | bad |

</br>

**`src\preprocessing\reorganize_data.py`**</br> 
A python script that organizes a list of images into their respective dataset folders. This was created because the 'test' and 'validation' data of the RSCD dataset came as a folder with images from all different classes mixed together. The 'train' part of the dataset was organized and the script follows the same type of categorization.</br></br>

## Dataset citations

```tex
@ARTICLE{10101715,
    author={Zhao, Tong and He, Junxiang and Lv, Jingcheng and Min, Delei and Wei, Yintao},
    journal={IEEE Transactions on Intelligent Transportation Systems}, 
    title={A Comprehensive Implementation of Road Surface Classification for Vehicle Driving Assistance: Dataset, Models, and Deployment}, 
    year={2023},
    volume={24},
    number={8},
    pages={8361-8370},
    doi={10.1109/TITS.2023.3264588}}
```

```tex
@article{ZHAO2024111019,
    title = {Road friction estimation based on vision for safe autonomous driving},
    journal = {Mechanical Systems and Signal Processing},
    volume = {208},
    pages = {111019},
    year = {2024},
    doi = {https://doi.org/10.1016/j.ymssp.2023.111019},
    author = {Tong Zhao and Peilin Guo and Yintao Wei}}
```
