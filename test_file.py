
#import sys
#sys.path.open('src/vibeAI23')
from src.vibeAI23 import data_breache, predict_breach

def test_allow_traffic():
    data = data_breache(
        Source_Port=125,
        Destination_Port=80,
        NAT_Source_Port=54,
        Bytes=10,
        Bytes_Sent=500,
        Bytes_Received=50,
        Packets=10,
        Elapsed_Time=5,
        pkts_sent=5,
        pkts_received=5
    )
    IP_ADD = '127.0.0.1'
    result = predict_breach(data, IP_ADD)
    
    assert result['prediction'] == 'allow'
    print('allow')
    assert not result['blocked']
        
test_allow_traffic()