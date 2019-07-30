#--------------------------------html text-------------------------------------------
html_text="""
<html>
<head>
<META HTTP-EQUIV="expires" CONTENT="0">
<META HTTP-EQUIV="pragma" CONTENT="no-cache">
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate">
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<title>Status</title>
<link rel="stylesheet" href="./stylesheets/nb.css" type="text/css">
<link rel="stylesheet" href="./stylesheets/tablesorter.css" type="text/css">
<script type="text/javascript" src="./javascripts/common.js"> </script>
<script type="text/javascript" src="./javascripts/jquery.js"></script>
<script type="text/javascript" src="./javascripts/jquery.tablesorter.js"></script>
<script>

var rateArrary;

$(function() {
	if ($("#wlanTable") != null)
		$("#wlanTable").tablesorter();
	$("#myTable").tablesorter();
});	

var g_ulTotalSec = 0;
function UpdateTimeShow()
{
	var oriSeconds = 78554;

	if (g_ulTotalSec <= 0)
		g_ulTotalSec = oriSeconds;
	document.getElementById("uptime_div").innerText = Second2Str(g_ulTotalSec);
	g_ulTotalSec++;
	setTimeout('UpdateTimeShow()', 1000);
}

function UpdateRouter()
{
	var form = document.statusform;
	var bNetRouter = Number(0) == 1;
	var netWanIpType = Number(0);
	var netWanIp = "192.168.0.99";
	var pppConnectType = Number("0");
	var bEmpty = (netWanIp == c_EmptyIp) || ((Number(0) == 0 && netWanIpType != 0));

	ShowDiv(!bNetRouter, "brdige_gateway_div");
	if(!bNetRouter)
		return false;

	ShowDiv(bNetRouter, "wan_status_div");
	ShowDiv(bNetRouter, "wan_status_hr");
	
	document.getElementById("netWanIpType").innerText = GetResourceString(ipTypeArray, netWanIpType);
	document.getElementById("netWanDns1").innerText = bEmpty ? c_EmptyIp : '0.0.0.0';
	document.getElementById("netWanDns2").innerText = bEmpty ? c_EmptyIp : '0.0.0.0';
	
	switch(netWanIpType)
	{
	case 1:	// DHCP client
		EnableField(form.btnConnect, true);
		form.btnConnect.value = bEmpty ? "Renew" : "Release";
		break;
	case 2:	// PPPoE
	case 3:
	case 4:
		EnableField(form.btnConnect, pppConnectType == 2);
		form.btnConnect.value = bEmpty ? "Connect" : "Disconnect";
		break;
	default:
		ShowDiv(false, "btnConnect");
		break;
	}
	return true;
}

function UpdateIfStatus()
{
	var xmlHttp;

	xmlHttp = createAjax();
	xmlHttp.onreadystatechange = function ()
	{
		if ((xmlHttp.readyState == 4) && (xmlHttp.status == 200))
		{
			var IfStatus = eval("(" + xmlHttp.responseText + ")");

			bContinue = Number(IfStatus.success) != 0 || $("#if_body").val() == "";
			if (bContinue)
			{
				var if_html = "";

				$("#if_body").empty();
				for (var i=0; i<g_ProductSpec.ulRfNum; i++)
				{
					var title = g_ProductSpec.ulRfNum>1 ? ("RF" + " " + (i+1).toString()) : "Wireless";
					var channel = IfStatus.wlan[i].Channel;
					var opmode = Number(IfStatus.wlan[i].OpMode);
					var wirmode = Number(IfStatus.wlan[i].WirMode);
					var chanmode = Number(IfStatus.wlan[i].ChanMode);
					var shortgi = Number(IfStatus.wlan[i].ShortGI);
					var bHasH20ShortGI = Number(g_ProductSpec.RfInfos[i].bHt20ShortGI);
					var chains = CalcBitsSet(g_ProductSpec.RfInfos[i].ulChainMask);
					var rateArray;
					var rate = "", status = "";

					if (opmode != 1 && (!Is80211nMode(wirmode)
					  || !(chanmode==1 || chanmode==2 || (chanmode==0 && bHasH20ShortGI))))
						shortgi = false;
					rateArrary = GenDatarateArray(wirmode, shortgi, chains);
					rate = GetResourceString(rateArrary, Number(IfStatus.wlan[i].TxRate));
					status = GetResourceString(upDownArray, Number(IfStatus.wlan[i].Status));
					if_html += "<tr>";
					if_html += "<td>" + title + "</td>";
					if_html += "<td>" + status + "</td>";
					if_html += "<td>" + channel + "</td>";
					if_html += "<td>" + rate + "</td>";
					if_html += "</tr>";
				}
				for (var i=0; i<g_ProductSpec.ulEthNum; i++)
				{
					var title = g_ProductSpec.ulEthNum>1 ? ("Ethernet" + " " + (i+1).toString()) : "Ethernet";
					var status = GetResourceString(upDownArray, Number(IfStatus.eth[i].Status));
					var rate = GetResourceString(etherRateArray, Number(IfStatus.eth[i].TxRate));
					var channel = IfStatus.eth[i].Channel;

					if_html += "<tr>";
					if_html += "<td>" + title + "</td>";
					if_html += "<td>" + status + "</td>";
					if_html += "<td>" + channel + "</td>";
					if_html += "<td>" + rate + "</td>";
					if_html += "</tr>";
				}
				$("#if_body").append(if_html);
				$("#myTable").trigger('update');
			}
		}
	}
	xmlHttp.open("GET", "/goform/ajaxGetInfo?sid="+Math.random() + "&name=" + "IfStatus", true);
	xmlHttp.send(null);

	setTimeout('UpdateIfStatus()', 2000);
}

function initpage()
{
	var bNetBridge = Number(0) == 0;
	var connTime = Number(0);
	var netWanIpType = Number(0);

	document.getElementById("connTime_id").innerText = Second2Str(connTime);
	setTimeout('UpdateTimeShow()', 0);
	ShowDiv(bNetBridge, "sysmac_div");
	ShowDiv(!bNetBridge, "lanmac_div");
	ShowDiv(netWanIpType != 0, "connTime_div");

	UpdateRouter();
	setTimeout('UpdateIfStatus()', 120);
	//ShowDiv(opMode == 1, "signal_div");
}

</script>
</head>
<body onLoad="initpage();">

<div class="box">
	<h2>Information</h2>
	<span class="note">
	This page shows the current status and some basic settings of the device.
	</span>
</div>
<hr>
    
    
<div class="box">
	<h3>System Information</h3>
	<table class="text">	
		<!--tr>
			<td>Model Name:</td>
			<td>EKI-6331AN-BE</td>
		</tr-->
		<tr id="sysmac_div">
			<td>MAC Address:</td>
			<td>00:d0:c9:fa:e5:d5</td>
		</tr>
		<tr>
			<td>Firmware Version:</td>
			<td>1.2.6.1(AD)16</td>
		</tr>
		<tr>
			<td>System Uptime:</td>
			<td id="uptime_div"></td>
		</tr>
		<tr>
			<td width="40%">Device Name:</td>
			<td width="60%">apfae5d5</td>
		</tr>
		<tr>
			<td>Country/Region:</td>
			<td>United States</td>
		</tr>
		<tr >
			<td>Mem Usage:</td>
			<td>21.894 %</td>
		</tr>
	</table>
</div>
<hr id="wan_status_hr" style="display:none">
    
    
<form action=/goform/formStatusSetup method=POST name="statusform">
<div class="box" id="wan_status_div" style="display:none">
    <h3>WAN Settings</h3>
    <table class="text">
      <tr>
        <td>MAC Address:</td>
        <td>00:d0:c9:fa:e5:d5</td>
      </tr>
      <tr id="connTime_div">
        <td width=40%>Connected Time:</td>
        <td width=60% id="connTime_id"></td>
      </tr>
      <tr>
        <td>Access Type:</td>
        <td><span id="netWanIpType"></span>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <input type="submit"  name="btnConnect" id="btnConnect">
        </td>
      </tr>
      <tr>
        <td width=40%>IP Address:</td>
        <td width=60%>192.168.0.99</td>
      </tr>
      <tr >
        <td width=40%>Subnet Mask:</td>
        <td width=60%>255.255.255.0</td>
      </tr>
      <tr>
        <td width=40%>Gateway IP Address:</td>
        <td width=60%>192.168.0.254</td>
      </tr>
      <tr>
        <td width=40%>DNS 1:</td>
        <td width=60% id="netWanDns1"></td>
      </tr>
      <tr>
        <td width=40%>DNS 2:</td>
        <td width=60% id="netWanDns2"></td>
      </tr>
    </table>
</div>
<hr>
    
    
</form>
<div class="box">
	<h3>LAN Settings</h3>
	<table class="text">
		<tr id="lanmac_div">
			<td>MAC Address:</td>
			<td>00:d0:c9:fa:e5:d5</td>
		</tr>
		<tr>
			<td width="40%">IP Address:</td>
			<td width="60%">192.168.1.1</td>
		</tr>
		<tr>
			<td>Subnet Mask:</td>
			<td>255.255.255.0</td>
		</tr>
		<tr id="brdige_gateway_div" style="display:none">
			<td>Gateway IP Address:</td>
			<td>0.0.0.0</td>
		</tr>
	</table>
</div>
<hr>
    
    
<div class="box">
	<h3>Wireless Settings</h3>
	<table class="text">
		<tr>
            <td width='40%'>Operation Mode:</td>
            <td width=60%'><script>document.write(GetResourceString(opModeArray, 0));</script></td>
        </tr>
        <tr>
            <td>802.11 Mode:</td>
            <td><script>document.write(GetResourceString(wirModeArray, 5));</script></td>
        </tr>
        <tr>
            <td>SSID:</td>
            <textarea id='text_ssid' style='display:none' disabled>testing0705</textarea>
            <td id='ssid_id'></td>
        <script>document.getElementById('ssid_id').innerText = document.getElementById('text_ssid').innerText;</script>
        </tr>
        <tr>
            <td>Encryption:</td>
            <td><script>document.write(GetResourceString(authModeArray, 0));</script></td>
      </tr>
      <tr>
        <td>ACK Timeout:</td>
        <td>35 &#956;s</td>
        </tr>

	</table>
</div>
<hr>
<div class="box">
	<h3>Interface Status</h3>
	<table class="text"><tr><td>
		<table width="100%" cellspacing="1" id="myTable" class="tablesorter">
			<thead>
			<tr>
				<th>Interface</th>
				<th>Status</th>
				<th>Channel</th>
				<th>Rate</th>
			</tr>
			</thead>
			<tbody align="center" id="if_body">
			</tbody>
		</table>
	</td></tr></table>
</div>
<hr>                                                                                                                                                                                                      
                                                                                                                
  <p align="center">
    <input type="button" value="Refresh" name="refresh" onClick="RefreshPage();">
  </p>
</body>
</html>
"""
#-----------------------------------------------------開始爬蟲-----------------------------


from bs4 import BeautifulSoup
soup=BeautifulSoup(html_text,'html.parser')
data=soup.find_all("td")
dictionary={}
for i in range(0,len(data),2):
    try :
        dictionary[data[i].string]=data[i+1].string
    except:
        break
print (dictionary)
print("----------------------------------------------")

"""
import csv
data_csv = open('data.csv', "a+")
csvwriter = csv.writer(data_csv)

count = 0
for i in dictionary.items():
    if count == 0:
        header = i.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(i.values())

data_csv.close()
"""



#07/26輸出到csv尚未完成，再進修
