from aiohttp import web
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '10.12.11.161', 'port': 9200}])

def get_recommend(user_id):
    
    search = es.search(index="recommender", doc_type="recommend", body={"query": {"match": {'userid':user_id}}}, filter_path=['hits.hits._source'])
    
    if (not search):
        return 0

    data = search['hits']['hits'][0]['_source']
    return data

async def index(request):
    data = await request.post()
    
    user_id = data['userid']
    print ('userid:', user_id)

    rs = get_recommend(user_id)
    result = {"result":rs}

    return web.json_response(result)
