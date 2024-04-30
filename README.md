# Mitarashi@PSO2NGS_JP
[![](https://img.shields.io/badge/python->=3.6-informational?style=for-the-badge&logo=python&logoColor=1da1f2)](https://www.python.org/)
[![](https://img.shields.io/badge/Twitter-@PSO2NGS_JP-blue?style=for-the-badge&logo=twitter)](https://twitter.com/PSO2NGS_JP)
[![](https://img.shields.io/badge/(C)SEGA-PHANTASY_STAR_ONLINE_2-lightgray?style=for-the-badge)](https://pso2.jp/)  
🍡 [PSO2NGS 15分前緊急予告BOT - JP](https://twitter.com/PSO2NGS_JP) のソースコードを公開用に簡略化したものです。  
```
$ pip install pyautogui opencv-python
```

## ⚙ 技術情報
スクリーンショットした結果を元に緊急クエスト/ステージライブが発生しているかを確かめます。  

## 💻 動作情報
以下の環境で運用していました。
- Microsoft Windows 10, version 22H2
- Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz
- NVIDIA GeForce GTX 770
- 16.0 GB DDR3

Minecraftのサーバーホストを兼ねられる程度には動いていました。  
ご参考までに。

## ❓ Q&A
#### ランニングコストはどのくらい？（追記・変更済み 24/04/03）  
[電力計](https://amzn.asia/d/gflqF3L)が届いたので1時間ほど実測してみました。  
設定は実際に使用していた際と同じで以下となります。  

- 電源プラン: バランス  
- 電源管理モード\[NVIDIAコンパネ\]: 最適電力
- 解像度: 1920x1080（発生緊急の識別にはある程度の解像度が必要なため）
- NGS設定: 最低（30FPS）
- モニター: なし（操作が必要な場面ではリモートデスクトップを使用します）

基本的に90W~92Wで安定、天候が雨や雷雨時（ゲーム内）に120W越えでした。  

- 消費電力: 90W  
- 電気料金の目安単価: 31円/kWh  
- 年間合計観測時間: 8448時間（最小水曜日, 定期メンテ6時間固定）  

この条件の場合、最低でも年間23,570円掛かるようです。  

それまでの使用電力量によって1kWhあたりの単価が変わったり、天候が雨や雷雨時（ゲーム内）に消費電力が増加したりと、  
変動する値が存在するため、概算は出来てもより具体的な金額は不明です。  
 ![ScreenShot](https://github.com/pso2ngs-unofficial/pso2ngs-jp/assets/61118664/672caf63-298e-46a5-ad4e-ddd00a8bf009)  
 
なお、アカウントが存在するX（Twitter）, Mastodon, Bluesky, Discordこれらのサービスにおいて、24年3月時点ではAPIのレート制限に引っかかる事はないため、サービス継続のための課金などは不要でした。  

TwitterAPIが有料化するということでbotの終了を宣言したこともありましたが、新APIの無料プラン発表前の宣言であったためTwitterに課金した事実はありません。  

#### 実際の運営支援について
運用中にはAmazonの欲しいものリスト経由で運営支援を頂いておりました。  
ギフトメッセージ（納品書）は手元に残しており、それらで確認できる範囲での運営支援概算は以下となりました。  
総ギフト人数: 2人  
総ギフト金額: 約11,400円  
最終ギフト日: 2023/07/06  

#### 今後について（追記 24/04/03）  
休止及びサービス再開する可能性があるとは言っているものの、このリポジトリを公開することからしても、現状では自身による今後のサービス再開は一切考えていないため、終了と考えていただいて問題ないです。  

発生している緊急の内容までわかる特徴を持った通知botであるこのサービスは、NGSに熱中している時に個人的に欲しかったから作ったものであり、一般公開しても追加のコストが掛からないから続けていただけで、自分が使わなくなった上で運営支援もない現状にて続けていく事は予算が無いので厳しいです。  

botの存在自体に賛否両論あったみたいですが、一度でも使っていただけたなら、少しでも多くの人に使って貰えたのなら光栄です。  
