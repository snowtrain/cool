from cool.modules.Nexus.nexus_1_get_vlan_list import nexus_get_vlan_lists
from cool.modules.Nexus.nexus_2_create_vlan import add_vlan
from cool.modules.Nexus.nexus_3_create_config_vxlan import create_vxlan, config_vxlan_nve
from cool.modules.Nexus.nexus_4_config_dhcp_relay import config_dhcp_relay_server
from cool.modules.Nexus.nexus_5_config_svi import create_svi, config_svi_ip_address
nxos1_ip = '192.168.20.1'
nxos3_ip = '192.168.20.3'
dhcp_ip_address = "172.16.254.254"


# 全自动配置Nexus交换机
def nexus_all_auto(vid):
    vlanid = str(vid)
    print('='*100)
    print('Start to Edit Nexus:')
    # 基于VLAN ID 产生VXLAN ID
    vxlanid = '100' + vlanid
    # 基于VLAN ID 产生SVI IP地址
    svi_ip = '172.16.' + vlanid + '.1'

    # 获取并且打印NXOS-1和NXOS-3配置之前的VLAN列表
    print('NXOS-1 vlan lists Befor: ' + str(nexus_get_vlan_lists(nxos1_ip)))
    print('NXOS-3 vlan lists Befor: ' + str(nexus_get_vlan_lists(nxos3_ip)))

    # 开始在NXOS-1和NXOS-3上创建VLAN
    print('Create Vlan \'' + vlanid + '\' on NXOS-1 and NXOS-3')

    # 在NXOS-1上创建VLAN
    add_vlan(vlanid, nxos1_ip)
    # 在NXOS-3上创建VLAN
    add_vlan(vlanid, nxos3_ip)

    # 获取并且打印NXOS-1和NXOS-3配置之后的VLAN列表
    print('NXOS-1 vlan lists Now: ' + str(nexus_get_vlan_lists(nxos1_ip)))
    print('NXOS-3 vlan lists Now: ' + str(nexus_get_vlan_lists(nxos3_ip)))

    # 开始在NXOS-1和NXOS-3上创建和配置VXLAN
    print('Create vxlan on NXOS-1 and NXOS-3: ' + vxlanid)
    create_vxlan(vlanid, nxos1_ip)
    config_vxlan_nve(vlanid, nxos1_ip)
    create_vxlan(vlanid, nxos3_ip)
    config_vxlan_nve(vlanid, nxos3_ip)

    # 配置VLAN的DHCP Relay
    print('Edit DHCP Realy for Vlan' + vlanid)
    config_dhcp_relay_server(vlanid, nxos3_ip, dhcp_ip_address)

    # 创建SVI,并且配置SVI的IP地址
    print('Create Vlan' + vlanid + ' SVI address' + ' on NXOS-3: ' + svi_ip)
    create_svi(vlanid, nxos3_ip)
    config_svi_ip_address(vlanid, nxos3_ip)


if __name__ == "__main__":
    nexus_all_auto(198)

