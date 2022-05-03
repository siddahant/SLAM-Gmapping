# SLAM-Gmapping
Dynamic Search of the optimal path in an unknown Environment uisng SLAM Gmapping
# clone the demonstration code
cd catkin_ws/src
git clone https://github.com/siddahant/SLAM-Gmapping.git

# return to catkin_ws root
cd ../ 
```
2. ** Build the workspace and activate it.**
```
catkin_make
source devel/setup.bash
```
3.**Launch the node.**
```
roslaunch ses_nevagiation ses.launch
