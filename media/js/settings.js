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
	//document.getElementById('btn_p2index').onclick = function(){
		//document.location.reload();
		//setTimeout($('#test01').slideDown(), 6000);
	//};
	
	
	 //$('.set_readonly').find('div').find('div').find('input').attr('readonly','readonly');
	
})
	