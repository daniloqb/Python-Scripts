import libvirt
import sys


conn = libvirt.openReadOnly(None)

if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)


hv_info = conn.getInfo()

print 'hv arch            : {0}'.format(hv_info[0])
print 'hv memory          : {0}'.format(hv_info[1])
print 'hv cores:            {0}'.format(hv_info[2])
print 'Mhz speed of hv CPU: {0}'.format(hv_info[3])
print
print hv_info