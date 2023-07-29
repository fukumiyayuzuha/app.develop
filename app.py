from flask import Flask, render_template, request

app = Flask(__name__)

class InteriorApp:
    def __init__(self):
        self.title = "interior destiny"
        self.layouts = ["1K", "2DK", "3LDK"]
        self.destinies = ["金運", "恋愛運", "仕事運"]
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

    def select_destiny(self):
        return render_template("select_destiny.html", destinies=self.destinies)

    def show_confirmation(self, selected_destiny):
        self.selected_destiny = selected_destiny
        return render_template("confirmation.html", selected_destiny=selected_destiny)

    def draw_fortune(self):
        # Implement fortune drawing logic here (omikuji)
        # For this example, we'll just set the fortune percentage randomly
        import random
        self.fortune_percentage = random.randint(0, 100)
        return render_template("draw_fortune.html", fortune_percentage=self.fortune_percentage)

    def show_fortune_details(self):
        return render_template("fortune_details.html", selected_layout=self.selected_layout, selected_destiny=self.selected_destiny, fortune_percentage=self.fortune_percentage)

interior_app = InteriorApp()

@app.route('/')
def home():
    return interior_app.start()

#タイトルページ
@app.route('/')
def show_title():
    return render_template('title.html')

#間取り選択ページ
@app.route('/select_layout', methods=['POST','GET'])
def select_layout():
    layouts = ["1K" , "2DK" , "3LDK"]
    if request.method == 'POST':
        #フォームから送信されたデータを受け取る処理を行う
        selected_layout = request.form['layout']
        #ここで次のページに遷移する処理を実装する
        return interior_app.show_layout_details(selected_layout)
    else:
        return interior_app.select_layout()

@app.route('/select_destiny', methods=['POST', 'GET'])
def select_destiny():
    if request.method == 'POST':
        selected_destiny = request.form['destiny']
        return interior_app.show_confirmation(selected_destiny)
    else:
        return interior_app.select_destiny()

@app.route('/draw_fortune', methods=['POST', 'GET'])
def draw_fortune():
    if request.method == 'POST':
        return interior_app.draw_fortune()
    else:
        return interior_app.show_fortune_details()

if __name__ == '__main__':
    app.run()

