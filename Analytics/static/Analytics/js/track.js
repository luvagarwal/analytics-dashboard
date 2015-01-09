function sendUserAction(action_id, apparel_id)
{
    xmlObject = new XMLHttpRequest();
    details = '';
    details += "action_id=" + action_id;
    details += "&apparel_id=" + apparel_id;
    xmlObject.open("GET", "/Analytics/addrequest?"+details);
    xmlObject.send();
}

function getUserID()
{
    xmlObject = new XMLHttpRequest();
    num = 0;
    xmlObject.onreadystatechange=function(){
        if(xmlObject.readyState==4 && xmlObject.status==200)
        {
            return xmlObject.responseText;
        }
    }
    xmlObject.open("GET", "/Analytics/giveUserID", false);
    xmlObject.send();
    return xmlObject.onreadystatechange();
}
