# Day 11

class PasswordGenerator

    attr_accessor :password

    def initialize(s)
        @old_password = s
        @password = s
        @array = 'abcdefghjkmnpqrstuvwxyz'
        initialize_hash
    end

    def initialize_hash()
        @hash = Hash.new
        @array.split('').each_with_index do |x,i|
            @hash[x] = @array[(i+1) % @array.size]
        end
    end

    def check_pair(s, num)
        count = 0
        @array.split('').each do |x|
            count += 1 if (s =~ Regexp.new("#{x}#{x}"))
        end
        return count >= num
    end

    def get_straight(i, cnt)
        tmp = ''
        cnt.times do |x|
            tmp += @array[i+x]
        end
        return tmp
    end

    def check_straight(s, cnt)
        (0..(@array.size-cnt)).each do |x|
            return true if (s =~ Regexp.new(get_straight(x, cnt)))
        end
        return false
    end

    def valid?()
        return (check_pair(@password, 2) and check_straight(@password, 3))
    end

    def increase()
        s = @password.reverse
        carry = false
        s.size.times do |i|
            carry = false
            carry = true if s[i] == 'z'
            s[i] = @hash[s[i]]
            break if not carry
        end
        @password = s.reverse
    end
end

s = gets.chomp
k = PasswordGenerator.new s
k.increase
while not k.valid?
    k.increase
end
p k
k.increase
while not k.valid?
    k.increase
end
p k
