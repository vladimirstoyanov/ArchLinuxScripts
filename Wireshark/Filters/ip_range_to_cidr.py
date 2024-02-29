import ipaddress
startip = ipaddress.IPv4Address('63.223.64.0')
endip = ipaddress.IPv4Address('63.223.127.255')
[ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]
