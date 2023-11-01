require_relative 'product'
require_relative 'market'

product = Product.new
product.name = 'Teclado Mecânico'
product.price = 499.99

Marketplace.new(product.name, product.price).buy
