# Day 10

def process(s)
    count = 0
    cur = 'x'
    tmp = ''
    s.size.times do |x|
        if s[x] != cur
            tmp += "#{count}#{cur}" if count > 0
            count = 0
        end
        cur = s[x]
        count += 1
    end
    tmp += "#{count}#{cur}" if count > 0
end

def solve(s, t)
    t.times do |x|
        puts "time: #{x}"
        s = process s
    end
    return s.size
end

s = gets.chomp

p solve s,40
p solve s,50

