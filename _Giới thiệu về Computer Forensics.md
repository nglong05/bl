---
title: Giới thiệu về Computer Forensics

---

# Giới thiệu về Computer Forensics

Trong thời đại công nghệ hiện nay, nhất là trong quá trình kỹ thuật số hoá, sự cần thiết và cấp thiết của việc phát triển kỹ thuật điều tra số vẫn tiếp tục tăng ngày từng ngày. Trong bài viết này, ta sẽ đi tìm hiểu tổng quan về Computer Forensics - một nhánh quan trọng của an toàn thông tin. Từ khái niệm, phân loại, cho đến ví dụ trong CTF cũng như trong đời sống.

## Khái niệm Computer Forensics là gì?

Computer Forensics (Pháp y máy tính) hay còn được biết đến với tên gọi Digital Forensics (Pháp y kỹ thuật số) là một nhánh trong an toàn thông tin tập trung vào việc điều tra các vụ tấn công tội trên không gian số. Bằng nhiều kỹ thuật khác nhau từ đơn giản đến phức tạp như khôi phục và lưu trữ dữ liệu thu thập được để phân tích và tìm ra chứng cứ từ những thiết bị số. Trong bài viết này, khi đề cập tới Forensisc, ta hiểu là Computer Forensics.

Các cuộc điều tra computer forensics có thể được sử dụng trong đa dạng các trường hợp khác nhau, trong đó phải kể đến tội phạm mạng, điều tra hình sự, gian lận, mã độc, v.v...

Các cuộc điều tra này đưa ra những thông tin vô cùng quan trọng sau các cuộc tấn công, những thông tin ấy rất có giá trị trong quá trình tìm ra sự thật.

## Mục đích của pháp y máy tính

Để điều tra forensics trên không gian số, người ta có thể dựa vào những dữ liệu được thu thập hoặc phục hồi từ hệ thống máy tính, điện thoại thông minh, các ổ đĩa chứa nhật ký trong quá trình xảy ra tấn công.

Hiện nay, dưới sự phát triển của khoa học và công nghệ, đã có nhiều nghiên cứu khoa học về việc điều tra - pháp y. Nhìn chung, mục đích của việc điều tra số thường bao gồm:
    
* Để nhận định nguyên nhân và hậu quả của một cuộc tấn công
* Ngăn chặn kịp thời cuộc tấn công
* Bảo vệ các thiết bị kịp thời trước khi các lỗ hổng bị khai thác
* Truy vết ngược lại dấu vết của tin tặc, khám phá những loại mã độc mà tin tặc để lại
* Nhận định việc dữ liệu đã bị rò rỉ hoặc đánh cắp hay chưa
* Xác định khoảng thời gian mạng bị truy cập trái phép
* Theo dõi các hoạt động đăng nhập của tin tặc để truy tìm nguồn gốc của chúng
* v.v...

## Một số loại hình pháp y phổ biến

Các cuộc tấn công nhắm vào thiết bị số có thể diễn ra bằng rất nhiều cách thức và con đường khác nhau, do vậy các loại điều tra cũng rất đa dạng. Ta thường gặp những dạng điều tra số bao gồm:

### Điều tra trên không gian mạng

Là việc thu thập các bằng chứng sau cuộc tấn công, hay đơn giản là việc theo dõi, giám sát lưu lượng mạng để phát hiện những cuộc tấn công từ sớm và kịp thời ngăn chặn.

### Điều tra trên dữ liệu ổ cứng thu thập được

Đây là loại hình điều tra dựa trên các thiết bị vật lý, cụ thể hơn là ổ cứng - là nơi chứa nhật ký, những dấu vết mà tin tặc vẫn để sót lại. Ngoài ra, còn bao gồm cả việc khôi phục dữ liệu, tìm kiếm những bằng chứng liên quan.

### Điều tra trên RAM

RAM (Random Access Memory) có thể được coi như là "bàn làm việc" trong quá trình máy tính được bật, vì thế những dữ liệu thu được từ RAM cũng là những bằng chứng sắc bén phục vụ cho quá trình điều tra nói chung. Thường tập trung vào việc ánh xạ, trích xuất các tập tin đang được sử dụng.

### Điều tra trên các thiết khác như: di động, PDA, GPS, tablet, ...

Công nghệ ngày càng phát triển, các thiết bị càng trở nên đa dạng thì sẽ càng dễ trở thành tầm ngắm của các cuộc tấn công. Do vậy cần thiết phải có những phương thức điều tra cụ thể đối với các thiết bị khác nhau chứ không chỉ mỗi máy tính.

Ngày nay, AI và blockchain đang trong quá trình phát triển mạnh mẽ, việc điều tra trên các thiết bị này ngày càng trở nên hiệu quả và chính xác hơn. AI có thể giúp phân tích và phát hiện các mẫu hành vi bất thường, nhận diện các cuộc tấn công và dự đoán các nguy cơ tiềm ẩn, trong khi blockchain có thể giúp xác thực các giao dịch và xác minh tính toàn vẹn của dữ liệu.

## Mảng Forensics trong CTF

CTF (Capture The Flag) là một dạng thi đấu, nơi mà người chơi phải giải quyết các thử thách được đưa ra để lấy được **flag** được ẩn giấu dưới những thử thách.

CTF Forensics và các mảng khác thường dựng lại những thử thách giống với quá trình điều tra, thu thập hay tấn công thường gặp trong thực tế. Từ đó giúp ta nâng cao kĩ năng trong lĩnh vực bảo mật khi tiếp xúc đa dạng các thử thách khác nhau.

Trong CTF, mảng Forensics ta thường bắt gặp những dạng bài như sau
    
### Memory forensics

Đúng như tên gọi, memory forensics là việc điều tra bộ nhớ RAM được lấy ra trong quá trình mô phỏng một cuộc tấn công. Người chơi cần sử dụng các công cụ hỗ trợ để có thể dump ra các file khả nghi, kết hợp thêm khả năng suy đoán và tìm kiếm để tìm ra flag ẩn giấu.

Thông thường, Memory Forensics mang những đặc điểm chung của Computer Forensics như:

* Dữ liệu cần phân tích thường lớn hoặc rất lớn
* Dữ liệu có thể không còn nguyên vẹn, bị thay đổi, bị phân mảnh.
* Dữ liệu bị giả mạo

### Steganography

Steganography là phương pháp che giấu thông tin trong các file media như ảnh, văn bản, âm thanh, video mà không làm cho người đọc hoặc người xem file cảm thấy nghi ngờ. Steganography không chỉ ẩn giấu thông tin, mà còn ẩn giấu cả sự tồn tại của thông tin đó

Thường gặp nhất là trong steganography ảnh, người ta có thể cố ý giấu những dữ liệu vào những bit ít quan trọng của hình ảnh, sao cho người xem ảnh vẫn không nhận ra điều gì, không làm ảnh hưởng tới việc người khác xem ảnh.

### Hard drive forensisc

Việc phân tích dữ liệu ổ cứng cũng là một dạng bài thường thấy trong các thử thách forensics. Dễ tiếp cận nhất có thể kể tới việc phân tích các tệp tin trong một file image của hệ điều hành Windows.

Trong file image ấy, có thể người chơi sẽ được yêu cầu tìm ra những phần mềm độc hại mà người dùng Windows đã mở lên, hoặc người chơi cũng có thể được yêu cầu sẽ phải khám phá và khôi phục dữ liệu của một file cụ thể nào đó. Người chơi cũng đôi khi cần phải bẻ khoá một file hay khôi phục lại những file đã bị hỏng (corrupted)

### Network forensics

Là pháp y về mạng, nơi người chơi cần phải phân tích các gói tin được capture lại trong quá trình máy tính giao tiếp với máy chủ, hoặc các gói tin được truyền qua các thiết bị đầu cuối.

Từ những gói tin được cung cấp, người chơi cần phân tích những gì được gửi kèm đi. Chẳng hạn như những file được truyền đi trong 1 gói tin FTP, hay những file được trình duyệt tải xuống trong các gói tin HTTP.

### Application forensics

Application forensics liên quan đến việc phân tích và điều tra các ứng dụng cài đặt trên hệ thống. Người chơi sẽ phải tìm hiểu cách thức hoạt động của các ứng dụng, xác định những điểm yếu bảo mật hoặc các lỗ hổng mà tin tặc có thể lợi dụng để tấn công.

Quá trình này có thể bao gồm việc kiểm tra các logs của ứng dụng, theo dõi hành vi của ứng dụng trong hệ thống hoặc phân tích mã nguồn của nó. Một số thử thách có thể yêu cầu tìm ra các lỗi bảo mật nghiêm trọng hoặc các dấu vết để lại bởi các cuộc tấn công đã xảy ra trước đó.

### Malware forensics

Malware là viết tắt của "malicious software" (phần mềm độc hại). Việc phân tích malware sẽ giúp xác định, hiểu và giảm thiếu sự đe doạ của malware tới các hệ thống, mạng, ...

Để phân tích malware, phải thu thập các mẫu malware, cài đặt môi trường, sau đó mới tiến hành các bước phân tích như phân tích tĩnh, phân tích động, phân tích hành vi, phân tích hậu quả.

Malware forensics nói chung cần thêm kĩ năng dịch ngược và đọc hiểu hợp ngữ, bởi có rất nhiều malware được làm rối mã nguồn và tinh chỉnh rất tinh vi nhằm qua mặt hệ thống và các anti-virus.

## Các kỹ năng cần có, công cụ thường được sử dụng

### Biết lập trình, đọc hiểu code

Muốn phân tích được những gì có trong các thiết bị số, việc đọc hiểu code là điều bắt buộc. Ngoài ra, trong các thử thách CTF ta cũng rất hay phải viết những script để khai thác lỗ hổng, hay để giải đố những gì được yêu cầu.

Bên cạnh những yêu cầu về lập trình, cũng cần phải có các kiến thức ở mức độ tốt về hệ điều hành, phần mềm, phần cứng, ...

### Sử dụng các hệ điều hành dựa trên Linux

Để thuận tiện hơn trong quá trình chơi CTF, ta cần thiết phải sử dụng tới các hệ điều hành dựa trên Linux. Phải kể tới Kali Linux, đây là một bản phối dựa trên Debian được thiết kế riêng cho pháp y số và tấn công thăm dò.

Ngoài ra, có thể tham khảo thêm [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) để tận dụng sức mạnh của Linux và Windows ngay trên hệ điều hành Windows.

### Các lệnh cơ bản trên Linux

#### Lệnh `strings`

Cú pháp

```bash
strings <file_name>
```

dùng để tìm kiếm và in ra các chuỗi có thể in được trong một tệp.

Có thể kết hợp thêm với lệnh `grep` để tìm những chuỗi nào chứa đoạn chữ mong muốn. Ví dụ như sau

```bash
strings malware.exe | grep "flag{"
```

Lệnh trên sẽ tìm đoạn nào có chứa "flag{" và highlight lên cho ta dễ nhìn.

#### Lệnh `file`

Giúp xem kiểu định dạng của file (tức là phần đuôi mở rộng như .exe, .txt, .docx, .pdf, v.v...

Cú pháp

```bash
file <file_name>
```

Ví dụ khi người ta cố tình đổi 1 file `flag.txt` thành `flag.zip`, nếu chỉ nhìn bằng mắt thường ta sẽ nhầm đây là file nén đuôi .zip, khi mở lên thì chắc chắn phần mềm giải nén sẽ không đọc được. Khi ấy để xác định chính xác, ta chạy `file flag.zip`

Khi ấy, ta nhận được kết quả

```bash
$ file flag.zip
flag.zip: ASCII text
```

và biết chắc chắn đây là file `.txt`

### Các công cụ hỗ trợ

Do mảng forensics có rất nhiều công cụ có thể dùng cho các dạng bài khác nhau, mỗi công cụ lại có cách dùng tuỳ thuộc vào yêu cầu đề bài. Do đó không thể kể chi tiết từng công cụ trong bài viết này nên mình sẽ để danh sách những công cụ thường gặp ở dưới đây. 

#### Phân tích chung
* Autopsy
* Bulk Extractor
* DB Browser for SQLite
* FTK Imager
* Hindsight
#### Chromebook
* cLEAPP
#### Ciphers
* CyberChef
* dcode.fr
#### Google Takeout / Returns
* RLEAPP
#### Mac
* mac_apt
* plist Editor - iCopyBot
#### Malware/PE
* PEStudio
* PPEE (puppy)
* IDA Pro
* Binary Ninja
* dnpsy
#### Memory/RAM
* MemProcFS
* Volatility 3
* Volatility 2
#### Mobile Devices
* ALEAPP
* Andriller
* APOLLO
* ArtEX
* iBackupBot
* iLEAPP
#### Networks
* Wireshark
* NetworkMiner
#### Windows Analysis
* Eric Zimmerman tools / KAPE
* USB Detective
#### Office Documents
* oletools, oledump
* PDFTools
#### Steganography
* Aperi’Solve
* zsteg, steghide, stegsolve, ..

## Tài liệu tham khảo

Cả CTF nói chung và CTF forensics nói riêng đều rất đa dạng, từ dạng bài, cách giải. Để chơi CTF ngày càng tốt hơn, không có cách nào khác ngoài chăm chỉ chơi CTF, tiếp xúc đa dạng các dạng bài và từ đó học hỏi thêm kinh nghiệm.

Để luyện tập chơi CTF, có những trang web sau đây

1. [picoCTF](https://play.picoctf.org/practice)
2. [TryHackMe](https://tryhackme.com/)
3. [Cyber Defender](https://cyberdefenders.org/blueteam-ctf-challenges/)
4. [HackTheBox](https://www.hackthebox.com/)
5. [BUUCTF](https://buuoj.cn/)