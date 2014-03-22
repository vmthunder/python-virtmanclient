
import sys
sys.path.append('..')

from vmthunderclient import client

if __name__ == '__main__':
    client = client.Client('10.107.14.163:8001')
    client.list()
    client.create('123456', 'vm6', [], '/dev/loop8')
    client.destroy('vm6')
