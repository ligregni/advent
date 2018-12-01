# Day 12
require 'json'

def traverse(json)
    p json
    sum = 0
    json.each do |k,v|
        if (k.is_a?(Hash) or k.is_a?(Array))
            sum += traverse k
        else
            sum += k.to_i
        end
        if (v.is_a?(Hash) or v.is_a?(Array))
            sum += traverse v
        else
            sum += v.to_i
        end
    end
    return sum
end

input = gets.chomp
json = JSON.parse input
p json
p traverse json
