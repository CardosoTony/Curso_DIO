numbers = []

positions = [
  'primeiro',
  'segundo',
  'terceiro'
]

puts 'Calcular terceira potência'

for position in positions
  print "Digite o #{position} valor: "
  numbers.push(gets.chomp.to_i)
end

print "Valores de entrada: #{numbers}\n"

numbers.map! do |number|
  number ** 3
end

print "Valores calculados: #{numbers}\n"
