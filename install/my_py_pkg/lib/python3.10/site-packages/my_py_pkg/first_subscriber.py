#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class FirstPublisherNode(Node):
    def __init__(self):
        super().__init__("py_subscriber")
        self.subscriber_ = self.create_subscription(String, "channel1", self.msg_processing_subscriber,5)
        self.subscriber_

    def msg_processing_subscriber(self, msg):
        self.get_logger().info(f"Recieved msg:{msg.data}")


def main(args = None):
    rclpy.init(args =args)
    node = FirstPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()