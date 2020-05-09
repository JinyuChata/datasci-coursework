# datasci-coursework
## data文件夹
用于存放原始数据
- **case_test.json**   

  题目的测试用例个数及题目答案的程序行数,格式如下

  ```json
  {
      "2061": {
          "测试用例个数": 1,
          "脚本行数": 90
      },
      ...
  }
  ```

- **case_analysis_source.json**

  题目的简单数据收集，包括题目的类别，提交次数，有效提交次数（100分提交为有效提交），平均得分，方差，格式如下

  ```json
  {
     "2179": {
          "题目类别": "数组",
          "总提交次数": 61,
          "有效提交次数": 56,
          "平均得分": 91.80327868852459,
          "方差": 752.4858908895447
      },
      ...
  }
  ```

- **cases_url.json**

  题目编码后的下载地址，数据格式如下

  ```json
  {
       "2908": "http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/%E5%8D%95%E8%AF%8D%E5%88%86%E7%B1%BB_1581144899702.zip",
      ...
  }
  ```

- **sample.json**

  样本数据，数据格式同test_data.json

- **test_data.json**

  原始数据，一切其他的数据都是通过分析该文件得出的,数据格式如下

  ```json
  {
      "3544":{
          "user_id":3544,
          "cases":[
              {
                  "case_id": "2908",
                  "case_type": "字符串",
                  "case_zip": "http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/单词分类_1581144899702.zip",
                  "final_score": 40,
                  "upload_records":[
                      {
                          "upload_id": 236494,
                          "upload_time": 1582023290656,
                          "code_url": "http://mooctest-dev.oss-cn-shanghai.aliyuncs.com/data/answers/4238/3544/%E5%8D%95%E8%AF%8D%E5%88%86%E7%B1%BB_1582023289869.zip",
                          "score": 40.0
                      },
                      ...
                  ]
              },
              ...
          ]
      }
  }
  ```

## cases文件夹

所有题目的zip文件

## data retrieval文件夹

获取数据的python脚本文件

- **case_decompression.py**

  解压缩cases文件夹中的文件，获取所有题目的测试用例个数和答案代码行数

  输出为case_test.json文件

- **case_download.py**

  输入为cases_url.json,

  下载所有的题目

  输出为cases文件夹

- **cases_retrieval.py**

  输入为test_data.json

  获取每一道题目的类型，总提交次数，有效提交次数，平均得分，方差

  

  