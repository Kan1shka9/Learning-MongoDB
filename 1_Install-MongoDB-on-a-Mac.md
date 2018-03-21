#### 1. Install MongoDB on a Mac

- [`MongoDB Download Center`](https://www.mongodb.com/download-center#community)

```sh
☁  ~  cd Downloads
☁  Downloads  tar xvzf mongodb-osx-ssl-x86_64-3.6.3.tgz
x mongodb-osx-x86_64-3.6.3/README
x mongodb-osx-x86_64-3.6.3/THIRD-PARTY-NOTICES
x mongodb-osx-x86_64-3.6.3/MPL-2
x mongodb-osx-x86_64-3.6.3/GNU-AGPL-3.0
x mongodb-osx-x86_64-3.6.3/bin/mongodump
x mongodb-osx-x86_64-3.6.3/bin/mongorestore
x mongodb-osx-x86_64-3.6.3/bin/mongoexport
x mongodb-osx-x86_64-3.6.3/bin/mongoimport
x mongodb-osx-x86_64-3.6.3/bin/mongostat
x mongodb-osx-x86_64-3.6.3/bin/mongotop
x mongodb-osx-x86_64-3.6.3/bin/bsondump
x mongodb-osx-x86_64-3.6.3/bin/mongofiles
x mongodb-osx-x86_64-3.6.3/bin/mongoreplay
x mongodb-osx-x86_64-3.6.3/bin/mongoperf
x mongodb-osx-x86_64-3.6.3/bin/mongod
x mongodb-osx-x86_64-3.6.3/bin/mongos
x mongodb-osx-x86_64-3.6.3/bin/mongo
x mongodb-osx-x86_64-3.6.3/bin/install_compass
☁  Downloads  cd mongodb-osx-x86_64-3.6.3
☁  mongodb-osx-x86_64-3.6.3  ll
total 232
-rw-r--r--@  1 kanishka  staff    34K Feb 22 11:37 GNU-AGPL-3.0
-rw-r--r--@  1 kanishka  staff    16K Feb 22 11:37 MPL-2
-rw-r--r--@  1 kanishka  staff   2.1K Feb 22 11:37 README
-rw-r--r--@  1 kanishka  staff    56K Feb 22 11:37 THIRD-PARTY-NOTICES
drwxr-xr-x  16 kanishka  staff   512B Mar 20 11:53 bin
☁  mongodb-osx-x86_64-3.6.3  cd bin
☁  bin  ll
total 561776
-rwxr-xr-x@ 1 kanishka  staff    10M Feb 22 11:37 bsondump
-rwxr-xr-x@ 1 kanishka  staff   5.7K Feb 22 12:03 install_compass
-rwxr-xr-x@ 1 kanishka  staff    31M Feb 22 12:01 mongo
-rwxr-xr-x@ 1 kanishka  staff    55M Feb 22 12:00 mongod
-rwxr-xr-x@ 1 kanishka  staff    13M Feb 22 11:38 mongodump
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongoexport
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongofiles
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongoimport
-rwxr-xr-x@ 1 kanishka  staff    54M Feb 22 12:00 mongoperf
-rwxr-xr-x@ 1 kanishka  staff    14M Feb 22 11:39 mongoreplay
-rwxr-xr-x@ 1 kanishka  staff    14M Feb 22 11:38 mongorestore
-rwxr-xr-x@ 1 kanishka  staff    30M Feb 22 11:50 mongos
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongostat
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:39 mongotop
☁  bin  sudo bash
Password:
bash-3.2# mkdir -p /data/db
bash-3.2# chmod 777 /data/db/
bash-3.2# ls -ld /data/db/
drwxrwxrwx  2 root  wheel  64 Mar 20 11:55 /data/db/
bash-3.2# exit
exit
☁  bin  whoami
kanishka
☁  bin 
```

```sh
☁  bin  ll
total 561776
-rwxr-xr-x@ 1 kanishka  staff    10M Feb 22 11:37 bsondump
-rwxr-xr-x@ 1 kanishka  staff   5.7K Feb 22 12:03 install_compass
-rwxr-xr-x@ 1 kanishka  staff    31M Feb 22 12:01 mongo
-rwxr-xr-x@ 1 kanishka  staff    55M Feb 22 12:00 mongod
-rwxr-xr-x@ 1 kanishka  staff    13M Feb 22 11:38 mongodump
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongoexport
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongofiles
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongoimport
-rwxr-xr-x@ 1 kanishka  staff    54M Feb 22 12:00 mongoperf
-rwxr-xr-x@ 1 kanishka  staff    14M Feb 22 11:39 mongoreplay
-rwxr-xr-x@ 1 kanishka  staff    14M Feb 22 11:38 mongorestore
-rwxr-xr-x@ 1 kanishka  staff    30M Feb 22 11:50 mongos
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:38 mongostat
-rwxr-xr-x@ 1 kanishka  staff    11M Feb 22 11:39 mongotop
☁  bin  sudo cp * /usr/local/bin
Password:
☁  bin  which mongo
/usr/local/bin/mongo
☁  bin
```

```sh
☁  ~  pgrep mongo
9474
☁  ~  kill 9474
☁  ~
```

```sh
☁  ~  mongod
2018-03-21T10:34:46.151-0700 I CONTROL  [initandlisten] MongoDB starting : pid=13833 port=27017 dbpath=/data/db 64-bit host=Miyahs-Air.ddnszone.calstatela.edu
2018-03-21T10:34:46.151-0700 I CONTROL  [initandlisten] db version v3.6.3
2018-03-21T10:34:46.151-0700 I CONTROL  [initandlisten] git version: 9586e557d54ef70f9ca4b43c26892cd55257e1a5
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 0.9.8zh 14 Jan 2016
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten] allocator: system
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten] modules: none
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten] build environment:
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten]     distarch: x86_64
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten]     target_arch: x86_64
2018-03-21T10:34:46.152-0700 I CONTROL  [initandlisten] options: {}
2018-03-21T10:34:46.153-0700 I -        [initandlisten] Detected data files in /data/db created by the 'wiredTiger' storage engine, so setting the active storage engine to 'wiredTiger'.
2018-03-21T10:34:46.153-0700 I STORAGE  [initandlisten] wiredtiger_open config: create,cache_size=3584M,session_max=20000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000),statistics_log=(wait=0),verbose=(recovery_progress),
2018-03-21T10:34:46.853-0700 I STORAGE  [initandlisten] WiredTiger message [1521653686:853971][13833:0x7fff99fb4340], txn-recover: Main recovery loop: starting at 2/102656
2018-03-21T10:34:46.956-0700 I STORAGE  [initandlisten] WiredTiger message [1521653686:956981][13833:0x7fff99fb4340], txn-recover: Recovering log 2 through 3
2018-03-21T10:34:47.024-0700 I STORAGE  [initandlisten] WiredTiger message [1521653687:23976][13833:0x7fff99fb4340], txn-recover: Recovering log 3 through 3
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten]
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten]
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-03-21T10:34:47.163-0700 I CONTROL  [initandlisten]
2018-03-21T10:34:47.177-0700 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
2018-03-21T10:34:47.178-0700 I NETWORK  [initandlisten] waiting for connections on port 27017
```

```sh
☁  ~  mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
Server has startup warnings:
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten]
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten]
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2018-03-21T10:35:42.207-0700 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2018-03-21T10:35:42.208-0700 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2018-03-21T10:35:42.208-0700 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2018-03-21T10:35:42.208-0700 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2018-03-21T10:35:42.208-0700 I CONTROL  [initandlisten]
> db
test
> db.names.insert({'name':'kan1shka9'});
WriteResult({ "nInserted" : 1 })
> db.names.find()
{ "_id" : ObjectId("5ab29815baba79c8681a8ee9"), "name" : "kan1shka9" }
>
```