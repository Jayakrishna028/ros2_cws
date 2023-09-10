#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Publisher_test(Node):

    def __init__(self):
        super().__init__("publisher_node")
        self.publisher_ = self.create_publisher(String, "channel1", 5)
        self.timer = self.create_timer(5, self.publisher_activate)


    def publisher_activate(self):
        msg = String()
        msg.data = "The publisher is UP and WORKING......!!!!"
        self.publisher_.publish(msg)
        self.get_logger().info("publishing to 'channel1'....")


def main(args=None):
    rclpy.init(args =args)
    node = Publisher_test()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
