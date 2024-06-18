import QtQuick 2.0
import org.kde.plasma.components 2.0 as PlasmaComponents


PlasmaComponents.Label {
    id: lableVulPackages
    text: "Vulnearable packages: "
    
    Timer {
           id: textTimer
           interval: 1000
           repeat: true
           running: true
           triggeredOnStart: true
           onTriggered: lableVulPackages.get_vulnearable_packages()
    }
    function get_vulnearable_packages()
    {
      var result = readTextFile("file:///tmp/vulnerablePackages.txt");
      lableVulPackages.text = result;
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
