from gearman import GearmanWorker

def speak(job):
    r = 'Hello %s' % job.arg
    print r
    return r

worker = GearmanWorker(["10.7.50.12"])
worker.register_function('speak', speak, timeout=3)
worker.work()
