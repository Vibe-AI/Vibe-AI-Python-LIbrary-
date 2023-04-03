import pickle
import socket
from pydantic import BaseModel

class data_breache(BaseModel):
    Source_Port: float
    Destination_Port: float
    NAT_Source_Port: float
    Bytes: float
    Bytes_Sent: float
    Bytes_Received: float
    Packets: float
    Elapsed_Time: float
    pkts_sent: float
    pkts_received: float

def load_model():
    pickle_in = open("model/firewall_model.pkl", "rb")
    classifier = pickle.load(pickle_in)
    return classifier


def block_ip(IP_ADD):

    # Define the IP address you want to block
    ip_to_block = IP_ADD
    print("Blocking suspicious traffic...")

    # Create a TCP/IP socket and bind it to the IP address to block
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip_to_block, 0))
    
    # Set the socket to listen for incoming connections
    sock.listen(1)
    
    # Run a loop to accept incoming connections and close them immediately
    while True:
        conn, addr = sock.accept()
        conn.close()


def predict_breach(data, IP_ADD):
    classifier = load_model()
    data = data.dict()
    Source_Port = data['Source_Port']
    Destination_Port = data['Destination_Port']
    NAT_Source_Port = data['NAT_Source_Port']
    Bytes = data['Bytes']
    Bytes_Sent = data['Bytes_Sent']
    Bytes_Received = data['Bytes_Received']
    Packets = data['Packets']
    Elapsed_Time = data['Elapsed_Time']
    pkts_sent = data['pkts_sent']
    pkts_received = data['pkts_received']
    prediction = classifier.predict([[Source_Port,Destination_Port,NAT_Source_Port,Bytes,Bytes_Sent,Bytes_Received,Packets,Elapsed_Time,pkts_sent,pkts_received]])
    if prediction[0] == 0:
        prediction = "allow"
    elif prediction[0] == 1:
        prediction = "drop"
    elif prediction[0] == 2:
        prediction = "deny"
    else:
        prediction = "reset-both"
    
    blocked = False
    if prediction in ["drop", "deny"]:
        
        blocked = True
        block_ip(IP_ADD)
        
        
        
    else:
        pass

    
    return {
        'prediction': prediction,
        "blocked" : blocked
    }

