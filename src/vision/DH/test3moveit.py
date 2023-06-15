#!/usr/bin/python3

import random
import math
import moveit_commander
import geometry_msgs.msg
import rospy


def main():
    # Iniciar moveit commander
    moveit_commander.roscpp_initialize([])

    # Iniciar nodo de ROS
    rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

    # Iniciar objeto RobotCommander para obtener información sobre el robot
    robot = moveit_commander.RobotCommander()

    # Iniciar objeto PlanningSceneInterface para obtener información sobre el mundo
    scene = moveit_commander.PlanningSceneInterface()

    # Iniciar objeto MoveGroupCommander para el grupo de articulaciones de interés
    group = moveit_commander.MoveGroupCommander('manipulator')

    # Configurar el objeto PlanningSceneInterface para considerar la geometría del robot
    scene.robot = robot

    # Crear lista para almacenar poses alcanzables
    reachable_poses = []

    # Crear lista de poses aleatorias en una semiesfera
    poses = []
    for i in range(10):
        # Generar coordenadas polares aleatorias en la semiesfera
        r = 0.5
        theta = random.uniform(0, math.pi/2)
        phi = random.uniform(0, 2*math.pi)
        x = r*math.sin(theta)*math.cos(phi)
        y = r*math.sin(theta)*math.sin(phi)
        z = r*math.cos(theta)

        # Crear pose
        pose = geometry_msgs.msg.Pose(
            position=geometry_msgs.msg.Point(x=x, y=y, z=z),
            orientation=geometry_msgs.msg.Quaternion(x=0, y=0, z=0, w=1)
        )

        # Agregar pose a la lista de poses
        poses.append(pose)

    # Verificar si cada pose es alcanzable
    for pose in poses:
        group.set_pose_target(pose)
        joint_values = group.get_random_joint_values()
        result = group.set_joint_value_target(joint_values)

        # Configurar el objeto PlanningSceneInterface para considerar la geometría del robot
        scene.robot = robot

        # Obtener la planificación para la pose y verificar si hay colisiones
        plan = group.plan()
        if plan[0]:
            if len(plan[0].joint_trajectory.points) > 0:
                # Verificar si hay colisiones
                collisions = scene.is_diff_robot()
                if not collisions:
                    reachable_poses.append(pose)

    # Imprimir lista de poses alcanzables
    print("Poses alcanzables:")
    for pose in reachable_poses:
        print(pose)

    # Terminar moveit commander
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    main()

