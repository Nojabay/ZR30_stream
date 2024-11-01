from setuptools import setup

package_name = 'image_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='agilex',
    maintainer_email='agilex@example.com',  # 適切なメールアドレスに変更
    description='A ROS 2 package for subscribing to camera images.',  # 説明を更新
    license='MIT',  # 使用するライセンスを選択
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_subscriber = image_subscriber.subscriber:main',
        ],
    },
)
