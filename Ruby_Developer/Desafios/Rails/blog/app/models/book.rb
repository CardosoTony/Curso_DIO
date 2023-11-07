class Book < ApplicationRecord
  validates :title, :author, :score, presence: true
end
