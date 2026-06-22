# Docker Compose for LoongArch64

<p align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></p>

<p align="center"><img src="https://img.shields.io/badge/Docker%20Compose%20LoongArch64%20%E9%BE%99%E8%8A%AF%E6%9E%B6%E6%9E%84%E5%8F%91%E8%A1%8C%E7%89%88-blue?logo=docker&logoColor=white" alt="Docker Compose LoongArch64 龙芯架构发行版"></p>

通过 CI/CD 为 **LoongArch64 (loong64)** 架构构建 [Docker Compose](https://github.com/docker/compose) 二进制文件。

## 工作原理

GitHub Actions 工作流克隆指定版本的 docker/compose，在 Debian 13 容器中使用
`GOOS=linux GOARCH=loong64` 交叉编译，将 `docker-compose` 构建到 `bin/build/` 目录。
目标平台：`linux/loong64`。

关于为何选择 Debian 13 容器，请参见 [Discussion #6 — Why Use container: debian:13?](https://github.com/orgs/kubernetes-loong64/discussions/6)。

## 分支命名

推送名为 `loong64-v<version>`（例如 `loong64-v5.1.4`）的分支以触发构建。
附加 `+<build>`（例如 `loong64-v5.1.4+0`）以包含构建元数据。

## [发布](https://github.com/kubernetes-loong64/compose-loong64/releases)

推送与 `release-loong64-v<version>` 匹配的标签（例如 `release-loong64-v5.1.4+0`）
即可发布包含构建好的二进制文件的 GitHub Release。

`+<build>` 后缀提供构建元数据（例如 `+0`、`+1-alpha.1`）。

构建元数据中的后缀表示发布阶段：

| 后缀      | 阶段   |
|---------|------|
| `alpha` | 内部测试 |
| `beta`  | 公开测试 |
| `rc`    | 预发布  |
| （无）     | 稳定版  |

## 发布制品

每个发布包含以下文件：

| 文件                                                         | 描述                       |
|------------------------------------------------------------|--------------------------|
| `docker-compose`                                           | 独立二进制文件（linux/loong64）   |
| `docker-compose-plugin-x.y.z.an23.loongarch64.rpm`         | Anolis OS 23 的 RPM 包     |
| `docker-compose-plugin_x.y.z.debian.13.trixie_loong64.deb` | Debian 13（Trixie）的 DEB 包 |

## 验证发布

- 发布文件使用 GPG 签名。
- 从 [keys.openpgp.org](https://keys.openpgp.org) 下载公钥。
- 指纹：[FCF8724722CCBF9F51B1FBE376532BE7E3013105](https://keys.openpgp.org/debug?q=FCF8724722CCBF9F51B1FBE376532BE7E3013105)
- [手动下载](https://keys.openpgp.org/vks/v1/by-fingerprint/FCF8724722CCBF9F51B1FBE376532BE7E3013105)

```shell
gpg --keyserver keys.openpgp.org --recv-keys FCF8724722CCBF9F51B1FBE376532BE7E3013105
echo "FCF8724722CCBF9F51B1FBE376532BE7E3013105:6:" | gpg --import-ownertrust
```

或者，手动下载公钥文件后导入：

```shell
gpg --import /tmp/xxx
```

## 许可证

[Apache License 2.0](LICENSE)
