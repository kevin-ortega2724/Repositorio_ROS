#!/usr/bin/env python3
# Import the necessary packages
import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose

# Initialize the ROS node
rospy.init_node("model_spawner")

# Wait for the spawn_model service to become available
rospy.wait_for_service("gazebo/spawn_urdf_model")

# Create a service proxy for the spawn_model service
spawn_model = rospy.ServiceProxy("gazebo/spawn_urdf_model", SpawnModel)

# Load the model file
with open("/home/ko/ur_ws/src/universal_robot/ur_description/urdf/ur5.urdf.xacro", "r") as file:

    model = file.read()

# Define the initial pose of the model
pose = Pose()
pose.position.x = 0
pose.position.y = 0
pose.position.z = 0

# Call the spawn_model service to publish the model
spawn_model("model_name", model, "", pose, "world")

# Change the model's texture
with open("model_with_texture.urdf", "r") as file:
    model_with_texture = file.read()

spawn_model("model_name", model_with_texture, "", pose, "world")

