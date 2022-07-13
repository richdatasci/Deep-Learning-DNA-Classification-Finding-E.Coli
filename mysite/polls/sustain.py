from django.core.cache import cache
import pickle

model_cache_key = 'model_cache'
# this key is used to `set` and `get` your trained model from the cache

model = cache.get(model_cache_key) # get model from cache

if model is None:
    # your model isn't in the cache
    # so `set` it
    filename = 'polls/E-Coli_model.pickle'
    model = pickle.load(open(filename, 'rb'))
    cache.set(model_cache_key, model, None) # save in the cache in above line, None is the timeout parameter. It means cache forever

