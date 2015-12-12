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

def toggle(light)
    !light
end

def turn(on, light)
    on 
end

def turn_int(value, light)
    [0, light + value].max
end

def bind_functor(f, closure)
    return lambda { |x|
        f.call(closure, x)
    }
end

def santa(type, lights, instruction, coordinates)
    start = coordinates[0]
    ends  = coordinates[1]
    xx = [start[0], ends[0]].sort
    yy = [start[1], ends[1]].sort
    function = nil
    if type == 1
        function = bind_functor(method(:turn), instruction == 'on')
        function = method(:toggle) if instruction == 'toggle'
    else
        closure = 2
        closure = 1 if instruction == 'on'
        closure = -1 if instruction == 'off'
        function = bind_functor(method(:turn_int), closure)
    end
    lights[xx[0]..xx[1]].each { |row|
        row.map!.with_index { |x,i| ( (yy[0]..yy[1]).include?(i) ? function.call(x) : x ) }
    }
end

MAX = 1000
lights1 = Array.new(MAX) {Array.new(MAX,false)}
lights2 = Array.new(MAX) {Array.new(MAX,0)}
STDIN.each_line do |line|
    instruction,coordinates = get_instruction line
    santa(1, lights1, instruction, coordinates)
    santa(2, lights2, instruction, coordinates)
end
puts (lights1.map { |row| row.count true }).reduce(:+)
puts (lights2.map { |row| row.reduce(:+) }).reduce(:+)
