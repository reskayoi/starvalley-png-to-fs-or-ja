将多个PNG文件自动转换为FS/JA包。

已支持：FS:帽子、衣服、发型 JA:衣服

## 使用方式
1. 安装python和pillow包
2. 配置config.ini
    ```ini
   [manifest]
   name=;mod名字
   author=;作者
   version=;版本
   description=;说明
   uniqueID=;modId

   [用于区分不同PNG的设置]
   FS_type=HAT;素材类型：HAT/SHIRT/HAIR
   input_img_name=;素材文件名（不包含png后缀）
   prefix=;生成的单个fs配置名称前缀
   ```
3. `python spriteslider.py`
4. 在执行目录下生成mod的压缩文件。

### 进阶参数设置
```ini
slide_height=自定义单个贴图的高度
slide_width=自定义单个贴图的宽度
slide_num=自定义几个贴图组成一个素材图片
resize=是否在读取图片前去除四周空白（不建议使用，除非原有图片大小不符合规范，且单个贴图不存在整行或整列的空白）
preview=是否在压缩包内存放总预览图

--模式切换--
[run]
pack_mode=JA;FS/JA

--FS的SHIRTS类型特别设置--
sleeve=true;是否有袖子
sleeve_color=true;true时，从自定义像素点取色
cus_sleeve_color=[(0,0),(0,2),(0,4)];贴图取色的像素点，不设置时默认为[(0,0),(0,1),(0,2)]
```

## TODO
- [x] 衣服支持自动生成袖子颜色（当前：默认白袖子可调色）

- [x] 支持发型

- [ ] JA模式（当前部分支持）

- [ ] 通过flow生成