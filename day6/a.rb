def get_coordinates(token)
    return token.split(',').map(&:to_i)
end

def get_instruction(line)
    tokens = line.split
    instruction = nil
    coordinates = [nil,nil],[nil,nil]
    if line =~ /^turn/
        instruction = tokens[1]
        coordinates[0] = get_coordinates tokens[2]
        coordinates[1] = get_coordinates tokens[4]
    elsif line =~ /^toggle/
        instruction = 'toggle'
        coordinates[0] = get_coordinates tokens[1]
        coordinates[1] = get_coordinates tokens[3]
    end
    return instruction,coordinates
end

class Light
    def initialize(value)
        @light = value
    end

    def toggle()
        @light = !@light
    end

    def turn()
        @light = true 
    end

    def is_on()
        return @light
    end
end

def santa(lights, instruction, coordinates)
    start = coordinates[0]
    ends  = coordinates[1]
    function = :turn
    function = :toggle if instruction == 'toggle'
    lights[start[0], ends[0]+1].each { |row|
        row[start[1], ends[1]+1].map! &function
    }
    return lights
end
    
#MAX = 1000
MAX = 3
lights = Array.new(MAX) {Array.new(MAX) {Light.new(false)}}
STDIN.each_line do |line|
    instruction,coordinates = get_instruction line
    santa(lights, instruction, coordinates)
end
puts (lights.map { |row| row.count { |light| light.is_on } }).reduce(:+)
