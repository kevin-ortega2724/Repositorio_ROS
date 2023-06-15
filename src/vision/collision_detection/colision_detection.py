#!/usr/bin/env python3

import rospy
import moveit_commander
from moveit_msgs.msg import PlanningScene, ObjectColor
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import CollisionObject

rospy.init_node('collision_checker', anonymous=True)

# Inicializar MoveIt
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")

# Crear un objeto de posición de destino
target_pose = PoseStamped()
target_pose.header.frame_id = "base_link"
target_pose.pose.position.x = 0.5 # COORDENADA X
target_pose.pose.position.y = 0.2 # COORDENADA Y
target_pose.pose.position.z = 0.5 # COORDENADA Z
target_pose.pose.orientation.w = 1.0

# Configurar el objeto en la escena
scene_msg = PlanningScene()
object_name = "target_object"
object_pose = target_pose.pose
object_size = [0.05, 0.05, 0.05] # Tamaño del objeto
scene_msg.world.collision_objects.append(CollisionObject(id=object_name, pose=object_pose, 
                                    primitives=[SolidPrimitive(type=SolidPrimitive.SPHERE, dimensions=object_size)], 
                                    primitive_poses=[object_pose]))
scene_msg.is_diff = True

# Crear un publisher para publicar el mensaje de la escena de planificación
scene_pub = rospy.Publisher('planning_scene', PlanningScene, queue_size=10)

# Publicar el mensaje de la escena de planificación
rate = rospy.Rate(10) # 10Hz
while not rospy.is_shutdown():
    scene_pub.publish(scene_msg)
    rate.sleep()

# Planificar el movimiento del robot a la posición de destino
group.set_pose_target(target_pose)
plan = group.plan()

# Comprobar si hay colisiones en el plan
if len(plan.joint_trajectory.points) > 0:
    rospy.loginfo("No hay colisiones en la posición de destino.")
else:
    rospy.logwarn("Se encontró una colisión en la posición de destino.")

