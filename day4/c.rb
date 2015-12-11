require 'digest'

def solve(s, r)
    x = 1
    while true
        d = Digest::MD5.hexdigest(s+x.to_s)
        return x if d =~ r
        x += 1
    end
end

input = readline
p solve(input.chomp, /^00000/)
p solve(input.chomp, /^000000/)
