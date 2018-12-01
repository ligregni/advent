def get_dyn(s)
    code = sprintf "String.new(%s).size", s
    return eval(code)
end

def get_dyn2(s)
    code = sprintf "%%Q/%s/", s
    puts "code #{code} size: #{code.size} #{eval(code).size}"
    x = sprintf "%s", s
    x = eval(s)
    p x, x.size
    return code.size-1
end

def solve1(s)
    return s.size-get_dyn(s)
end

def solve2(s)
    return get_dyn2(s)-(s.size)
end

total1 = 0
total2 = 0
STDIN.each_line do |line|
    input = line.strip
    total1 += solve1(input)
    total2 += solve2(input)
end

puts total1, total2
