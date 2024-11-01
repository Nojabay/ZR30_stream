import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/ZR30/camera_stream',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # 画像データをnumpy配列に変換
        image = np.frombuffer(msg.data, dtype=np.uint8)
        image = image.reshape((msg.height, msg.width, 3))  # 高さ、幅、チャンネルにリシェイプ
        cv2.imshow("Camera Stream", image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

