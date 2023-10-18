# 仮想通貨のスケジューリング成行注文マニュアル

## プロジェクト概要
このプロジェクトは、Bybitの仮想通貨取引所でスケジューリング成行注文を行うためのものです。AWS LambdaとEventBridgeを使用して、指定された日時に成行注文を自動的に実行します。

## システム構成
- **サーバ**: AWS Lambda (ECRコンテナ [東京リージョン])
- **スケジューリングの仕組み**: EventBridge

## 操作手順

1. **Amazon EventBridgeの設定**:
    - AWS Management Consoleにログインし、EventBridgeのダッシュボードに移動します。
    - 東京リージョンを選択します。
    - 新しいルールを作成し、ルールの名前や説明を入力します。
    - ソースとして`Event Source`を選択し、`Scheduled`を選びます。
    - 任意の日時をCronまたはRate式で設定します。
    - ターゲットとして、`lambda-python-bybit-schedule-order`を選択します。

2. **ペイロードの設定**:
    - ターゲットの詳細設定の中で、`Constant (JSON text)`を選択します。
    - ペイロードには、[BybitのAPIドキュメント](https://bybit-exchange.github.io/docs/v5/order/create-order)で示されている`Request Parameters`に従って、JSON形式のデータを入力します。
    - **ペイロードの例**:
      ```json
      {
          "orderLinkId": "spot-test-postonly",
          "isLeverage": "0",
          "orderType": "Market",
          "symbol": "XRPUSDT",
          "qty": "1",
          "category": "spot",
          "side": "Buy",
          "key": "0",
          "timeInForce": "GTC"
      }
      ```

3. ルールの作成を完了するには、`Create rule`ボタンをクリックします。
