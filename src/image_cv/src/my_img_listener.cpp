//Este nodo se subscribe a un tópico y muestra la imagen o video
// fuente: http://wiki.ros.org/image_transport/Tutorials/SubscribingToImages
#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>

using namespace cv;
std::string window_name = "Video stream";
void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  try
  {
    Mat received_img = cv_bridge::toCvShare(msg, "bgr8")->image;
    imshow(window_name, received_img);
    waitKey(10);
  }
  catch (cv_bridge::Exception& e)
  {
    ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
  }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "image_listener");
  ros::NodeHandle nh;
  namedWindow("window_name");
  startWindowThread();
  image_transport::ImageTransport it(nh);
  std::string topic_name;
  if(argc !=1) topic_name =argv[1];
  else{
  	topic_name ="/camera/depth/image_raw"; 
  	std::cout << "No topic name given, the default topic name will be use:" << topic_name << std::endl;
  	}
image_transport::Subscriber sub = it.subscribe("topic_name", 1, imageCallback);
  ros::spin();
 // cv::destroyWindow("view");
}
