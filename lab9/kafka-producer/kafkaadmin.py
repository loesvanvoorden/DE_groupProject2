from kafka.admin import KafkaAdminClient, NewTopic

def delete_topics(admin):
    admin.delete_topics(topics=['players', 'transfers', 'players_merged_topic', 'avg_transfer_fee_topic'])

def create_topics(admin, topic_list):
    admin.create_topics(new_topics=topic_list, validate_only=False)

if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers="VMIP:9092",
                                    client_id='Lab9')  # use your VM's external IP Here!
    topic_list = [
        NewTopic(name="players", num_partitions=1, replication_factor=1),
        NewTopic(name="transfers", num_partitions=1, replication_factor=1),
        NewTopic(name="players_merged_topic", num_partitions=1, replication_factor=1),
        NewTopic(name="avg_transfer_fee_topic", num_partitions=1, replication_factor=1)
    ]
    create_topics(admin_client, topic_list)
