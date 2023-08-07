from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.debug = True

class InteriorApp:
    def __init__(self):
        self.title = "interior destiny"
        self.layouts = ["1K", "2DK", "3LDK"]  # レイアウトの選択肢を追加する
        self.destinies = ['金運', '恋愛運', '仕事運']
        self.selected_layout = None
        self.selected_destiny = None
        self.fortune_percentage = 0

    def start(self):
        return self.show_title()

    def show_title(self):
        return render_template("title.html", title=self.title)

    def select_layout(self):
        return render_template("select_layout.html", layouts=self.layouts)

    def show_layout_details(self, selected_layout):
        self.selected_layout = selected_layout
        return render_template("layout_details.html", selected_layout=selected_layout)


    def confirmation(self, selected_destiny):
        return render_template("confirmation.html", selected_destiny=selected_destiny)


    def draw_fortune(self):
        import random
        self.fortune_percentage = random.randint(0, 100)
        return render_template("confirmation.html", fortune_percentage=self.fortune_percentage)

    def get_fortune_data(self):
        url = 'https://api.open-meteo.com/v1/forecast?latitude=35.0211&longitude=135.7538&hourly=rain&timezone=Asia%2FTokyo'

        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            return None
    
    def draw_fortune(self):
        fortune_data = self.get_fortune_data()
        if fortune_data:
            return render_template("draw_fortune.html", fortune_data=fortune_data)
        else:
            return "Error: Failed to fetch data from the API."



    def show_fortune_details(self):
        return render_template("fortune_details.html", selected_layout=self.selected_layout, selected_destiny=self.selected_destiny, fortune_percentage=self.fortune_percentage)

interior_app = InteriorApp()

@app.route('/')
def home():
    return interior_app.start()

@app.route('/select_layout', methods=['POST', 'GET'])
def select_layout():
    app_instance = InteriorApp()
    if request.method == 'POST':
        selected_layout = request.form['layout']
        return app_instance.show_layout_details(selected_layout)
    return app_instance.select_layout()

@app.route('/confirmation', methods=['POST', 'GET'])
def confirmation():
    if request.method == 'POST':
        # フォームが送信されたら、draw_fortune()メソッドを呼び出す
        return draw_fortune()
    else:
        # フォームが送信されていない場合は、confirmation.htmlを表示する
        app_instance = InteriorApp()
        return app_instance.confirmation()



@app.route('/draw_fortune')
def draw_fortune():
    app_instance = InteriorApp()
    return app_instance.draw_fortune()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')