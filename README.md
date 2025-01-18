# CryptographicDictGenerator

## 项目简介
`CryptographicDictGenerator` 是一个用于生成密码字典的工具，支持生成普通随机密码和基于社会工程学（社工）的密码。该工具可以帮助安全研究人员、渗透测试人员和白帽黑客创建自定义的密码字典，用于合法的安全测试和研究目的。

## 功能概述
- **普通密码生成**：根据指定的字符集、长度和其他规则生成随机密码。
- **社工密码生成**：基于个人信息（如生日、姓名、重要日期等）生成可能的密码组合。
- **配置管理**：支持保存和加载常用的配置参数。
- **灵活的命令行接口**：通过命令行参数控制生成过程，支持多种输出格式。

## 安装与配置

### 安装依赖
确保已安装Python 3.x环境。可以通过以下命令安装所需的依赖包：
~~~bash 
pip install -r requirements.txt
~~~
### 配置文件
配置文件位于 `config.yaml`，可以自定义生成密码的各种参数。示例配置文件如下：
~~~yaml 
lowercase: 2 
uppercase: 3 
umbers: 1 
symbols: 1 
total_length: 10 
random_length: true 
number: 5 
custom_set: null 
pattern: null 
exclude_chars: "0O" 
output_format: text
~~~
## 使用方法

### 普通密码生成
普通密码生成模式下，可以通过配置参数生成符合要求的随机密码。支持的命令行参数如下：

| 参数名          | 描述                                      | 默认值      |
|-----------------|-------------------------------------------|-------------|
| -l, --lowercase    | 密码中小写字符的位数                        | 0            |
| -u, --uppercase    | 密码中大写字符的位数                        | 0            |
| -n, --numbers      | 密码中数字的位数                            | 0            |
| -s, --symbols      | 密码中特殊符号的位数                        | 0            |
| -t, --total-length | 密码的总长度                                | 1            |
| -rl, --random-length| 密码为随机长度                              | False       |
| -nu, --number      | 生成密码的数量                              | 1            |
| -cs, --custom-set  | 自定义字符集，多个字符之间无分隔符          | None         |
| -pt, --pattern     | 密码模式模板，如 'LNL' 表示大写字母-数字-小写字母 | None         |
| -ex, --exclude-chars| 排除的字符，多个字符之间无分隔符            | ""           |
| -sc, --save-config | 保存当前配置到指定文件                    | None         |
| -lc, --load-config | 从指定文件加载配置                        | None         |
| -of, --output-format| 输出格式，默认为文本                      | text         |
| -o, --output-file  | 将生成的密码保存到指定文件                | None         |

#### 示例
生成10个长度为8的随机密码，包含2个小写字母、2个大写字母、2个数字和2个特殊符号：
~~~bash 
python main.py -l 2 -u 2 -n 2 -s 2 -t 8 -nu 10
~~~
## 文件结构
项目目录结构如下：
~~~
CryptographicDictGenerator/ 
├── README.md 
├── config.yaml 
├── main.py 
├── RegularPasswordDictionary/ 
│ ├── config_manager.py 
│ ├── logger.py 
│ └── password_generator.py
~~~
### 文件说明
- [`main.py`](file://main.py): 主程序入口，处理命令行参数和密码生成逻辑。
- [`config_manager.py`](file://RegularPasswordDictionary/config_manager.py): 配置文件管理，包括保存和加载配置。
- [`logger.py`](file://RegularPasswordDictionary/logger.py): 日志记录管理。
- [`password_generator.py`](file://RegularPasswordDictionary/password_generator.py): 密码生成逻辑实现。

## 常见问题解答 (FAQ)

### Q1: 如何生成更复杂的密码？
答：可以通过调整命令行参数中的 `-l`, `-u`, `-n`, `-s` 等选项来增加密码的复杂度。还可以使用 `-pt` 参数指定密码模式模板。

### Q2: 如何保存生成的密码到文件？
答：使用 `-o` 参数指定输出文件路径，例如：
~~~bash 
python main.py -l 2 -u 2 -n 2 -s 2 -t 8 -nu 10 -o output.txt
~~~
### Q3: 如何加载配置文件？
答：使用 `-lc` 参数指定配置文件路径，例如：
~~~bash 
python main.py -lc config.yaml
~~~
## 贡献指南
欢迎贡献代码或提出改进建议。请遵循以下步骤：
1. Fork 本项目。
2. 创建一个新的分支 (`git checkout -b feature-branch`)。
3. 提交更改 (`git commit -am 'Add some feature'`)。
4. 推送到新分支 (`git push origin feature-branch`)。
5. 提交Pull Request。

## 许可证
本项目采用MIT许可证，详情参见 [LICENSE](LICENSE) 文件。

---


