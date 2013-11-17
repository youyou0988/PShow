function ChangeDiv(divId,divName,zDivCount)
{
for(i=0;i<=zDivCount;i++)
 {
     document.getElementById(divName+i).style.display="none";
 }
 document.getElementById(divName+divId).style.display="block";
}
function timedMsg()
 {
 	var t=setTimeout(function(){
 		yyyy();
 	},3000);
 }
 function yyyy(){
 	alert('5 seconds!');
 }

$(document).ready(function(){
	document.getElementById('btn_p2index').onclick = function(){
		alert("h");
		window.onload=function(){
			alert("haha");//不执行
			$('#test01').slideDown();//不执行
		};
		if (document.readyState && document.readyState == 'complete') {
				alert("ha");//没有等待表单刷新完就执行了
				$('#test01').slideDown();//瞬间显示，表单刷新完之后消失
				//因为原来的css设为了不显示
		} else {
			setTimeout("alert('haha');", 10);
		}
	};
	
	
	 //$('.set_readonly').find('div').find('div').find('input').attr('readonly','readonly');
	
})
	