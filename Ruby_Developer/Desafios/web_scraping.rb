require 'nokogiri'
require 'net/http'

https = Net::HTTP.new('example.com', 443)

https.use_ssl = true

response = https.get('/')

doc = Nokogiri::HTML(response.body)

tag = doc.at('p')
puts tag.content

last_post = doc.at('p a')
puts last_post.content
puts last_post['href']
