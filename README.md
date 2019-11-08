# SAM Template

SAMアプリケーションのテンプレート

## 構成

```bash
.
├── README.md                   <-- このファイル
├── template.yaml               <-- SAM Template
├── doc                         <-- ドキュメント置き場
├── events                      <-- テスト用イベントメッセージ
│   └── service                 <-- サービス層
├── hello                       <-- Lambda Function のソースコード
│   ├── __init__.py
│   ├── app.py                  <-- Lambda Handlerのコード
│   ├── requirements.txt        <-- build時に追加インストールするパッケージリスト
│   └── service                 <-- サービス層
│       ├── __init__.py
│       └── hello.py            <-- Greetingクラスのコード
└── tests                       <-- ユニットテスト
    ├── conftest.py             <-- ユニットテストの初期化ファイル
    └── hello
        └── service             <-- サービス層のテスト
            ├── __init__.py
            └── test_hello.py   <-- Greetingクラスのテストコード
```

## Requirements

* AWS CLI already configured with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)


sam package --template-file template.yaml  --output-template-file packaged.yaml --s3-bucket biglobe-isp-private-data-bucket
sam deploy --template-file packaged.yaml --stack-name AccountManager --capabilities CAPABILITY_IAM

## ローカル実行

* ローカル実行は、Dockerコンテナ上でLambda実行環境のイメージを使って実行する
* AWS上のサービスには、template.yamlで定義されたポリシーではなく、~/.aws/ の認証情報のユーザ又はロールのポリシーでアクセスする（実際にデプロイするとエラーになることも）

```bash
sam build
sam local invoke HelloWorldFunction --event event.json
```

## プロジェクトのビルド

[AWS Lambda requires a flat folder](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) with the application as well as its dependencies in deployment package. When you make changes to your source code or dependency manifest,
run the following command to build your project local testing and deployment:

```bash
sam build
```

If your dependencies contain native modules that need to be compiled specifically for the operating system running on AWS Lambda, use this command to build inside a Lambda-like Docker container instead:
```bash
sam build --use-container
```

By default, this command writes built artifacts to `.aws-sam/build` folder.


## パッケージ化とデプロイ


Firstly, we need a `S3 bucket` where we can upload our Lambda functions packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Next, run the following command to package our Lambda function to S3:

```bash
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name user_man \
    --capabilities CAPABILITY_IAM
```

## 参考

[Serverless Application Model (SAM) HOWTO Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html)

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name user_man \
    --query 'Stacks[].Outputs[?OutputKey==`HelloWorldApi`]' \
    --output table
``` 


## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called sam logs. sam logs lets you fetch logs generated by your Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
sam logs -n HelloWorldFunction --stack-name user_man --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Testing


Next, we install test dependencies and we run `pytest` against our `tests` folder to run our initial unit tests:

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

## Cleanup

In order to delete our Serverless Application recently deployed you can use the following AWS CLI Command:

```bash
aws cloudformation delete-stack --stack-name user_man
```