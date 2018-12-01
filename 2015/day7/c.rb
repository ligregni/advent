MOD = 2 ** 16

class String
    def is_integer?
        self.to_i.to_s == self
    end
end


class Wire
    attr_writer :answer
    def initialize(h, name)
        @name = name
        @hash = h
        @answer = nil
    end
    def process_input(input)
        @requirements = input
    end
    def get_answer(input)
        return input.to_i if input.is_integer?
        return @hash[input].get_output
    end
    def get_output
        return @answer if @answer
        results = Array.new
        op = :+
        puts "processing #{@name} #{@requirements}"
        if @requirements =~ /SHIFT/
            op = :<< if @requirements =~ /LSHIFT/
            op = :>> if @requirements =~ /RSHIFT/
            results << get_answer(@requirements.split[0])
            results << get_answer(@requirements.split[-1])
        elsif @requirements =~ /NOT/
            results << ~(get_answer @requirements.split[-1])
        elsif @requirements.split.size > 1
            op = :& if @requirements =~ /AND/
            op = :| if @requirements =~ /OR/
            results << (get_answer @requirements.split[0])
            results << (get_answer @requirements.split[-1])
        else
            results << (get_answer @requirements.split[0])
        end
        r = results.reduce(op)
        r %= MOD
        @answer = r
        puts "for #{@name} the answer is #{@answer}: #{@requirements}"
        return @answer
    end
end

def process_line(h, line)
    input,output = line.split('->')
    output = output.split[0]
    h[output] = Wire.new(h,output) if not h.include? output
    h[output].process_input(input)
end

h = Hash.new
STDIN.each_line do |line|
    process_line h,line
end

a = h['a'].get_output

h.each_key do |k|
    h[k].answer = nil
end

h['b'].answer = a

aa = h['a'].get_output

p a, aa
