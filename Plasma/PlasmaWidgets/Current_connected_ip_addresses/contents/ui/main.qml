import QtQuick 2.0
import org.kde.plasma.components 2.0 as PlasmaComponents


PlasmaComponents.Label {
    id: labelCurConnectedIpAddresses
    text: "Connected ip addresses: "

    Timer {
           id: textTimer
           interval: 1000
           repeat: true
           running: true
           triggeredOnStart: true
           onTriggered: labelCurConnectedIpAddresses.get_ip_addresses()
    }
    function get_ip_addresses()
    {
      var result = readTextFile("file:///tmp/list_connected_ip_addr.txt");
      labelCurConnectedIpAddresses.text = result;
    }

    function readTextFile(file)
    {
      var rawFile = new XMLHttpRequest();
      var allText = 'nothing';
      rawFile.open("GET", file, false);
      rawFile.onreadystatechange = function ()
      {
          if(rawFile.readyState === 4)
          {
              if(rawFile.status === 200 || rawFile.status == 0)
              {
                  allText = rawFile.responseText;
              }
          }
      }
      rawFile.send(null);
      return allText;
    }
}
