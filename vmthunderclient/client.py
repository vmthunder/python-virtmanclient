import requests
from vmthunderclient.openstack.common import jsonutils

class Client(object):
    USER_AGENT = 'python-vmthunderclient'
    def __init__(self, endpoint, *args, **kwargs):
        self.endpoint = endpoint

    def _get_url(self, function):
        return "http://%s/%s" % (self.endpoint, function)

    def _get_kwargs(self, body={}):
        kwargs = {}
        kwargs.setdefault('headers', kwargs.get('headers', {}))
        kwargs['headers']['Accept'] = 'application/json'
        kwargs['headers']['Content-Type'] = 'application/json'
        if not body == {}:
            kwargs['body'] = jsonutils.dumps(body)
        return kwargs

    def _get(self,url):
        resp = requests.request('GET', url)
        return resp

    def _post(self, url, body):
        kwargs = self._get_kwargs(body)
        resp = requests.request('POST', url, kwargs)
        return resp

    def list(self):
        url = self._get_url('list')
        resp = self._get(url)
        instances = jsonutils.loads(resp.content)
        return instances

    def create(self, image_id, vm_name, connections, snapshot_dev):
        url = self._get_url('create')
        body = {
            'image_id':image_id,
            'vm_name':vm_name,
            'connections':connections,
            'snapshot_dev':snapshot_dev
        }
        self._post(url, body)

    def destroy(self, vm_name):
        url = self._get_url('destroy')
        body = {
             'vm_name':vm_name,
        }
        self._post(url, body)
