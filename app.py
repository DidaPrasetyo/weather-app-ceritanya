from unittest import result
from flask import Flask, render_template, url_for
import tensorflow as tf
import thinkspeak as ts
import numpy as np

app = Flask(__name__, template_folder='templates')

def predict_result(array, array_max):
  i = 0
  weather = ['Rain','Clouds','Thunderstorm','Clear','Haze','Dust','Fog','Mist','Squall','Tornado','Smoke','Drizzle','Ash']
  # print(array, array_max)
  for nilai in array:
    if nilai == array_max:
      # print(weather[i])
      return i, weather[i]
    i += 1
  return None

@app.route('/')
def main():
  temp = float(ts.read_data(1))
  humidity = float(ts.read_data(2))
  pressure = float(ts.read_data(3))
  # print(temp, humidity, pressure)

  new_model = tf.keras.models.load_model('model/cobamodel2.h5')
  data_masuk = [temp,    humidity,    pressure]
  data_masuk = np.array(data_masuk).reshape(-1,3)
  cobalagi = new_model.predict(data_masuk)

  predict = predict_result(cobalagi[0],cobalagi[0].max())
  # print(predict_result(cobalagi[0],cobalagi[0].max()))

  return render_template('main.html', result=predict[1], info=[temp, humidity, pressure])
  # return(predict_result(cobalagi[0],cobalagi[0].max()))
  # return f"Weather {predict[1]}!"

if __name__ == '__main__':
  app.run()