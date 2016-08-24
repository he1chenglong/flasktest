前后端 数据通信方式  总结

前端是指 网页 ，用户可以看到和 操作的界面，编程语言  HTML ,js

后端 指的是 服务器 ，编程语言  python，flask 
一 ： flash       服务器 向页面 传送字符串 

后：
from flask import Flask, jsonify, render_template, request,flash,json

flash("hello jikexueyuan")

前：
<a href=# id="uptext">  {{ get_flashed_messages()[0] }} </a>

这个实际是 flask 的模板技术 应用

二 ：把页面  用户的输入  传递给  后端
前 ;
HTML   POST 

<form action="/login" method="post">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Submit">   提交按钮
</form>

后：
@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

后端 通过  flash  ，和 刷新 页面的方式   ，将结果返回给 前端 

flash("please input username")
return render_template("index.html")

例子 03msg_error

下面的操作 使用了 JS  ，jQUERY

例子 01flaskapp


三 ：把页面  用户的输入  传递给  后端  

GET 方式：

前：
<script type="text/javascript">
  $(  function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {   
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val(),
        now: new Date().getTime()
      }, function(data) {     读取后端 返回的数据 
        $('#result').text(data.result);     显示 后端 返回的数据
        $('input[name=a]').focus().select();
      });
      return false;
    };

    $('a#calculate').bind('click', submit_form);  点击按钮
)}；
后：

@app.route('/_add_numbers')
def add_numbers():
    print 'call _add_numbers ...'
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)    通过request.args.get获取前端数据
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)    通过 jsonify  返回 json 数据 给 前端



四  ;   前端传送 JSON 数据 给后端
前：  
<script type="text/javascript">
  $(  function() {
var postjson = function(e){
    var data = {
          data: JSON.stringify({
                            "value":$('input[name="a"]').val()   将INPUT 框的数值
                        })
       }

        $.ajax({
           url:"/postjson",
           type: 'POST',
           data: data,
           success: function(msg){
                     $('#result').text(msg.result);
                      alert(msg);
                    }
        })
    };
    $('a#uptext').bind('click', postjson);
  });
</script>

后 ：

@app.route("/postjson", methods=['POST','GET'])
def getpostjson_data():
    print 'call postjson'
    data = json.loads(request.form.get('data'))
    ss = data['value']
    print str(ss)
    return 'ok'     返回字符串 




五  前端 轮询  后端数据的实现 

前：
<script >
    var polling = function(){
       $.post('/polling', function(data, textStatus){
          
 		读取后端返回的数据
              $.getJSON($SCRIPT_ROOT + '/polling', {
                now: new Date().getTime()
              }, function(data) {
                $('#result').text(data.result);   显示 后端返回的数据
              });
 
         });
    };
    interval = setInterval(polling, 1000);   每隔1S 轮询 一次
</script>

后 ：

@app.route("/polling",methods=['POST','GET'])
def polldata():
    print 'call polldata...'
    data = request.form.get('data')
    randomnum=random.randint(1,100)
    return  jsonify(result=randomnum)    返回随机数 ,json 格式



参考资料：1.
前端与后端的数据交互（jquery ajax+python flask）

http://www.jianshu.com/p/4350065bdffe
2.

flask  用 jQuery 实现 Ajax  局部 数据刷新
http://www.pythondoc.com/flask/patterns/jquery.html

