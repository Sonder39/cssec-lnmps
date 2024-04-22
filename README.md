# Reference

- **[base_web_nginx_mysql_php_74](https://github.com/ctfhub-team/base_web_nginx_mysql_php_73)**


# Base Image LNMPS

- L: Linux alpine
- N: Nginx
- M: MySQL
- P: PHP 7.3
- S: SSH
- PHP MySQL Ext
    + mysql
    + mysqli

## Usage

### ENV

- ROOT_PASSWORD=root
- AWD_PASSWORD=awd
- FLAG=cssec{nginx_mysql_ssh_php_73}
- FLAG_TABLE=flagtable
- FLAG_COLUMN=flagcolumn

### Files

- src 网站源码
    + db.sql 数据库文件
    + index.php
    + ...etc
- Dockerfile
- docker-compose.yml 可选

### Dockerfile

```
FROM sonder39/cssec-lnmps

COPY src /var/www/html

# 自定义 flag 方式
# COPY run.sh /run.sh
```

