## Sử dụng burpsuite cơ bản và các kĩ thuật liên quan

### Burpsuite là gì?

Burpsuite là một công cụ phổ biến trong kiểm thử xâm nhập. Công cụ này có thể sử dụng để tìm kiếm các lỗ hổng bảo mật khác nhau như SQL Injection, XSS thông qua quá trình sử dụng GUI như người dùng bình thường. Điều quan trọng ở đây là nó hoạt động như một proxy, nghĩa là nó nằm giữa web server và browser của người sử dụng để bắt các request. Từ đó ta có thể chỉnh sửa và nghiên cứu các request này để thực hiện khai thác.

![All you need to know about BurpSuite](https://cdn.prod.website-files.com/62efedb360a7998b0e43cb84/6321a0f076706854ff591093_All%20about%20BurpSuite.jpg)

Burpsuite có nhiều feature khác nhau: proxy, Repeater, intruder, scanner, ... Ta sẽ đi tìm hiểu chúng với góc nhìn của một người mới bắt đầu tìm hiểu.

### Interception Proxy

Đây là tính năng chính của Burp Suite, cho phép Burp đóng vai trò như một trung gian giữa client (trình duyệt web) và server của ứng dụng. Khi đứng giữa hai thành phần này, Burp có thể chặn toàn bộ các request/response được trao đổi. Điều này giúp pentester có thể phân tích chi tiết từng request và tùy ý chỉnh sửa chúng.

Cơ chế hoạt động của Proxy là chặn từng request một, sau đó để pentester quyết định có cho phép request đi tiếp hay không. Trước khi forward request, pentester hoàn toàn có thể chỉnh sửa nội dung rồi mới gửi lên server.

Ngoài ra, Proxy còn cho phép quan sát lịch sử các request/response trực tiếp mà không cần gửi thủ công lại lên server. Thực tế, đây chính là chế độ được sử dụng nhiều nhất của Proxy.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-34-41-image.png)

Tại đây sẽ hiển thị toàn bộ các request đã được gửi tới domain, ví dụ như ở đây là “nglong05.github.io”. Khi chọn một request bất kỳ, ta có thể xem được nội dung request mà trình duyệt đã gửi cũng như response trả về từ server. Mỗi lần pentester thao tác với ứng dụng web trên trình duyệt, một request mới sẽ xuất hiện trong phần history này.

Bên cạnh đó cũng còn chức năng quan trọng là  Intercept, như ở ảnh dưới khi ta tiếp tục thao tác GUI trên browser thì nó bắt request định gửi đi chứ chưa gửi cho server ngay lập tức. Điều này giúp ta chỉnh sửa thủ công từng request được gửi hoặc phân tích luồng request hoạt động với góc nhìn user:

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-37-10-image.png)

Request sẽ được gửi đi sau khi ta ấn vào forward. Hoặc ta có thể lựa chọn không gửi request bằng cách drop nó.

### Burp Repeater

Đây là module cho phép ta gửi lại một request bất kỳ nhiều lần theo ý muốn. Đúng như tên gọi, pentester có thể lặp lại các request và tùy ý chỉnh sửa chúng trước khi gửi tới server. Sau đó, có thể phân tích phản hồi từ server dựa trên những thay đổi đã thực hiện. Repeater thường được sử dụng để thủ công xác định và khai thác các lỗ hổng.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-39-52-image.png)

Chúng ta có thể ném request bắt được vào một khu vực này, từ đó có thể chỉnh sửa request đó và gửi lại request đó. Điều này giúp ta tấn công được bằng cách gửi các request kèm với payload của chúng ta mà không tốn nhiều công sức build lại một request hợp lệ.

### Burp Intruder

Đây là một công cụ mạnh mẽ cho phép tự động gửi request kèm payload tùy chỉnh. Ví dụ, Intruder có thể tự động tăng giá trị của một tham số và lần lượt gửi từng giá trị đó lên server. Nhờ vậy, pentester có thể tự động hóa các tác vụ lặp đi lặp lại vốn không thể thực hiện thủ công, chẳng hạn như gửi hàng nghìn request. Khả năng sử dụng Intruder gần như không giới hạn, với việc có thể thêm nhiều payload cùng loại hoặc khác loại.

Intruder có tab Positions để pentester xác định vị trí chèn payload trong request, sau đó có thể lựa chọn loại payload cần inject trong tab Payloads.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-44-59-image.png)

Trong ví dụ trên, một request cơ bản đang gọi tới file “repos?per_page=100”. Sử dụng Intruder, ta có thể kiểm tra sự tồn tại của các file từ 1 đến 1000. Cách thực hiện là đặt ký hiệu “§” bao quanh giá trị cần tăng dần, sau đó trong tab **Payloads** chọn phạm vi từ 1 đến 1000 để Intruder tự động gửi lần lượt các request tương ứng.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-47-07-image.png)

Sau khi thực hiện tấn công, một cửa sổ sẽ hiện ra kết quả thực hiện của request của 1000 request với từng số được cấu hình:

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-49-01-image.png)

### Vulnerability Scanner

Đây là một trong những tính năng quan trọng nhất của Burp Suite Professional. Scanner sẽ tự động thực hiện **passive scan** trên toàn bộ request giữa client và server, và **active scan** trên những request do pentester lựa chọn.

**Passive scan** chỉ phân tích luồng traffic, phát hiện lỗ hổng dựa trên các mẫu nhận diện sẵn có mà không làm thay đổi request. Ví dụ, nếu trong response có chứa địa chỉ email, Burp sẽ tự động báo cáo thông tin này.

Ngược lại, **active scan** chủ động chỉnh sửa request, chèn payload độc hại vào một hoặc nhiều vị trí được chọn rồi phân tích phản hồi từ server. Nếu server trả về kết quả thể hiện rõ ảnh hưởng từ payload, Scanner sẽ báo cáo mức độ lỗ hổng tương ứng.

Với khả năng này, Scanner là công cụ không thể thiếu, giúp pentester tiết kiệm thời gian và nâng cao hiệu quả kiểm thử. Để thực hiện **active scan**, chỉ cần gửi request sang Intruder, xác định vị trí payload như khi dùng Intruder thông thường, sau đó nhấp chuột phải và chọn “Do active scan”.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-51-11-image.png)

Kết quả của quá trình scan sẽ được hiển thị trong tab **Dashboard** của Burp Suite, nơi pentester có thể theo dõi chi tiết các phát hiện lỗ hổng và mức độ nghiêm trọng của chúng.

### Burp Collaborator

Đây là một dịch vụ của Burp cho phép pentester sử dụng một nền tảng trung gian trên Internet, có thể truy cập từ bất kỳ đâu. Collaborator đặc biệt hữu ích trong việc khai thác các lỗ hổng không trả về thông tin gì trong response của server nhưng vẫn cần được xác thực.

Các lỗ hổng dạng này thường không tạo ra lỗi, không trả về phản hồi bất thường hoặc cũng không gây ra độ trễ đáng kể. Ví dụ, nếu lỗ hổng cho phép thực thi lệnh hệ thống trên server nhưng kết quả của lệnh không hiển thị trong response, pentester có thể dùng Collaborator để exfiltrate dữ liệu và xác nhận lỗ hổng.

## Burp Suite Extensions

Pentester có thể cài đặt các extension do PortSwigger phát triển hoặc do cộng đồng xây dựng để mở rộng khả năng và đáp ứng thêm nhiều nhu cầu trong quá trình kiểm thử.

Đúng như tên gọi, mục **Extensions** cho phép tải xuống và quản lý các tiện ích mở rộng chính thức hoặc từ cộng đồng. Trong phần tiếp theo, chúng ta sẽ cùng xem xét những extension được coi là thiết yếu đối với một web pentester.

**Hackvertor**

 Đây là một extension dạng “toolbox” hỗ trợ chuyển đổi bất kỳ chuỗi ký tự nào sang kiểu mã hóa mong muốn. Extension này sử dụng các thẻ XML bao quanh chuỗi để xác định loại mã hóa hoặc chuyển đổi cần áp dụng. Các thẻ này có thể được dùng trực tiếp trong nhiều module của Burp như **Repeater** hay **Intruder**, đồng thời pentester cũng có thể tự định nghĩa thẻ XML của riêng mình để phục vụ các nhu cầu chuyển đổi nâng cao.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-55-26-image.png)

**Param Miner**

Đây là extension hỗ trợ tìm kiếm các header hoặc parameter ẩn trong một request. Công cụ này đặc biệt hữu ích khi kiểm tra các lỗ hổng thuộc dạng **web cache poisoning**.

Cách sử dụng rất đơn giản: chỉ cần chuột phải vào request muốn kiểm tra, chọn **Extensions**, **Param Miner**, rồi chọn loại test cần chạy. Ví dụ dưới đây minh họa việc tìm kiếm các header ẩn.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-13-56-40-image.png)

**JWT Editor**

Đây là extension dùng để phân tích và chỉnh sửa các JSON Web Token (JWT). Với công cụ này, pentester có thể giải mã, chỉnh sửa payload hoặc header của JWT, sau đó mã hóa lại để gửi đi. JWT Editor đặc biệt hữu ích khi kiểm thử các cơ chế xác thực dựa trên token, chẳng hạn như việc kiểm tra tính toàn vẹn của chữ ký hoặc thử nghiệm các thuật toán ký không an toàn.

Để sử dụng, chỉ cần chuột phải vào request chứa JWT, chọn **Extensions**, **JWT Editor**, rồi thực hiện việc decode, chỉnh sửa và encode lại token theo nhu cầu.

![](/home/nguyenlong05/.config/marktext/images/2025-08-20-14-00-15-image.png)

### Lời kết

Burp Suite là một công cụ gần như bắt buộc phải có khi làm pentest web. Từ những chức năng cơ bản như Proxy, Repeater, Intruder cho tới các tính năng nâng cao như Scanner, Collaborator hay hệ thống Extension, tất cả đều giúp quá trình phân tích và khai thác lỗ hổng trở nên dễ dàng và hiệu quả hơn.

Khi mới bắt đầu, chỉ cần nắm chắc Proxy, Repeater và Intruder là đã có thể thực hiện được khá nhiều kỹ thuật cơ bản. Sau đó có thể dần mở rộng sang Scanner, Collaborator và các Extension để phục vụ cho các tình huống nâng cao. Nếu sử dụng thành thạo, Burp Suite sẽ trở thành một công cụ “tất cả trong một” cho pentester trong quá trình kiểm thử ứng dụng web.
