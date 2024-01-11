local exclude_list = {
  {"203.0.113.0/24", "Google"},
  {"131.247.48.0/20", "Microsoft"},
  {"157.240.221.0/24", "Facebook"}
}

function is_excluded(ip_addr)
  for _, exclude_range in ipairs(exclude_list) do
    if ip_addr:match(exclude_range[1]) then
      return true
    end
  end

  return false
end

function dissect_ip(buffer, pktinfo, tree)
  local ip_src_f = Field.new("ip.src")
  local ip_dst_f = Field.new("ip.dst")

  local ip_src = ip_src_f()
  local ip_dst = ip_dst_f()

  if is_excluded(ip_src) or is_excluded(ip_dst) then
    pktinfo.not_displayed = true
  end
end

dissector_table = DissectorTable.get("tcp.port")
dissector_table:add(80, dissect_ip)

dissector_table = DissectorTable.get("udp.port")
dissector_table:add(53, dissect_ip)
