### Một số những switch trong sqlmap

**output verbose**: trình bày chi tiết output(debug, gồm level 0->6), recommend sử dụng level 2 (-v 2 hoặc -vv)

**lựa chọn target:** 

- -d: sử dụng trực tiếp cho database 

- -u (hoặc--url), sử dụng để target trực tiếp url
  
  ```
  $ sqlmap -u "http://www.target.com/vuln.php?id=1" -f --banner --dbs
  ```

- -r: lấy request từ một file, có thể copy trực tiếp request từ các công cụ khác (burpsuite, ...), bằng cách này có thể không cần cấu hình những lựa chọn khác (cookie, post data, ...)
  
  ```
  $ sqlmap -r req.txt --dbs
  ```
  
  **các lựa chọn request**

- --method (ví dụ: --method=PUT)

- --data: truyền post data mẫu vào script, đồng thời sử dụng method POST 
  
  ```
  $ sqlmap -u "http://www.target.com/vuln.php" --data="id=1" -f --banner --dbs --users
  ```

- --cookie: truyền cookie vào script

- --cookie-del: sử dụng nếu không sử dụng `;` để phân tách cookie

- --drop-set-cookie: sqlmap will ignore any coming Set-Cookie header

- nếu --level >= 2, cookie header cũng sẽ được đưa vào script để inject 

- mặc định, User-agent sẽ là sqlmap/1.0-dev-xxxxxxx (http://sqlmap.org) nếu không set  --user-agent switch, ngoài ra sử dụng --random-agent sẽ lấy một user angent ngẫu nhiên trong ./txt/user-agents.txt. nếu --level >= 3, header User-agent sẽ được test

- --host

- --referer 

- --header: bổ sung thêm header, mỗi header cách nhau bởi \n 
  
  ```
  $ sqlmap -u "http://192.168.21.128/sqlmap/mysql/get_int.php?id=1" -z "ign,flu,bat,tec=E" --headers="Host:www.target.com\nUser-agent:Firefox 1.0" -v 5
  ```

- --auth-type và --auth-cred: cung cấp authentication, auth-type (Basic, Digest, NTLM) và auth-cred(username:password)
  
  ```
  $ sqlmap -u "http://192.168.136.131/sqlmap/mysql/basic/get_int.php?id=1" --auth-type Basic --auth-cred "testuser:testpass"
  ```

- --auth-file: cung cấp key PEM format

- --ignore-code: sử dụng khi server trả về status lỗi và sẽ skip những response này

- --delay: delay giữa những request được gửi

- --timeout: sử dụng để cấu hình lại timeout, mặc định là 30s

- --retries: cấu hình lại số lần thử nếu timeout

- để tránh session hiện tại đang sử dụng bị hủy do sqlmap gửi quá nhiều request không hợp lệ, có thể sử dụng các option: --safe-url, --safe-post, --safe-req và --safe-freq để visit một url hợp lệ khác trong quá trình chạy script

- --skip-urlencode: mặc định payload sẽ được url-encode, nếu có switch này thì payload sẽ không được encode

**Bypass CSRF**

- mặc định, sqlmap tự động nhận diện và bypass CSRF. trong trường hợp service không cấu hình csrf như thông thường, switch --csrf-token sẽ có thể xác định lại tên.
- --csrf-url: lấy csrf token từ url được chỉ định

**eval**

- --eval: sử dụng python trong script:
  
  ```
  $ sqlmap -u "http://www.target.com/vuln.php?id=1&hash=c4ca4238a0b9238
  20dcc509a6f75849b" --eval="import hashlib;hash=hashlib.md5(id).hexdigest()"
  ```

**injection**

- -p: lựa chọn param để tấn công, ví dụ `-p "id,user-agent"`
- --skip: loại bỏ param trong quá trình tấn công, thường hay đi cùng với switch --level

**DBMS**

- --dbms
- --os

**Custom injection payload**

- --prefix and --suffix. example:
  
  ```php
  $query = "SELECT * FROM users WHERE id=('" . $_GET['id'] . "') LIMIT 0, 1";
  ```
  
  ```
  $ sqlmap -u "http://192.168.136.131/sqlmap/mysql/get_str_brackets.php?id=1" -p id --prefix "')" --suffix "AND ('abc'='abc"
  ```
  
  ```
  $query = "SELECT * FROM users WHERE id=('1') payload-here AND ('abc'='abc') LIMIT 0, 1";
  ```

**Tamper injection data**
format của một tamper script như sau:

```py
# Needed imports
from lib.core.enums import PRIORITY

# Define which is the order of application of tamper scripts against
# the payload
__priority__ = PRIORITY.NORMAL

def tamper(payload):
    '''
    Description of your tamper script
    '''

    retVal = payload

    # your code to tamper the original payload

    # return the tampered payload
    return retVal
```

ví dụ sử dụng:

```
$ sqlmap -u "http://192.168.136.131/sqlmap/mysql/get_int.php?id=1" --tamper tamper/between.py,tamper/randomcase.py,tamper/space2comment.py -v 3
```

**Detection**

- --level: gồm 5 level. mặc định, tất cả injection point trong GET và POST đều được tấn công. với level 2, header cookie sẽ được đưa vào danh sách. với level 3, header referer và header user-agent sẽ được thêm
- -- risk: gồm 3 level
  sqlmap sử dụng so sánh nội dung trang để xác định truy vấn True hay False trong boolean-based blind SQLi. Tuy nhiên, nếu trang có nội dung động thay đổi theo thời gian, có thể cần tùy chỉnh phương pháp so sánh.
- --string: Xác định một chuỗi luôn xuất hiện trên trang True, nhưng không có trên trang False.
- --not-string: Xác định một chuỗi chỉ xuất hiện trên trang False.
- --regexp: Dùng biểu thức chính quy để so sánh thay vì chuỗi cố định.
- --code: So sánh dựa trên HTTP status code (VD: 200 cho True, 401 cho False).
- --titles: So sánh dựa trên tiêu đề trang (VD: "Welcome" cho True, "Forbidden" cho False).
- --text-only: Bỏ qua nội dung động (script, quảng cáo, v.v.), chỉ so sánh nội dung văn bản.

**Kĩ thuật tấn công**

switch: --technique. mặc định, sqlmap thử tất cả các phương pháp tấn công sql injection, nhưng ta có thể chỉ định loại tấn công như sau:
B: Boolean-based blind
E: Error-based
U: Union query-based
S: Stacked queries
T: Time-based blind
Q: Inline queries

- --time-sec: set thời gian cho các kĩ thuật time-based, mặc định là 5s
- --union-cols: số cột trong bảng đã biết. mặc định sqlmap sẽ thử từ 1-10 cột. ví dụ: `-union-cols 2-16`
- second order attack: --second-url and --second-req
- sqlmap tự động nhận diện DBMS. Nếu muốn nhận diện chi tiết hơn, sử dụng--fingerprint: Xác định chính xác phiên bản DBMS, hệ điều hành, kiến trúc và bản vá thông qua nhiều kỹ thuật (SQL dialects, lỗi inband, v.v.). --banner: Kết hợp với --fingerprint để có kết quả chính xác hơn.

**Enumeration**

- --all

- -b (--banner): trả về version hệ thống

- --current-user: trả về username và host

- --current-db: trả về tên của database

- --hostname

- --is-dba

- --dbs: enum list các database

- --tables: enum các tables cùng với database tương ứng

- --columns: enum các column cùng với table và database tương ứng

- -D -T -C : chỉ định cụ thể db, table hoặc column
  
  ```
  $ sqlmap -r req.txt --columns -T users
  ```

- --dump: dump toàn bộ data

**Khác**

- --batch: tự động quá trình chạy script, không cần tương tác người dùng
- --crawl: crawl service 
- --crawl-exclude
- --beep: make a sound
