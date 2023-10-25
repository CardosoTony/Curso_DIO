require 'complex'

def clear_screen
  system('clear')
end

operations = [
  '0. Sair',
  '1. Somar',
  '2. Subtrair',
  '3. Multiplicar',
  '4. Dividir',
  '5. Raiz Quadrada'
]

def print_menu(menu)
  max_length = menu.map { |op| op.length }.max + 4
  horizontal_line = '─' * (max_length)

  puts "\n┌" + horizontal_line + '┐'

  menu.each do |operation|
    padding = max_length - operation.length - 2
    menu_line = "|  #{operation}#{' ' * padding}|"
    puts menu_line
  end

  puts '└' + horizontal_line + '┘'
end

def print_result(results)
  results_str = results.to_s
  max_length = results_str.length + 4

  horizontal_line = '─' * (max_length)
  puts "\n┌" + horizontal_line + '┐'
  puts "|  #{results}  |"
  puts '└' + horizontal_line + '┘'
end

loop do
  puts 'Aplicação - Calculadora'

  print_menu(operations)

  print "\nSelecione a operação: "
  input = gets.chomp
  clear_screen

  if input.match?(/\A\d+\z/)
    operation = input.to_i

    if (0..5).include?(operation)
      if operation == 0
        puts "\nAté breve!"
        break
      end

      puts "\n#{operations[operation]}"

      valid_number_regex = /\A\d+(\.\d+)?\z/

      if operation == 5
        while true
          print "\nDigite um valor: "
          first_value = gets.chomp

          if first_value.match?(valid_number_regex)
            first_value = first_value.to_f
            break
          else
            puts "\nEntrada inválida! Por favor insira um número."
          end
        end
      else
        while true
          print "\nDigite um valor: "
          first_value = gets.chomp

          if first_value.match?(valid_number_regex)
            first_value = first_value.to_f
            break
          else
            puts "\nEntrada inválida! Por favor insira um número."
          end
        end

        while true
          print "\nDigite o segundo valor: "
          second_value = gets.chomp

          if second_value.match?(valid_number_regex)
            second_value = second_value.to_f
            break
          else
            puts "\nEntrada inválida! Por favor insira um número."
          end
        end
      end

      case operation
      when 1
        result = "#{first_value} + #{second_value} = #{first_value + second_value}"
        print_result(result)
      when 2
        result = "#{first_value} - #{second_value} = #{first_value - second_value}"
        print_result(result)
      when 3
        result = "#{first_value} * #{second_value} = #{first_value * second_value}"
        print_result(result)
      when 4
        if second_value.zero?
          result = "Divisão por zero não é permitida."
          print_result(result)
        else
          result = "#{first_value} / #{second_value} = #{first_value / second_value}"
          print_result(result)
        end
      when 5
        result = "√#{first_value} = #{Math.sqrt(first_value)}"
        print_result(result)
      end

      print "\nPressione Enter para continuar..."
      gets.chomp
      clear_screen

    else
      puts "\nOperação inválida! Por favor digite um valor entre 0 e 5."
      print "\nPressione Enter para continuar..."
      gets.chomp
      clear_screen
    end
  else
    puts "\nEntrada inválida! Por favor digite um número válido!"
    print "\nPressione Enter para continuar..."
    gets.chomp
    clear_screen
  end
end