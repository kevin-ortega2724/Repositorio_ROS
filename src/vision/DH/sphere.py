#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import JointState



class SphereDataReader:
    def __init__(self):
        self.sphere_center = None
        self.sphere_radius = None
        self.joint_angles = None
        rospy.Subscriber("/sphere_data", Vector3, self.sphere_callback)
        rospy.Subscriber("/joint_states", JointState, self.joint_callback)

    def sphere_callback(self, sphere_data):
        self.sphere_center = sphere_data.vector
        self.sphere_radius = sphere_data.radius
        
    def joint_callback(self, joint_state):
        self.joint_angles = joint_state.position
        
    def sample_uniform_sphere(self):
        if self.sphere_radius is None:
            return None
        theta = np.random.uniform(0, np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        r = self.sphere_radius * np.cbrt(np.random.uniform(0, 1))
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        return np.array([x, y, z])
        
    def sample_quality(sample, obstacle_list):
        quality = 1.0
        for obstacle in obstacle_list:
            obstacle_x, obstacle_y, obstacle_z = obstacle[0], obstacle[1], obstacle[2]
            obstacle_radius = obstacle[3]
            sample_x, sample_y, sample_z = sample[0], sample[1], sample[2]
            distance = np.sqrt((obstacle_x - sample_x)**2 + (obstacle_y - sample_y)**2 + (obstacle_z - sample_z)**2)
            if distance < obstacle_radius:
                quality = 0.0
                break
    return quality
    
    def generate_random_samples(self, n_samples):
        samples = []
        for i in range(n_samples):
            sample = self.sample_uniform_sphere()
            quality = self.evaluate_sample_quality(sample)
            samples.append((sample, quality))
        return samples    

  
if __name__ == '__main__':
    reader = SphereDataReader()
    n_samples = 100
    samples = reader.generate_random_samples(n_samples)
    for sample in samples:
        print(sample) 
  
     
#if __name__ == '__main__':
#    rospy.init_node('sphere_data_reader')
#    reader = SphereDataReader()
#    #sample = reader.sample_uniform_sphere()
#    n_samples = 1000
#    samples = []
#    samples1 = reader.generate_random_samples(n_samples)
#    for i in range(samples):
#        sample = reader.sample_uniform_sphere()
#        samples.append(sample)
#
#    print(samples)
#    rospy.spin()


#if __name__ == '__main__':
#    rospy.init_node('sphere_sampler')
#    reader = SphereDataReader()
#    rate = rospy.Rate(10) # 10Hz
#    while not rospy.is_shutdown():
#        sample = reader.sample_uniform_sphere()
#        if sample is not None:
#            rospy.loginfo("Sample: {}".format(sample))
#        rate.sleep()

