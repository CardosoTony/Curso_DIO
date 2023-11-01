class Marketplace
  def initialize(product, price)
    @product = product
    @price = price
  end

  def buy
    puts "Você comprou o produto: #{@product} por R$ #{@price}"
  end
end
