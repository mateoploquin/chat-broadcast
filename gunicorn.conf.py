# For production use, more robust solution like Redis or RabbitMQ for message queuing might be better but this works.
import threading
from app import process_message_queue

def post_fork(server, worker):
    """
    Calling just after a worker has been forked.
    """
    server.log.info("Worker forked (pid: %s)", worker.pid)
    
    # Starting the queue processing thread inside the new worker
    thread = threading.Thread(target=process_message_queue)
    thread.daemon = True
    thread.start()
    server.log.info("Started queue processing thread in worker %s", worker.pid)
