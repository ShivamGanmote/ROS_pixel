#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.publish_image)

    def publish_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            ros_image = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher_.publish(ros_image)

def main(args=None):
    rclpy.init(args=args)
    webcam_publisher = WebcamPublisher()
    rclpy.spin(webcam_publisher)
    webcam_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

