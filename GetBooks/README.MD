背景说明：
本工具不是用来盗取数据，只是很多时候需要离线读书，或者省点钱，只可用于自读，不应该用于窃取微信读书的书籍
运行：
1.依赖python selenium pyautogui PIL 需要自行安装
2.需要安装chrome插件 gofullpage, 安装之后记得将工具钉在工具栏上，如图：
![image](https://user-images.githubusercontent.com/59589551/192925167-ac24f80f-0a5f-4689-af67-461ff847f415.png)
脚本上的click的坐标就是插件的屏幕坐标
3.gofullpage 设置如下：
![image](https://user-images.githubusercontent.com/59589551/192924702-f641e8e0-c5b4-4fe2-ba4a-e8a5c2b107ba.png)
4.先用命令chrome --remote-debugging-port=9527 --user-data-dir="C:\ChromeTmp"打开chrome, 工具中的路径可以自行设置
5.在chrome中打开微信读书，登入，打开书籍，确定插件屏幕坐标和脚本是否一致
6.运行脚本
