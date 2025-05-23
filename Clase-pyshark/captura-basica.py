import pyshark

cap = pyshark.LiveCapture(interface='enx00e04c68039b')
for pkt in cap.sniff_continuously():  # sin límite
    print(pkt)
