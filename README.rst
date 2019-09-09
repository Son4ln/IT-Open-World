LittleBlogs
=========

Dự án website diễn đàn công nghệ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Docker local
------------

::
  $ docker-compose -f local.yml build

::
  $ docker-compose -f local.yml up

Truy Cập vào container
::
  $ docker-compose -f local.yml run --rm app-name sh

Docker production
------------
::
  $ docker-compose -f production.yml build
::
  $ docker-compose -f production.yml up

Truy Cập vào container
^^^^^^^^^^^^^^^^^^^^^^

::
  $ docker-compose -f production.yml run --rm app-name sh

Docker clean all
------------

::
  $ docker system prune -a
  $ docker system prune --volumes -a
  $ docker container rm -f $(docker container ls -aq -a)
  $ docker image prune -a
  $ docker network prune

MinIo
------------
Using MinIo instead of AWS ...

https://min.io/
https://docs.min.io/docs/python-client-quickstart-guide.html
https://hub.docker.com/r/minio/minio/


Truy cập vào OwnCloud
------------

::
  $ docker-compose -f local.yml run --rm minio sh

Có thể backup lại dữ liệu nếu cần thiết

Port List
------------


Django
^^^^^^

http://localhost:8000

MinIo
^^^^^^^^
nếu minio gặp lỗi khi build. Xóa file data/.minio.sys/format.json và build lại
http://localhost:9001
ID và PASS trong evironment của local.yml/production.yml

Reactjs
^^^^^^^

http://localhost:3000

NodeServer
^^^^^^^^^^

http://localhost:3001

Laravel
^^^^^^^

http://localhost:8081
