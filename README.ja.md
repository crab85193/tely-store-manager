# Tely Store Manager

[![Docker](https://img.shields.io/badge/Docker-24.0.5-1488C6.svg?logo=docker&style=plastic)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11.0-3776AB.svg?logo=python&style=plastic)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/Nginx-1.21%20alpine-269539.svg?logo=nginx&style=plastic)](https://www.nginx.com/)
[![Sentry](https://img.shields.io/badge/-Sentry-FB4226.svg?logo=sentry&style=plastic)](https://sentry.io/welcome/)
[![Deploy](https://github.com/crab85193/tely-store-manager/actions/workflows/deploy.yml/badge.svg)](https://github.com/crab85193/tely-store-manager/actions/workflows/deploy.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

![logo](./docs/img/logo-w.png)

[English README is here](./README.md)

## Description
代理電話予約サービス[Tely](https://github.com/crab85193/Tely)で使用する店舗情報管理プログラム。
Google Place API で取得した店舗情報をデータベースに保管する。

## Requirement
- Ubuntu22.04
- Docker 24.0.5
- Python 3.11.0
- Sentry-sdk 1.39.1
- Google Place API

## Usage
このプログラムを実行するためには、Dockerのインストールと、[Tely](https://github.com/crab85193/Tely)を起動させる必要があります。

`.env.dev`を作成し、以下の内容を記述します。

```
GOOGLE_API_KEY={KEY VALUE}

MYSQL_ROOT_PASSWORD={ROOT PASSWORD}
MYSQL_DATABASE={DATABASE NAME}
MYSQL_USER={USER NAME}
MYSQL_PASSWORD={USER PASSWORD}
MYSQL_HOST={HOST}
MYSQL_PORT={PORT}

IMAGE_SERVER_ADDRESS="127.0.0.1"
IMAGE_SERVER_PROTOCOL="http"

SAVE_IMG_DIR="./static"

SENTRY_DNS={SENTRY DNS ADDRESS}

```

`.env.dev` 作成後、以下のコマンドを実行し、コンテナを起動します。

```
$ docker-compose -f docker-compose.dev.yml up -d --build
```

## Reference

- [Python Documents](https://docs.python.org/3.11/)
- [Google Place API Documents](https://developers.google.com/maps/documentation/places/web-service/overview?hl=ja)
- [Docker Documents](https://docs.docker.com/)

## License
Copyright © 2023 Team Quartetto Inc.

This software is released under the Apache 2.0 License, see [LICENSE](./LICENSE).