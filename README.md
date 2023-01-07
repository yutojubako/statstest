# statstest
3群以上で対応のない独立なデータ群の検定のためには、

3群以上で対応のない(独立な)データ

　　　　↓
    
正規性の検定(Shapiro-Wilk検定、もしくはQQプロットでも..)　　→ Non-paraへ

　　　　↓
    
等分散性の検定(Bartlett検定)　　　　　　　　　　　　　　　　 → Non-paraへ

　　　　↓
    
一元配置分散分析(ANOVA)　　　 　　　　　　　　　　　　　 → Non-paraへ

　　　　↓
    
Tukey_HSD検定、Scheffe検定、Tukey検定(各群のnが同じ)、Dunnett検定(Control群との比較)

上のフローチャートでNon-parametricの場合

　　　　↓
    
等分散性の検定(Levene検定、Fligner検定)

　　　　↓
    
一元配置分散分析(Kruskal-Wallis検定)

　　　　↓
    
Steel-Dwass-Critchlow-Fligner(dscf)検定、Conover Iman検定

# References
統計検定を理解せずに使っている人のために 
Ⅰ　https://www.jstage.jst.go.jp/article/kagakutoseibutsu/51/5/51_318/_pdf
Ⅱ　https://www.jstage.jst.go.jp/article/kagakutoseibutsu/51/6/51_408/_pdf
Ⅲ https://www.jstage.jst.go.jp/article/kagakutoseibutsu/51/7/51_483/_pdf
https://qiita.com/rola_satoru/items/af2bcad7826672891f80
