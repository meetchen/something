import httplib2
import time
import json
import matplotlib.pyplot as plt

class OdlUtil:
    url = ''

    def __init__(self, host, port):
        self.url = 'http://' + host + ':' + str(port)

    def install_flow(self, container_name='default', username="admin", password="admin"):
        http = httplib2.Http()
        http.add_credentials(username, password)
        i = 0
        port1 = []
        port2 = []
        axis = []
        headers = {'Accept': 'application/json'}
        flow_name = 'flow_' + str(int(time.time() * 1000))
        # s3流表

        s3_h3_to_h1 = '{"flow": [{"id": "0","match": {"ethernet-match": ' \
                      '{"ethernet-type": {"type": "0x0800"}},' \
                      '"ipv4-source": "10.0.0.3/32",' \
                      '"ipv4-destination": "10.0.0.1/32"},' \
                      '"instructions": {"instruction": [{"order": "0",' \
                      '"apply-actions": {"action": [{"order": "0","output-action": {' \
                      '"output-node-connector": "1"}}]}}]},' \
                      '"priority": "100","table_id": "0"}]}'
        # s1流表

        s1_h2_to_h1 = '{"flow": [{"id": "0","match": {"ethernet-match": ' \
                      '{"ethernet-type": {"type": "0x0800"}},' \
                      '"ipv4-source": "10.0.0.2/32",' \
                      '"ipv4-destination": "10.0.0.1/32"},' \
                      '"instructions": {"instruction": [{"order": "0",' \
                      '"apply-actions": {"action": [{"order": "0","output-action": {' \
                      '"output-node-connector": "1"}}]}}]},' \
                      '"priority": "100","table_id": "0"}]}'

        s1_h3_to_h1 = '{"flow": [{"id": "0","match": {"ethernet-match": ' \
                      '{"ethernet-type": {"type": "0x0800"}},' \
                      '"ipv4-source": "10.0.0.3/32",' \
                      '"ipv4-destination": "10.0.0.1/32"},' \
                      '"instructions": {"instruction": [{"order": "0",' \
                      '"apply-actions": {"action": [{"order": "0","output-action": {' \
                      '"output-node-connector": "1"}}]}}]},' \
                      '"priority": "100","table_id": "0"}]}'
        # s2流表

        # h2工作下发的流表
        s2_h2_to_h1 = '{"flow": [{"id": "0","match": {"ethernet-match": ' \
                      '{"ethernet-type": {"type": "0x0800"}},' \
                      '"ipv4-source": "10.0.0.2/32",' \
                      '"ipv4-destination": "10.0.0.1/32"},' \
                      '"instructions": {"instruction": [{"order": "0",' \
                      '"apply-actions": {"action": [{"order": "0","output-action": {' \
                      '"output-node-connector": "1"}}]}}]},' \
                      '"priority": "100","table_id": "0"}]}'

        # h3工作时s2端口1空闲下发的流表

        s2_h3_to_h1_1 = '{"flow": [{"id": "1","match": {"ethernet-match": ' \
                        '{"ethernet-type": {"type": "0x0800"}},' \
                        '"ipv4-source": "10.0.0.3/32",' \
                        '"ipv4-destination": "10.0.0.1/32"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"order": "0","output-action": {' \
                        '"output-node-connector": "1"}}]}}]},' \
                        '"priority": "150","table_id": "0"}]}'

        s2_h3_to_h1_4 = '{"flow": [{"id": "2","match": {"ethernet-match": ' \
                        '{"ethernet-type": {"type": "0x0800"}},' \
                        '"ipv4-source": "10.0.0.3/32",' \
                        '"ipv4-destination": "10.0.0.1/32"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"order": "0","output-action": {' \
                        '"output-node-connector": "4"}}]}}]},' \
                        '"priority": "100","table_id": "0"}]}'
        # h3工作时s2端口1满载下发的流表

        s2_mh3_to_h1_1 = '{"flow": [{"id": "1","match": {"ethernet-match": ' \
                         '{"ethernet-type": {"type": "0x0800"}},' \
                         '"ipv4-source": "10.0.0.3/32",' \
                         '"ipv4-destination": "10.0.0.1/32"},' \
                         '"instructions": {"instruction": [{"order": "0",' \
                         '"apply-actions": {"action": [{"order": "0","output-action": {' \
                         '"output-node-connector": "1"}}]}}]},' \
                         '"priority": "100","table_id": "0"}]}'

        s2_mh3_to_h1_4 = '{"flow": [{"id": "2","match": {"ethernet-match": ' \
                         '{"ethernet-type": {"type": "0x0800"}},' \
                         '"ipv4-source": "10.0.0.3/32",' \
                         '"ipv4-destination": "10.0.0.1/32"},' \
                         '"instructions": {"instruction": [{"order": "0",' \
                         '"apply-actions": {"action": [{"order": "0","output-action": {' \
                         '"output-node-connector": "4"}}]}}]},' \
                         '"priority": "150","table_id": "0"}]}'
        headers = {'Content-type': 'application/json'}
        # 下发s1的流表
        response, content = http.request(
            uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/opflow:1/flow-node-inventory:table/0/flow/0',
            body=s1_h2_to_h1, method='PUT', headers=headers)
        response, content = http.request(
            uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/opflow:1/flow-node-inventory:table/0/flow/1',
            body=s1_h3_to_h1, method='PUT', headers=headers)
        # 下发s3的流表
        response, content = http.request(
            uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/opflow:3/flow-node-inventory:table/0/flow/0',
            body=s3_h3_to_h1, method='PUT', headers=headers)
        # 下发s2的流表(h2到h1)
        response, content = http.request(
            uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/opflow:2/flow-node-inventory:table/0/flow/0',
            body=s2_h2_to_h1, method='PUT', headers=headers)

        while True:
            axis.append(i)
            i = i+2
            # 获取s2端口1的流量
            uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:2/node-connector/openflow:2:1'
            response, content = http.request(uri=uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0][
                'opendaylight-port-statistics:flow-capable-node-connector-statistics']
            bytes1_port1 = statistics['bytes']['transmitted']
            # 获取s2端口4的流量
            uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:2/node-connector/openflow:2:4'
            response, content = http.request(uri=uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0][
                'opendaylight-port-statistics:flow-capable-node-connector-statistics']
            bytes1_port4 = statistics['bytes']['transmitted']
            # 1秒后再次获取
            time.sleep(2)
            uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:2/node-connector/openflow:2:1'
            response, content = http.request(uri=uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0][
                'opendaylight-port-statistics:flow-capable-node-connector-statistics']
            bytes2_port1 = statistics['bytes']['transmitted']
            uri = 'http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:2/node-connector/openflow:2:4'
            response, content = http.request(uri=uri, method='GET')
            content = json.loads(content.decode())
            statistics = content['node-connector'][0][
                'opendaylight-port-statistics:flow-capable-node-connector-statistics']
            bytes2_port4 = statistics['bytes']['transmitted']
            # 输出s2端口1和端口4的速度
            speed1 = float(bytes2_port1 - bytes1_port1)/2
            speed2 = float(bytes2_port4 - bytes1_port4)/2
            # figure
            port1.append(speed1)
            port2.append(speed2)
            plt.ion()
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.clf()
            plt.title("S2交换机-两端口实时流速图")
            plt.xlabel("time /s")
            plt.ylabel("bytes /s")
            plt.plot(axis, port1, label="S2交换机 1端口")  # 画出当前 ax 列表和 ay 列表中的值的图形
            plt.plot(axis, port2, label="S2交换机 2端口")  # 画出当前 ax 列表和 ay 列表中的值的图形
            plt.legend()
            plt.pause(0.1)  # 暂停一秒
            plt.ioff()  # 关闭画图的窗口
            
            # 在检测到s2的1口流量空闲时发的流表
            if speed1 != 0:  # 获取有效的速度
                print('s2端口1速度：%.3lf byte/s' % speed1)
                print('s2端口4速度：%.3lf byte/s' % speed2)
                #print(speed1)
                if speed1 < 300*1024*1024:
                    print('当前s2端口1处于空闲状态，h3数据包通往s1')
                    response, content = http.request(
                        uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1',
                        body=s2_h3_to_h1_1, method='PUT', headers=headers)
                    response, content = http.request(
                        uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/2',
                        body=s2_h3_to_h1_4, method='PUT', headers=headers)
                # 在检测到s2的1口流量满载时发的流表
                else:
                    print('当前s2端口1处于满载状态，h3数据包通往s3')
                    response, content = http.request(
                        uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/1',
                        body=s2_mh3_to_h1_1, method='PUT', headers=headers)
                    response, content = http.request(
                        uri='http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/2',
                        body=s2_mh3_to_h1_4, method='PUT', headers=headers)


                print("------------------------------------")
odl = OdlUtil('127.0.0.1', '8181')
odl.install_flow()
