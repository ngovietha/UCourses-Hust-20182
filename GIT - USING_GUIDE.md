# Git - Using Guide

## 1. Tổng quan

Git dùng để quản lý code. Vậy thôi.


---

## 2. Clone, Commit, Pull và Push

### 2.1 Kéo Project về
> git clone https://github.com/quyctd/UCourses-Hust-20182.git
> 

sau "clone" là đường dẫn của project.

### 2.2 Báo git nhận thay đổi file

> git stage .

> git commit -m "Your message go here"
> 

Thay "Your message go here" thành message bạn muốn git biết. **Bắt buộc phải có message**.

### 2.3 Kéo Code mới trên github về

Trước khi kéo code về **PHẢI COMMIT**.

Để kéo code về dùng:

> git pull
> 

### 2.4 Đẩy code mới của bạn lên github.

Tương tự kéo code mới về, trước khi đẩy code mới lên **PHẢI COMMIT**.

Để đẩy code lên dùng:
> git push
> 


---

## 3. Làm việc với branch.

Trong 1 project thì người ta chia các branch ra làm việc cho nó rõ ràng + hiệu quả + không bị conflic các thứ.

Ví dụ ở project mình hiện đang có 1 số branch sau:
> *master

> dev

> dev_auth

> dev_categories

> ...

> 

**Khi ở các branch khác nhau thì commit, pull, push vẫn như hướng dẫn bên trên. Đừng làm khác ^^**

### 3.1 Kiểm tra branches

Để biết mình đang ở branch nào gõ:

> git branch
> 
Dòng nào có dấu * là mình đang ở branch đấy.

Ví dụ:
![](https://i.imgur.com/2GMMWb9.png)

Đây là t đang ở branch dev.

### 3.2 Chuyển đổi branch

Trước khi chuyển đổi branch **PHẢI COMMIT**

Để chuyển đổi giữa các branch gõ:
> git checkout *branch_name*
> 

Ví dụ:
> git checkout dev
> 

### 3.3 Lấy toàn bộ code mới về (Dù khác branch)

Đã pull là **PHẢI COMMIT.**

> git pull --all
> 

### 3.4 Merge code

Merge code có thể hiểu như sau:

Ví dụ nhánh dev_auth đã làm xong, người dùng đã có thể login, register, logout được rùi thì cần chuyển code này sang nhánh dev. Khi đó người ta dùng merge code.

Để merge code từ nhánh dev_auth sang nhánh dev làm như sau:

> git checkout dev (Sang nhánh dev)

> git merge dev_auth (Đưa code nhánh dev_auth vào nhánh dev)


**Công việc này thường là do thằng lead làm, merge linh tinh là chết cả project đó**



---

## 4. Lời kết.

**KHUYẾN CÁO TOÀN THỂ BÀ CON LÀ CHỈ DÙNG NHỮNG LỆNH HỆT NHƯ BÊN TRÊN, TRÁNH DÙNG CÁC LỆNH BÊN TRÊN KÈM THEO CÁC OPTION KHÁC KHI MÀ CHƯA HIỂU RÕ NÓ LÀ GÌ.**

Ví dụ:
> git push -u origin master
> 

Lệnh trên sẽ xóa hết code mới của người khác và chỉ lưu giữ lại code giống như trong máy của bạn. ---> **Là MẤT CODE đó.**



---

# HẾT RÙI