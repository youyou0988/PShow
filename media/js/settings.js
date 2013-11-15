function ChangeDiv(divId,divName,zDivCount)
{
for(i=0;i<=zDivCount;i++)
 {
     document.getElementById(divName+i).style.display="none";
 }
 document.getElementById(divName+divId).style.display="block";
}
window.onload = function(){
	document.getElementById('btn_previous').onclick = function(){
		//$('#previous_new').toggle();
	}
    $('.set_readonly').find('div').find('div').find('input').attr('readonly','readonly');
	
}
	