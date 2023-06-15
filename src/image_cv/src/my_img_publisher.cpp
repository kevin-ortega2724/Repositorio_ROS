//Publica información de la cámara en un tópico cuya descripción estará detallada en código.
//Source : http://wiki.ros.org/image_transport/Tutorials/PublishingImages

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <sstream>
 
using namespace cv;  //Evita iniciar con cv en las funciones de opencv
 
int main(int argc, char** argv)
{
	ros::init(argc, argv, "my_img_publisher");  //Inicialización del nodo
	ros::NodeHandle nh;
	image_transport::ImageTransport it(nh);
	image_transport::Publisher pub = it.advertise("/camera/color/image_raw", 1);
	
	VideoCapture cap(0);    //Argumento es '0' para utilizar la cámara
	if(!cap.isOpened()) return 1;
	Mat frame;
	sensor_msgs::ImagePtr msg;
	
	ros::Rate loop_rate(10);		//frecuencia de ejecucion 10 hz

//Ciclo infinito
//Se pueden ver especificaciones de los colores bgr8 documentacion
	while (nh.ok()) {
		cap >> frame; 
		if(!frame.empty()) {
			msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();

			pub.publish(msg);
		}
		ros::spinOnce();
		loop_rate.sleep();
	}
}
