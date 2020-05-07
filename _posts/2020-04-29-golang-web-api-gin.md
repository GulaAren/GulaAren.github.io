---
layout: post
title: "Pengenalan Golang + Gin: Membuat Web API Sederhana"
menutitle: Pengenalan Golang + Gin
labels:
 - Golang
 - RestAPI
categories:
 - Golang
---

[Gin](https://github.com/gin-gonic/gin) merupakan web framework yang dibuat dengan bahasa pemograman sedang hot yaitu Go (Golang).
Gin memiliki performa yang cepat (_doc: [gin benchmark](https://github.com/gin-gonic/gin#benchmarks)_).

Kali ini kita akan menginstal dan membuat web API sederhana untuk pengenalan Gin.

<!--more-->

### Persiapan

Instalasi library untuk kode menggunakan [`dep`](https://golang.github.io/dep/).
Pertama kita siapkan folder kode yang berada di dalam direktori `$GOPATH/src`. Jika Golang sudah terinstall, folder `$GOPATH` dapat dilihat di commandline dengan perintah `echo $GOPATH`.

```bash
$ echo $GOPATH
/home/ubuntu/go
$ cd go
$ ls
bin  pkg  src
```

Lalu buat direktori untuk kode kita.

```bash
$ cd src
$ mkdir coba-webapi
$ cd coba-webapi
```

### Install `dep`

> Untuk menggunakan manejemen library lain dapat dilihat di [gin#start-using-it](https://github.com/gin-gonic/gin#start-using-it)


`dep` merupakan salah satu program untuk manejemen perlengkapan/keperluan library/paket untuk Golang.
Mirip `Rubygems` untuk Ruby atau `npm` untuk Nodejs.

Instalasinya
```bash
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
```

### Mulai Kode

Sekarang kita mulai menulis kode dengan nama file `main.go`.

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()

    // path: "/"
    r.GET("/", func(c *gin.Context) {
        c.JSON(200, gin.H { "pesan": "hello world" })
    })

    r.Run(":8080")
}
```

### Install Library

```bash
# Mulai 
$ dep init
$ ls
Gopkg.lock  Gopkg.toml  main.go  vendor
# Install library
$ dep ensure
```

Library yang dibutuhkan kode kita akan disimpan di folder `vendor`.


### Percobaan Awal

```bash
$ go run main.go
[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:   export GIN_MODE=release
 - using code:  gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /                         --> main.main.func1 (3 handlers)
[GIN-debug] Listening and serving HTTP on :8080
[GIN] 2018/05/29 - 02:43:25 | 200 |     150.963µs |             ::1 |  GET     /
```

Hasil
```bash
$ curl -i localhost:8080
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 28 May 2018 19:43:25 GMT
Content-Length: 25

{"pesan":"hello world"}
```

### Web API Sederhana

##### URL: `/get` 

_Catatan_: Kode ini kita tambahkan sebelum baris `r.Run(":8080")`
```go
    ...

    // "/get"
    r.GET("/get", func(c *gin.Context) {
        // nilai default `nama` := testuser
        nama  := c.DefaultQuery("nama", "testuser")
        // pesan diambil dari argumen url
        pesan := c.Query("pesan")

        c.JSON(200, gin.H {
            "nama": nama,
            "pesan": pesan,
        })
    })
    ...
```

Hasil
```bash
$ curl -i "localhost:8080/get?nama=testnama&pesan=yo+"
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 28 May 2018 20:51:57 GMT
Content-Length: 33

{"nama":"testnama","pesan":"yo "}
```

##### URL: `/get` 

_Catatan_: Kode ini kita tambahkan sebelum baris `r.Run(":8080")`

```go
    // url: /post
    r.POST("/post", func(c *gin.Context) {
        pesan := c.PostForm("pesan")
        user  := c.DefaultPostForm("nama", "tamu")

        c.JSON(200, gin.H {
            "status": "data diterima",
            "user"  : user,
            "pesan" : pesan,
        })
    })

    r.Run(":8080")
```

Hasil
```bash
$ curl -i -X POST  "localhost:8080/post?nama=testnama&pesan=pesan+dari+testnama"
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Date: Mon, 28 May 2018 21:01:13 GMT
Content-Length: 51

{"pesan":"","status":"data diterima","user":"tamu"}
```

### Kesimpulan

Dari percobaan yang sudah dilakukan, kita sudah dapat menangani metode protokol HTTP seperti `GET` dan `POST` dan argumennya.
Gin merupakan web framework yang handal untuk bahasa pemograman yang handal pula yaitu Golang.
Banyak hal yang dapat dilakukan untuk kode web api.
Berikut info selengkapnya mengenai Gin.

### Info

- [Dokumentasi Gin](https://gin-gonic.github.io/gin/)
- [Gin _di_ godoc.org](https://godoc.org/github.com/gin-gonic/gin)
- [Gin _di_ github](https://github.com/gin-gonic/gin)
