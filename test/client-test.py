
import sys
sys.path.append('..')

from vmthunderclient import client

if __name__ == '__main__':
    prop0 = {}
    prop0['target_portal'] = '10.107.14.50:3260'
    prop0['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop0['target_lun'] = 1

    prop1 = {}
    prop1['target_portal'] = '10.107.14.161:3260'
    prop1['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop1['target_lun'] = 1

    prop2 = {}
    prop2['target_portal'] = '10.107.14.162:3260'
    prop2['target_iqn'] = 'iqn.2010-10.org.openstack:1'
    prop2['target_lun'] = 1

    client1 = client.Client('10.107.14.161:8001')
    client1.list()
    client1.create('1', 'vm6', [prop0], '/dev/loop1')
    client1.list()
'''
    client2 = client.Client('10.107.14.162:8001')
    client2.list()
    client2.create('1', 'vm6', [prop1], '/dev/loop1')
    client2.list()
    
    client3 = client.Client('10.107.14.163:8001')
    client3.list()
    client3.create('1', 'vm6', [prop1], '/dev/loop1')
    client2.list()
'''
