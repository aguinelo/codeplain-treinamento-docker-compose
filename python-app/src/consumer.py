import pika, os

def run():    

    try:
        url = os.environ.get('CLOUDAMQP_URL', 'amqp://admin:123456@rabbitmq/%2f')
        params = pika.URLParameters(url)
        params.socket_timeout = 5

        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='hello-docker')

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(
            queue='hello-docker', 
            on_message_callback=callback, 
            auto_ack=True
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    except Exception as error:
        print(f"Error: {str(error)}")

if __name__ == "__main__":
    run()
