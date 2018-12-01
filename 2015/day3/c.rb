require 'set'

def solve(line, caso)
    s = Set.new
    santa = [0,0]
    robot = [0,0]
    wey = [santa, robot]
    s << wey[0].clone
    total = 1
    line.split('').each do |c|
        wey[0][0] -= 1 if c == '<'
        wey[0][0] += 1 if c == '>'
        wey[0][1] -= 1 if c == 'v'
        wey[0][1] += 1 if c == '^'
        s << wey[0].clone
        wey.rotate! if caso == 2
    end
    return s.size
end

line = readline
puts solve line, 1
puts solve line, 2
