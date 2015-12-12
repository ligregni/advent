STDIN.each_line do |line|
    input = line.strip
    p input, input.size, input.to_s
    p [input].pack('H*')
end

