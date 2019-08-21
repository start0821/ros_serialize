# Ros_serialize
이건 온보드에서 실행하고 있는 `/mavros/vision_pose/pose`와 `/mavros/local_position/pose` 토픽을 데이터를 udp통신을 이용해 원하는 컴퓨터로 옮겨주는 패키지입니다.

## Installtion
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/start0821/ros_serialize.git
$ cd ..
$ catkin_make
```

## Run node
### ros_serialize_send
이 노드는 ROS_MASTER_URI가 localhost인 온보드 컴퓨터에서 같은 라우터를 공유하고 있는 컴퓨터로 udp통신을 통해 데이터를 넘겨주는 노드입니다.
``` bash
$ export ros_serialize_receive_ip=# 데이터를 넘겨받고 싶은 컴퓨터의 IP를 입력합니다..
# 예를 들어 $ export ros_serialize_receive_ip=192.168.0.123
$ rosrun ros_serialize ros_serialize_send
```

### ros_serialize_receive
이 노드는 데이터를 수신하고 싶은 컴퓨터에서 실행해야합니다. 온보드 컴퓨터에서 송신하고 있는 데이터를 수신하면 여기서는 `/realsense_pose_data`와`/pixhawk_pose_data` 토픽을 publish합니다.

``` bash
$ export ros_serialize_receive_ip=# 데이터를 넘겨받고 싶은 컴퓨터의 IP를 입력합니다..
# 예를 들어 $ export ros_serialize_receive_ip=192.168.0.123
$ rosrun ros_serialize ros_serialize_receive
```