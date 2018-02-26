import pyowm
import facebook

def get_weather(loc):
    '''
    (str) -> None
    '''
    owm = pyowm.OWM('4744dde8ab269330ab8ce3b62f505e74') 

    observation = owm.weather_at_place(loc)
    w = observation.get_weather()
    print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

    # Weather details
    print(w.get_wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.get_humidity())              # 87
    print(w.get_temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

def get_facebook_info(ids, field):
    '''
    (str, str) -> dict
    '''
    graph = facebook.GraphAPI(access_token="EAACEdEose0cBAKdaSqHdaZCkAE1xZAV3\
    ijOjh2HF1GG9mQZA1GZAUeijACi7HV9ZBOo3hToWI6mSGO24wCS5C3vcCY9cNzRDcArbrzpfu\
    HLOJeEnJ2sCNwLNbg58OTeB3M7uyWWyz0ZBZADVrZAzlzsZASdY2HhmmJntrZCALt2c4sz1ou\
    cDNLyI5BtJdZAF44vMuVjvwStkaakCgZDZD", version='2.1')
    events = graph.get_object(id=ids, fields=field)
    return events
