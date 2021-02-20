import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests.auth import HTTPBasicAuth

# ESXI IP地址/用户名/密码
esxi_ip = '192.168.3.110'
esxi_username = 'root'
esxi_password = 'YUting@123'

# vCenterIP地址/用户名/密码
vcip = '192.168.3.101'
username = 'administrator@vsphere.local'
password = 'YUting@123'

# vCenter登录并且获取Cookie的URL链接
login_url = 'https://' + vcip + '/rest/com/vmware/cis/session'  # 请求的URL


# 登录,获取Cookie并且维持会话
def get_session():
    client = requests.session()
    client.post(login_url, auth=HTTPBasicAuth(username, password), verify=False)

    return client


vc_session = get_session()

