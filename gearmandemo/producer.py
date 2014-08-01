import time
from gearman import GearmanClient, Task

client = GearmanClient(["10.7.50.12"])

for i in range(5):
    client.dispatch_background_task('speak', i)
    print 'Dispatched %d' % i
    time.sleep(1)
