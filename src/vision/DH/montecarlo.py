#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import numpy as np

# Inicializar ROS y MoveIt
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('ur5_kinematics', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander('manipulator')

# Definir las coordenadas objetivo en x, y, z
target_coords = [[0.3, -0.1, 0.5], [0.5, 0.0, 0.5], [0.3, 0.1, 0.5]]

for target_coord in target_coords:
    # Establecer la posición objetivo del efector final
    group.set_position_target(target_coord)

    # Calcular la planificación de movimiento
    plan = group.plan()
    joint_angles = list(plan.joint_trajectory.points[-1].positions)


    # Imprimir la configuración articulada
    print(f"Configuración articulada para la posición {target_coord}: {joint_angles}")

