import QtQuick 2.0
import org.kde.plasma.components 2.0 as PlasmaComponents

PlasmaComponents.Label {
    text: {
        return get_vulnerable_packages();
    }
    function get_vulnerable_packages()
    {
      var result = readTextFile("file:///tmp/vulnerablePackages.txt");
      return result;
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
                  alert(allText);
              }
          }
      }
      rawFile.send(null);
      return allText;
    }
}
