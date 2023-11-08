import sys
import dpkt
from dpkt.utils import mac_to_str, inet_to_str





def main():
    args = sys.argv[1:]
    print(args)
    with open(args[0],'rb') as logfile:
        pcap = dpkt.pcap.Reader(logfile)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            eth.pprint()





if __name__ == "__main__":
    main()



