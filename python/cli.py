import os
import argparse
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup

def api_key():
  load_dotenv()
  return os.environ['HUBSPOT_API_KEY']

def search_next_contacts_batch(after, limit, search_query):
  filter_ = Filter(property_name="hs_object_id", operator="GT", value=after)
  filter_groups = [FilterGroup(filters=[filter_])]

  public_object_search_request = PublicObjectSearchRequest(
    query=search_query,
    limit=limit,
    filter_groups=filter_groups,
    sorts=[{"propertyName": "hs_object_id", "direction": "ASCENDING"}],
  )

  api_client = HubSpot(api_key=api_key())
  response = api_client.crm.contacts.search_api.do_search(
    public_object_search_request=public_object_search_request,
  )

  return response.results

def iterate_via_search_results(search_query, process_contact_func, batch_size=10):
  after = 0
  while True:
    contacts = search_next_contacts_batch(
      search_query=search_query, after=after, limit=batch_size
    )

    if len(contacts) == 0:
      break

    for contact in contacts:
      process_contact_func(contact)

    after = contacts[-1].id

parser = argparse.ArgumentParser(description='Parse Hubspot API arguments')
parser.add_argument('-q', '--query', help='Search query')
parser.add_argument('-s', '--size', help='Batch size')
args = parser.parse_args()

if (args.query is None):
  raise Exception('Please, provide search query to call with -q or --query. See --help to get more info.')

iterate_via_search_results(
  search_query=args.query,
  process_contact_func=lambda contact: print(
    "Processing contact_id={}".format(contact.id)
  ),
  batch_size=args.size
)
