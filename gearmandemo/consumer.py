from gearman import GearmanWorker

def speak(job):
    r = 'Hello %s' % job.arg
    print r
    return r

worker = GearmanWorker(["127.0.0.1"])
worker.register_function('speak', speak, timeout=3)
worker.work()
