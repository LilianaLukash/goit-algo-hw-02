from queue import Queue
import random

class Request:
    def __init__(self, request_id):
        self.request_id = request_id

    def process(self):
        print(f"Processing request {self.request_id}")

def generate_request(request_queue, request_id):
    new_request = Request(request_id)
    request_queue.put(new_request)
    print(f"Generated request {request_id}")

def process_request(request_queue):
    if not request_queue.empty():
        request = request_queue.get()
        request.process()
    else:
        print("The queue is empty.")

def main():
    request_queue = Queue()
    request_id = 1

    try:
        while True:
            user_input = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ").strip().lower()
            if user_input == 'g':
                generate_request(request_queue, request_id)
                request_id += 1
            elif user_input == 'p':
                process_request(request_queue)
            elif user_input == 'q':
                print("Exiting application.")
                break
            else:
                print("Invalid input. Please try again.")
    except KeyboardInterrupt:
        print("\nApplication exited.")

if __name__ == "__main__":
    main()