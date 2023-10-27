require 'cpf_cnpj'

def check_cpf(cpf_number)
  if CPF.valid?(cpf_number)
    return 'CPF válido!'
  else
    return 'CPF inválido!'
  end
end

print 'Digite o número do CPF: '
cpf_number = gets.chomp.to_i

result = check_cpf(cpf_number)

puts result
