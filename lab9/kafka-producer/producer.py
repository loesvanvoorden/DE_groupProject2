import csv
import json
from kafka import KafkaProducer
import threading

def kafka_python_producer_sync(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8'))
    print("Sending " + msg)
    producer.flush(timeout=60)

def success(metadata):
    print(metadata.topic)

def error(exception):
    print(exception)

def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    producer.flush()

def produce_from_file(producer, file, topic):
    print(file)
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            kafka_python_producer_sync(producer, json.dumps(row), topic)

def run_job():
    producer = KafkaProducer(bootstrap_servers='VMIP:9092')  # use your VM's external IP Here!
    t1 = threading.Thread(target=produce_from_file,
                          args=(producer, '/Users/leviwarren/Downloads/lab9/data/players.csv', 'players'))
    t2 = threading.Thread(target=produce_from_file,
                          args=(producer, '/Users/leviwarren/Downloads/lab9/data/transfers.csv', 'transfers'))
    t1.start()
    t2.start()

if __name__ == '__main__':
    run_job()
