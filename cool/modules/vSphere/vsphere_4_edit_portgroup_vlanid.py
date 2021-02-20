from cool.modules.vSphere.vsphere_0_sshclient import sshclient_execmd
from cool.modules.vSphere.vsphere_0_login_info import esxi_ip,esxi_username,esxi_password


# 修改Port-Group的VLAN
def edit_pg_vlan_id(vlan_id):
    hostname = esxi_ip
    port = 22
    username = esxi_username
    password = esxi_password
    execmd = "esxcli network vswitch standard portgroup set -p VLAN"+str(vlan_id)+" -v "+str(vlan_id)

    sshclient_execmd(hostname, port, username, password, execmd)


if __name__ == "__main__":
    edit_pg_vlan_id(178)

