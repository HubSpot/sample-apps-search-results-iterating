require_relative 'config'
require 'optparse'
require 'ostruct'

class Cli
  def initialize(options)
    @options = options
    @search_query = options[:search_query]
    @batch_size = options[:batch_size] || 10
  end

  def run
    validate

    after = 0

    loop do
      contacts = call_api(after)

      break if contacts.empty?

      yield contacts if block_given?
      after = contacts.last.id
    end
  end

  private

  attr_reader :search_query, :batch_size

  def validate
    raise ArgumentError 'Please, provide search query to call with -q or --query' unless search_query
  end

  def call_api(after)
    search_request = search_request(after)
    api = ::Hubspot::Crm::Contacts::SearchApi.new 
    api.do_search(search_request, auth_names: 'hapikey').results
  end

  def search_request(after)
    filter = ::Hubspot::Crm::Contacts::Filter.new(
      property_name: 'hs_object_id',
      operator: 'GT',
      value: after
    )

    filter_group = ::Hubspot::Crm::Contacts::FilterGroup.new(filters: [filter])

    ::Hubspot::Crm::Contacts::PublicObjectSearchRequest.new(
      query: search_query,
      limit: batch_size,
      filter_groups: [filter_group],
      sorts: [{'propertyName' => 'hs_object_id', 'direction' => 'ASCENDING'}]
    )
  end
end

options = OpenStruct.new
OptionParser.new do |opt|
  opt.on('-q', '--query QUERY', 'Search query') { |o| options.search_query = o }
  opt.on('-s', '--size SIZE', 'Batch size. 10 by default') { |o| options.batch_size = o }
end.parse!

Cli.new(options).run { |contacts| p contacts }
