// Sample Markers on Page
var MarkersInit = function(markers) {
  var elements = document.querySelectorAll('.wavesurfer-marker');
  Array.prototype.forEach.call(elements, function(el, i) {
    var time_start = el.dataset.start;
    var time_end = el.dataset.end;
    var id = el.dataset.id;;
    if (id >= 1) {
      id = id - 1;
    } else {
      id = 0;
    }
    marker = {};
    marker.time_start = time_start;
    marker.time_end = time_end;
    marker.dom = el;
    if (typeof(markers[id]) === 'undefined') {
      markers[id] = [];
    }
    markers[id].push(marker);
  });
}

// On Ready
document.onreadystatechange = () => {
  if (document.readyState === 'complete') {

    // Init Markers
    var markers = [];
    MarkersInit(markers);

    // Create SoundCloud Player Object ( TODO: all loop)
    var iframeElement = document.getElementById("musicframe");
    var widget = SC.Widget(iframeElement);

    // Register On Click Event Handler
    var elements = document.querySelectorAll('.wavesurfer-marker');
    Array.prototype.forEach.call(elements, function(el, i) {
      el.onclick = function() {
        // Get Data Attribute
        var pos = el.dataset.start * 1000 +1;
        // Seek
        widget.seekTo(pos);
      }
    });

    // Bind Continuous Play
    widget.bind(SC.Widget.Events.PLAY_PROGRESS, function() {
      widget.getPosition(function(current_time) {
        current_time = current_time / 1000;
        var j = 0; // NOTE: to extend for several players
        markers[j].forEach(function(marker, i) {
          if (current_time >= marker.time_start && current_time <= marker.time_end) {
            marker.dom.classList.add("wavesurfer-marker-current");
            marker.dom.scrollIntoView({block: 'nearest'})
          } else {
            marker.dom.classList.remove("wavesurfer-marker-current");
          }
        });
      });
    });

  } // Document Complete
}; // Document Ready State Change

function openInfo(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click(); 