#!/usr/bin/python3
#
#Mensajes ur5
#

from std_msgs.msg import Header			#Para la variable nsec y sec
from trajectory_msgs.msg import JointTrajectory	#Mensaje de trayectorias

from trajectory_msgs.msg import JointTrajectoryPoint
import numpy as np

import rospy




#-----------------
num_samples = 1000 # número de muestras de Monte Carlo
vector_6dof = np.zeros((num_samples, 6)) # vector de 6 grados de libertad con coordenadas inicializadas en 0

for i in range(num_samples):
  # asignación de coordenadas aleatorias a cada grado de libertad
  vector_6dof[i, 0] = np.random.uniform(-1, 1) # coordenada x
  vector_6dof[i, 1] = np.random.uniform(-1, 1) # coordenada y
  vector_6dof[i, 2] = np.random.uniform(-1, 1) # coordenada z
  vector_6dof[i, 3] = np.random.uniform(-1, 1) # coordenada rotación x
  vector_6dof[i, 4] = np.random.uniform(-1, 1) # coordenada rotación y
  vector_6dof[i, 5] = np.random.uniform(-1, 1) # coordenada rotación z

# normalización de las coordenadas para que cada muestra se encuentre en la superficie de una esfera unitaria
for i in range(num_samples):
  norm = np.linalg.norm(vector_6dof[i, :])
  vector_6dof[i, :] = vector_6dof[i, :] / norm
 # print(vector_6dof)
#------------------
#Hacer el for en i
waypoints = [[0.0, -1.44, 1.4, 0, 0, -0.0], [-0.5,-0.5,0,0,0,-0.6], [-0.1,-0.9,0,0,0,-0.5]]		#Puntos
#
VERBOSE = False 
def main():
    rospy.init_node('send_joints')
    pub = rospy.Publisher('/arm_controller/command',
                          JointTrajectory,
                          queue_size=10)

    # Create the topic message
    traj = JointTrajectory()
    traj.header = Header()
    # Joint names for UR5
    traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
                        'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
                        'wrist_3_joint']

    rate = rospy.Rate(1)
    cnt = 0
    pts = JointTrajectoryPoint()
    traj.header.stamp = rospy.Time.now()

    #-----------------
    num_samples = 1000 # número de muestras de Monte Carlo
    vector_6dof = np.zeros((num_samples, 6)) # vector de 6 grados de libertad con coordenadas inicializadas en 0

    for i in range(num_samples):
        # asignación de coordenadas aleatorias a cada grado de libertad
        vector_6dof[i, 0] = np.random.uniform(-1, 1) # coordenada x
        vector_6dof[i, 1] = np.random.uniform(-1, 1) # coordenada y
        vector_6dof[i, 2] = np.random.uniform(-1, 1) # coordenada z
        vector_6dof[i, 3] = np.random.uniform(-1, 1) # coordenada rotación x
        vector_6dof[i, 4] = np.random.uniform(-1, 1) # coordenada rotación y
        vector_6dof[i, 5] = np.random.uniform(-1, 1) # coordenada rotación z

    # normalización de las coordenadas para que cada muestra se encuentre en la superficie de una esfera unitaria
    for i in range(num_samples):
        norm = np.linalg.norm(vector_6dof[i, :])
        vector_6dof[i, :] = vector_6dof[i, :] / norm
    #------------------

    while not rospy.is_shutdown():         #Apagado de rospy
        cnt += 1

        # Mover el robot utilizando las coordenadas aleatorias generadas
        pts.positions = vector_6dof[cnt % num_samples, :]
        pts.time_from_start = rospy.Duration(1.0)

        # Set the points to the trajectory
        traj.points = []
        traj.points.append(pts)
        # Publish the message
        pub.publish(traj)
        rate.sleep()
        print(pts.positions, pts.time_from_start)


