# Open and set content equal to txt file in directory
try:
    with open('input queue-1-1.txt', 'r') as file:
        # Read the entire contents of the file
        content = file.readlines()
except FileNotFoundError:
    content = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
               "E Vicky", "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete", "P Dee",
               "S Bill", "S Chase", "E Price", "P Dee", "E Sue"]


# Initialize queues as lists
premium_queue = []
standard_queue = []
economy_queue = []

# Append packets to corresponding queues
for packet in content:
    priority, packet_content = packet.split(maxsplit=1)
    if priority == 'P':
        premium_queue.append(packet_content.strip())  # Remove trailing newline
    elif priority == 'S':
        standard_queue.append(packet_content.strip())
    elif priority == 'E':
        economy_queue.append(packet_content.strip())

# Weighted Fair Queue (WFQ) algorithm
while premium_queue or standard_queue or economy_queue:
    # Dequeue 3 Priority packets
    for _ in range(3):
        if premium_queue:
            print(premium_queue.pop(0))
    # Dequeue 2 Standard packets
    for _ in range(2):
        if standard_queue:
            print(standard_queue.pop(0))
    # Dequeue 1 Economy packet
    if economy_queue:
        print(economy_queue.pop(0))
