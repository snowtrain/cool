from cool.modules.ASA.asa_0_login_info import ip
from cool.modules.ASA.asa_4_all_auto import asa_all_auto
# from cloud_system.modules.IOS.config_dhcp_server import config_server, dhcp_server_ip
from cool.modules.IOS.config_dhcp_server_netmiko import ssh_netmiko, dhcp_server_ip
from cool.modules.Nexus.nexus_6_all_auto import nexus_all_auto
from cool.modules.vSphere.vsphere_8_all_auto import vsphere_all_auto


def cloud_all_auto(cpu_cores, mem, vlanid):
    # 根据输入的CPU和MEM配置,判断模板
    global temp_no
    if mem == 1 and cpu_cores == 1:
        temp_no = 1
    elif mem == 2 and cpu_cores == 1:
        temp_no = 2
    elif mem == 1 and cpu_cores == 2:
        temp_no = 3
    elif mem == 2 and cpu_cores == 2:
        temp_no = 4

    # 完成vSphere的自动化任务,创建虚拟机,Port-Group等等操作
    vsphere_all_auto(temp_no, vlanid)
    # 在IOS设备上配置DHCP服务器
    ssh_netmiko(vlanid, dhcp_server_ip)
    # 完成Nexus交换机上的自动化任务,创建VLAN,VXLAN,SVI,DHCP Relay等等操作
    nexus_all_auto(vlanid)
    # 完成ASA上的自动化任务,创建OBJ,NAT,ACL等等操作
    asa_all_auto(vlanid, ip)
    return vlanid


if __name__ == "__main__":
    cloud_all_auto(1, 1, 58)

