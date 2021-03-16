# MakeLeaps_API_df（サンプル）

MakeLeapsのAPIから、clientとdocumentとdocument_lineitemをdfとして取得し、csvへ保存。
{Client Id}, {Client Secret}, {MakeLeaps_ID}はそれぞれ独自のものを入れる必要あり。
以下の画面から取得可能。
<img width="748" alt="image" src="https://user-images.githubusercontent.com/13245856/111249605-4ef2b780-864f-11eb-8dc3-536ac3d461b7.png">

１回のリクエストで20データしかダウンロードしないため、データ量に応じて、完了までに時間がかかる。（15,000レコードの書類をダウンロードするのに10分程度）
pageアクセスごとにコンソールへ状況を出力。

<img width="571" alt="image" src="https://user-images.githubusercontent.com/13245856/111249914-caecff80-864f-11eb-9b66-466ca78c89dd.png">

