#coding:utf-8

from amqplib import client_0_8 as amqp
import sys

conn = amqp.Connection(host="localhost:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

msg = amqp.Message(sys.argv[1])
msg.properties["delivery_mode"] = 2
chan.basic_publish(msg,exchange="sorting_room",routing_key="jason")

chan.close()
conn.close()


'''
打开一个终端，执行:
python amqp_consumer.py
让消费者运行，并且创建队列、交换机和绑定。
然后在另一个终端运行:
python amqp_publisher.py "AMQP rocks."

如果一切良好，你应该能够在第一个终端看到输出的消息。
'''
