#!/usr/bin/env python3

import rospy
import moveit_commander
import geometry_msgs.msg



# Función de control del robot UR5
def control_ur5():
    # Iniciar el objeto MoveGroupCommander
    move_group = moveit_commander.MoveGroupCommander("manipulator")

    # Configurar la velocidad y la aceleración del robot
    move_group.set_max_velocity_scaling_factor(0.1)
    move_group.set_max_acceleration_scaling_factor(0.1)

    # Definir la posición objetivo del robot
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = 0.2
    pose_goal.position.y = 0.3
    pose_goal.position.z = 0.4
    pose_goal.orientation.x = 0.0
    pose_goal.orientation.y = 0.0
    pose_goal.orientation.z = 0.0
    pose_goal.orientation.w = 1.0

    # Planificar el movimiento del robot a la posición objetivo
    move_group.set_pose_target(pose_goal)
    plan = move_group.plan()

    # Ejecutar el movimiento del robot
    move_group.execute(plan, wait=True)

if __name__ == '__main__':
    try:
        # Inicializar el nodo de ROS
        rospy.init_node('ur5_gazebo_control', anonymous=True)

        # Obtener la descripción del modelo UR5 en formato XML
        robot_description_xml = rospy.get_param('robot_description')

        # Iniciar el objeto RobotCommander
        robot = moveit_commander.RobotCommander()

        # Iniciar el objeto PlanningSceneInterface
        scene = moveit_commander.PlanningSceneInterface()

        # Iniciar el objeto MoveGroupCommander
        move_group = moveit_commander.MoveGroupCommander("manipulator")

        # Esperar a que Gazebo esté listo
        rospy.sleep(2)

        # Llamar a la función de control del robot UR5
        control_ur5()

    except rospy.ROSInterruptException:
        pass

