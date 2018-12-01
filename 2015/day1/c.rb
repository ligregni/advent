def santa(input)
    count = 0
    input.split('').each_with_index do |c, i|
        count += ( if c == '(' then 1 else -1 end )
        return i + 1 if count == -1
    end
end

input = STDIN.read
puts santa input
