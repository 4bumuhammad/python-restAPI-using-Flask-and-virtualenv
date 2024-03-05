# Python RestAPI using Flask and virtualenv

---

#### Begin Project:

        ❯ virtualenv myenviro

        ❯ pip install virtualenv

        ❯ source myenviro/bin/activate


    # install di dalam environment

        ❯ pip install flask

        ❯ pip install flask-restful
        
        ❯ pip install flask-cors


    # untuk mengecek apa saja yang telah terinstal

        ❯ pip list



#### Menjalankan code :

    ❯  python3 001app.py

        op:

            * Serving Flask app '001app'
            * Debug mode: on
            WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
            * Running on http://127.0.0.1:5005
            Press CTRL+C to quit
            * Restarting with stat
            * Debugger is active!
            * Debugger PIN: 106-564-594
            127.0.0.1 - - [05/Mar/2024 08:22:11] "GET /api HTTP/1.1" 200 -

Buka pada browser 

    URL http://localhost:5005/api

    op:
    {
        "msg": "Hallo dunia, ini app restful."
    }

<p align="center">
    <img src="./gambar-petunjuk/ss_001app.png" alt="ss_001app" style="display: block; margin: 0 auto;">
</p>


---

#### Pada code selanjutnya akan POST data.

- buka postman, buat request POST, dan masukkan key pada multiplatform

    [Body] : form-data
    nama : adim
    umur : 23
    [Send]

    op:
    {
        "msg": "Data berhasil dimasukkan"
    }


- tangkap data hasil GET pada url browser

    http://localhost:5005/api

    op:
    {
        "nama": "admin",
        "umur": "23"
    }

#### atau bisa test tanpa browser menggunakan CURL

    ❯ curl -X POST \
        > -F 'nama=Andrea' \
        > -F 'umur=90' \
        > http://localhost:5005/api
        {
            "msg": "Data berhasil dimasukkan"
        }



    ❯ curl -X GET \
        > -H "Content-Type: application/json" \
        > http://localhost:5005/api
        {
            "nama": "admin",
            "umur": "23"
        }
