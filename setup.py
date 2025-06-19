from setuptools import find_packages, setup

package_name = 'range_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jerem',
    maintainer_email='jerem@todo.todo',
    description='Node ROS 2 pour capteur HC-SR04 avec gpiozero',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'range_node = range_sensor.range_node:main',
        ],
    },
)
