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
    
    def select_destiny(self):
        return render_template("select_destiny.html", destinies=self.destinies)
    
    def show_confirmation(self, selected_destiny):
        self.selected_destiny = selected_destiny
 
        return render_template("confirmation.html", selected_destiny=selected_destiny)
    
    def confirmation(self, selected_destiny):
        return render_template("confirmation.html", selected_destiny=selected_destiny)
    
    def draw_fortune(self):
        fortune_data = self.get_fortune_data()
        selected_destiny = self.selected_destiny
        if fortune_data and selected_destiny is not None:
            rain_mm = fortune_data.get('hourly', {}).get('rain', 0)
            fortune_result = self.get_fortune_result(rain_mm, selected_destiny)   
            return render_template("draw_fortune.html", fortune_result=fortune_result, fortune_data=fortune_data, selected_destiny=self.selected_destiny)
        else:
            return "Error: Failed to fetch data from the API.app.pyコードのエラー"

    def get_fortune_data(self):
        url = 'https://api.open-meteo.com/v1/forecast'
        
        query_params = {
            'latitude': '35.0211',
            'longitude': '135.7538',
            'hourly': 'rain',
            'timezone': 'Asia/Tokyo',
        }
        response = requests.get(url, params=query_params) # APIにリクエストを送信してレスポンスを取得します
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print('Error: Failed to fetch data from the API. Status code:', response.status_code)
            return None

    def get_fortune_result(self, rain_mm, selected_destiny):
        import random
        
        #こっちに雨の場合のおみくじ結果を書く
        if rain_mm == 0.0:
            if selected_destiny == '金運':
                fortune = random.choice([
                    '傘にゴールドのリボンをつけ玄関に置く',
                    'ハンガーを洗面所におく',
                    '鏡をいつもと逆の方に向ける',
                    'ゴミ箱の位置を変える',
                    '寝室の枕の位置を逆にする',
                    '水回りの掃除',
                    '料理の際に自然の音楽を流す',
                    '窓をあける',
                    'テレビのリモコンの置く位置を変える',
                    '冷蔵庫の中を整理整頓',
                ])
            elif selected_destiny == '恋愛運':
                fortune = random.choice([
                    '換気をする',
                    '長い傘を玄関に置く',
                    '寝室でアロマを焚く',
                    'テーブルの位置を変える',
                    '水回りに花を活ける',
                    'シンクの掃除',
                    'ベットメイキング',
                    '部屋の明るい所で本を読む',
                    'リビングで音楽をかける',
                    'カーテンをなるべく閉める'
                ])
            elif selected_destiny == '仕事運':
                fortune = random.choice([
                    '窓をあける',
                    '木製のデスクを使う',
                    '間接照明など温かみの照明を使う'
                    'アロマディフューザーを置く',
                    'ブランケットを使う',
                    '窓辺に観葉植物を置く',
                    'ローズゴールドや銅色の小物を置く',
                    'ハーバリウムを置く',
                    'コーヒーメーカーやお気に入りのマグカップを置く',
                    'アーティストの絵筆セットをデスクに置く'
                ])
        
        #こっちに晴れの場合のおみくじ結果を書く
        else:
            if selected_destiny == '金運':
                fortune = random.choice([
                    '窓をあける',
                    '洗濯をする',
                    '黄色い物を西に置く',
                    '財布の中のお金を数える',
                    '玄関に観葉植物を置く',
                    '玄関に鏡を置く',
                    '北枕にして寝る',
                    'カーテンに薄い黄色のものを貼る',
                    'カーテンを一日中あけておく',
                    '靴を靴箱にしまう'
                ])
            elif selected_destiny == '恋愛運':
                fortune = random.choice([
                    '窓を開けて風通しよくする',
                    '南東にピンクのものを置く',
                    '花を飾る',
                    'リビングに白のものを置く',
                    'クッションを整える',
                    '玄関に観葉植物を置く',
                    '香水を部屋にかける',
                    'ベットメイキング',
                    '枕の向きを南東にする',
                    '玄関マットを敷く'
                ])
            elif selected_destiny == '仕事運':
                fortune = random.choice([
                    'デスクを窓際に置く',
                    'イエローの小物をデスクに置く',
                    '収納スペースを整理整頓する',
                    'モチベーションを高めるアートを飾る',
                    '快適な椅子を使う',
                    '観葉植物を机の上に置く',
                    'ブラインドを使う',
                    'ウォールボードを置く',
                    '自己啓発本を本棚に置く',
                    'クッションを椅子に置く'
                ])
        
        return fortune
    
    def show_fortune_details(self):
        return render_template("fortune_details.html", selected_layout=self.selected_layout, selected_destiny=self.selected_destiny, fortune_percentage=self.fortune_percentage)
    
    
    
interior_app = InteriorApp()
@app.route('/')
def home():
    return interior_app.start()

@app.route('/select_layout', methods=['POST', 'GET'])
def select_layout():
    if request.method == 'POST':
        selected_layout = request.form.get('layout')
        if selected_layout is not None:
            # レイアウトが選択されたらselect_destiny.htmlにリダイレクト
            return redirect('/select_destiny')
        else:
            return "Error: Layout not selected"
    else:
        return interior_app.select_layout()
    
@app.route('/select_destiny', methods=['POST', 'GET'])
def select_destiny():
    if request.method == 'POST':
        selected_destiny = request.form.get('destiny')
        
        if selected_destiny is not None:
            return interior_app.show_confirmation(selected_destiny)
        else:
            return render_template("select_destiny.html", destinies=interior_app.destinies, selected_layout=interior_app.selected_layout)
    else:
        selected_layout = request.args.get('layout')
        if selected_layout is not None:
            return interior_app.select_destiny()
        else:
            return redirect(url_for('select_layout'))
        
@app.route('/confirmation', methods=['POST', 'GET'])
def confirmation():
    if request.method == 'POST':
        # フォームが送信されたら、draw_fortune()メソッドを呼び出す
        return draw_fortune()
    else:
        # フォームが送信されていない場合は、confirmation.htmlを表示する
        app_instance = InteriorApp()
        return app_instance.confirmation()
    
@app.route('/draw_fortune', methods=['POST'])
def draw_fortune():
    #app_instance = InteriorApp()
    return interior_app.draw_fortune()


print(app.url_map)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8000')