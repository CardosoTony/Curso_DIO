print 'Digite seu nome: '
firstName = gets.chomp.capitalize

print 'Digite seu sobrenome: '
lastName = gets.chomp.capitalize

print 'Digite sua idade: '
age = gets.chomp.to_i

puts "#{firstName} #{lastName}, #{age} anos."