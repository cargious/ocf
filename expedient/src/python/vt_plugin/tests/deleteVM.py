import os
import sys
from os.path import dirname, join

PYTHON_DIR = join(dirname(__file__), '/opt/ofelia/expedient/src/python/')

# This is needed because wsgi disallows using stdout
sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'expedient.clearinghouse.settings'

sys.path.insert(0,PYTHON_DIR)


from vt_plugin.models import *

vmid = str(sys.argv[1])

vm = VM.objects.get(id = vmid)
server = VTServer.objects.get(uuid = vm.serverID)
server.vms.remove(vm)
vm.completeDelete()
