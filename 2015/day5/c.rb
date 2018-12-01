def check_vowels(s)
    total = 0
    vowels = 'aeiou'
    vowels.split('').each do |v|
        total += s.count v
    end
    return total >= 3
end

def check_double(s)
    ('a'..'z').each do |x|
        return true if s =~ Regexp.new(x+x)
    end
    return false
end

def check_forbidden(s)
    forbidden = 'acpx'
    forbidden.split('').each do |x|
        return false if s =~ Regexp.new(x+(x.ord+1).chr)
    end
    return true
end

def check_pair(s)
    (s.size-1).times do |i|
        k = s[i]+s[i+1]
        return true if s[(i+2)...s.size] =~ Regexp.new(k)
    end
    return false
end

def check_trio(s)
    s[0...(s.size-2)].split('').each_with_index do |x,i|
        return true if s[i+2] == x
    end
    return false
end

def check(s, c)
    return (check_vowels(s) & check_double(s) & check_forbidden(s)) if c == 1
    return (check_pair(s) & check_trio(s)) if c == 2
end

total1 = 0
total2 = 0
STDIN.each_line do |line|
    total1 += 1 if check line,1
    total2 += 1 if check line,2
end
puts total1
puts total2
