#!/usr/bin/env ruby

puts ARGV[0].scan(/(((?<=from:)|(?<=to:))(([\w])+|.([\d])+)|(?<=flags:).{12}\d?)/).join
