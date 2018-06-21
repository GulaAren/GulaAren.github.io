---
layout: post
title: Membuat Web App dengan Golang + Gin (Bagian 1)
menutitle: Web App = Golang + Gin (bag 1)
---

[Postingan sebelumnnya][lastpost] ditulis sebagai pengenalan [Gin][gin].
Kali ini kita akan mencoba membuat web app dengan Golang dan Gin.

<!--more-->

### Persiapan

Untuk percobaan ini paket yang akan kita gunakan antara lain:

- [github.com/gin-gonic/gin][gin]: Web HTTP framework Golang
- [Bootstrap v4.1][boostrap]: toolkit HTML, CSS, JS
- [Popper.js][popperjs]: Untuk Bootstrap
- [Jquery][jquery]: Untuk Bootsrap

Kita akan menginstall Gin untuk memastikan dapat berjalan baik.
Pertama buat program kode `main.go` seperti berikut.

```go
// main.go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // tunggu dan serve on 0.0.0.0:8080
}
```

Instalasi `Gin` dengan [Dep][dep]. 

```bash
$ # Buat direktori untuk kode kita di $GOPATH/src
$ cd ~/go/src
$ mkdir go_webapp
$ # buat projek baru
$ dep init
$ # tambahkan paket yang diperlukan untuk projek
$ dep ensure
``` 

Untuk klien http, kita bisa gunakan `curl` untuk pengguna commandline (Linux, MacOS), browser dan lain-lain.
Hasil dengan program klien HTTP `curl`:
```bash
$ curl localhost:8080/ping
{"message":"pong"}
```

Hasil di browser :

![Hasil di browser][pingpong]

Log dari program go:
```bash
$ go run main.go

[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:   export GIN_MODE=release
 - using code:  gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /ping                     --> main.main.func1 (3 handlers)
[GIN-debug] Environment variable PORT is undefined. Using port :8080 by default
[GIN-debug] Listening and serving HTTP on :8080
[GIN] 2018/06/02 - 00:00:01 | 200 |     166.529µs |             ::1 |  GET     /ping
```

[boostrap]: https://getbootstrap.com/docs/4.1/getting-started/introduction
[dep]:      https://golang.github.io/dep
[gin]:      https://github.com/gin-gonic/gin
[jquery]:   https://code.jquery.com
[popperjs]: https://popper.js.org

[lastpost]: /blog/golang-web-api-gin
[pingpong]: /assets/imgs/blog/golang-gin-webapp-ping-pong.png

