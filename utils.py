from keras.models import model_from_json


def save_model_weights(model):
    model_json = model.to_json()
    with open('model/drake-model.json', 'w') as json_file:
        json_file.write(model_json)
        print('saved model')
    
    model.save_weights('model/drake-weights.h5')
    print('saved weights')


def load_model():
    json_file = open('model/drake-model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    print('loaded model')
    
    loaded_model.load_weights('model/drake-weights.h5')
    print('loaded weigths')
