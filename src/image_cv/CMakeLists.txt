cmake_minimum_required(VERSION 3.0.2)
project(image_cv)


find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  sensor_msgs
  std_msgs
)
find_package(OpenCV)
include_directories(${OpenCV_INCLUDE_DIRS})

catkin_package(
	CATKIN_DEPENDS cv_bridge image_transport roscpp rospy sensor_msgs std_msgs

)

include_directories( ${catkin_INCLUDE_DIRS})

add_executable(my_img_publisher src/my_img_publisher.cpp)
target_link_libraries(my_img_publisher ${catkin_LIBRARIES})
target_link_libraries(my_img_publisher ${OpenCV_LIBRARIES})

add_executable(my_img_listener src/my_img_listener.cpp)
target_link_libraries(my_img_listener ${catkin_LIBRARIES})
target_link_libraries(my_img_listener ${OpenCV_LIBRARIES})






