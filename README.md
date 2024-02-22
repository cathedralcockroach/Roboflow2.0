# Its written by Suv 
# all the steps i have followed while doing this proj
# if u are having any issues running the proj pls go through Rdme.txt

## Create a virtul enviroment:- 
```
python -m venv myenv
```
## Activate the enviroment:-
```
myenv/Scripts/Activate.ps1 
```
```
source myenv/bin/activate (mac)
myenv/Scripts/activate.bat (cmd)
myenv/Scripts/Activate.ps1 (powershell)
```
## Install the dependencies:- 
```
pip install -r requirements.txt 
```
## Now while running the ipynb file select the kernal as the enviroment name
## for this case it will be myenv.

#### To close the virtual environment:
```
deactivate
```
<!-- Set the path for test and train folders. -->

<!-- Follow the steps in cmd for applying  -->

## bash command for installing yolov5 
```
pip install torch torchvision
git clone https://github.com/ultralytics/yolov5.git
```







