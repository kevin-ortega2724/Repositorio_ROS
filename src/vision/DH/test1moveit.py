#!/usr/bin/python3
#
import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped
import random
import math
# Inicializar MoveIt!
rospy.init_node('test_moveit')
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander('manipulator')

# Generar coordenadas cartesianas
poses = []

center_x = 0.0
center_y = 0.0
center_z = 0.0
radius = 0.3
center_z = 0.5
radius = 0.3
h = 0.4

z = center_z
x = center_z
y = center_y
r = radius

for i in range(100):
    theta = random.uniform(0, 2*math.pi)
    z = random.uniform(z - h/2, z + h/2)
    r = random.uniform(0, r)
    x = r * math.cos(theta) + x
    y = r * math.sin(theta) + y
    pose = PoseStamped()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    poses.append(pose)

# Calcular posiciones de las articulaciones para cada pose
for pose in poses:
    group.set_pose_target(pose)
    joint_values = group.get_random_joint_values()
    result = group.set_joint_value_target(joint_values)
    print(joint_values)

    if result is not None:
        print(f"Pose alcanzable: {pose}")
    else:
        print(f"Pose no alcanzable: {pose}")
