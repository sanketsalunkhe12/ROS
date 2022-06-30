1. sensor.urdf: A sample code for integrating different types of sensor. Camera, RGBD Camera, Stero Camera, Laser Scanner, 3D lidar, IMU
2. mobile_robot1.urdf: A simple two wheel mobile robot with laser scanner, RGBD camera, IMU and odometere with differential drive.
3. rplidar.urdf.xacro: XACRO file for a 2D laser scanner lidar.
4. turtlebot4_lite.urdf.xacro: Incomplete xacro file combining other xacro file. Simple representation of urdf creation from xacro file

rosrun xacro xacro turtlebot4_lite.urdf.xacro > turtlebot4_lite.urdf
