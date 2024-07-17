def make_en(pi = 3.14):
    '''円の面積を計算する関数を作る'''

    def circle_kei(radius):
        '''円の面積を計算する'''

        return radius * radius * pi

    return circle_kei

# piが初期設定(3.14)のとき
circle_kei_a = make_en()
#piが3.1415926535のとき
circle_kei_b = make_en(pi = 3.1415926535)
