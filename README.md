将多个PNG文件自动转换为FS包。

已支持：帽子、衣服

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
        FS_type=HAT;素材类型：HAT/SHIRT
        input_img_name=;素材文件名（不包含png后缀）
        prefix=;生成的单个fs配置名称前缀
   ```
3. `python spriteslider.py`
4. 在执行目录下生成mod的压缩文件。

## TODO
- [ ] 衣服支持自动生成袖子颜色（当前：默认白袖子可调色）

- [ ] 支持发型

- [ ] 通过flow生成