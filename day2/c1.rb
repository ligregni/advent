class RoundRobin
    attr_accessor :array
    def initialize(array)
        @array = array
    end

    def traverse()
        @array.each_with_index do |x, i|
            @array[(i+1)...(@array.length)].each do |y|
                yield x, y
            end
        end
    end
end

def get_measures(measures)
    k = Array.new
    measures.traverse do |a,b|
        k << a*b
    end
    return k
end

def get_perimeter(measures)
    k = Array.new
    measures.traverse do |a,b|
        k << a*2 + b*2
    end
    return k.min
end

def get_paper_area(measures)
    total = 0
    k = get_measures(measures)
    k.each do |x|
        total += x * 2
    end
    total += k.min
end

def get_ribbon_length(measures)
    total = 0
    total += get_perimeter measures
    total += measures.array[0] * measures.array[1] * measures.array[2]
    return total
end

paper = 0
ribbon = 0
STDIN.each_line do |line|
    measures = RoundRobin.new line.split('x').map(&:to_i)
    paper += get_paper_area measures
    ribbon += get_ribbon_length measures
end
puts paper
puts ribbon
