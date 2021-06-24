#/usr/bin/env python3

proto = [ "ssh", "http", "https" ]
protoa = [ "ssh", "http", "https" ]
print(proto)
proto.append("dns") # append dns to list
protoa.append("dns") # append dns to list
print(proto)
proto2 = [ 22, 88, 443, 53 ] # list of common ports
proto.extend(proto2) # pass proto2 as arg to extend method
print(proto)
protoa.append(proto2) # proto2 as arg to append method
print(protoa)

print(proto.count("ssh")) # count list for ssh and print valu

print()
# list proto then reverse it and print again
print(proto)
proto.reverse()
print(proto)

