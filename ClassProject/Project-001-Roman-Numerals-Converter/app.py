from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''

    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) 
        decimal_num %= i
    return num_to_roman


@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':  #bu number sayısını çek 
        alpha = request.form['number']
        if not alpha.isdecimal(): #bu sayı desimal değilse (negatif, float) index html kirala ve hata verdir(not valid=True) 
            return render_template('index.html', developer_name='Osman', not_valid=True)
        number = int(alpha)
        if not 0 < number < 4000: #sayı bu aralıkta değilse index.html kirala yine hata mesajı verdir.
            return render_template('index.html', developer_name='Osman', not_valid=True)
        return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Osman')
    #eğer üstteki iki koşulda geçerli değilse demekki sonuç doğru result.html kirala
    #number decimal = kutucuktan çekilen sayı sonra alpha ya atanan sayı (18.satır)
    # numberroman = convert fonk.girecek olan sayı(5.satır)number_roman = convert(number)
    else:  # post değilse yani get ise ana sayfayı karşımıza çıkaracak index.html den. notvalid false olduğu için alttaki hata çıkmıyor.
        return render_template('index.html', developer_name='Osman', not_valid=False)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
