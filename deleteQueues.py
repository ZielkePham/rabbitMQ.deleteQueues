import pika
import json

def getRbmqParam():
    with open('settingsTest.json') as fi:
        settings = json.load(fi)        
        username, password, hostname, port, vhost, rbmqqueue = settings.get('username'), settings.get('password'), settings.get('hostname'), settings.get('port'), settings.get('vhost'), settings.get('rbmqqueue')
        connectRBMQ(username, password, hostname, port, vhost, rbmqqueue)

def connectRBMQ(username, password, hostname, port, vhost, rbmqqueue):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(hostname,
                                           port,
                                           vhost,
                                           credentials)    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    with open('deleteQueues.json') as fi1:
        queueNames = json.load(fi1)
        for queueName in queueNames:
            channel.queue_delete(queue=queueName)
            print(queueName +" has been deleted!")
    connection.close()   

def main():
    getRbmqParam()

main()


##currentDate = datetime.datetime.now() - datetime.timedelta(days=1)
##eodDate = currentDate.strftime("%Y%m%d")
##print(eodDate)

##if len(sys.argv) == 2:
##    eodDate = sys.argv[1]