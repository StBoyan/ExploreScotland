$(document).ready(function() {
    initMap();
});


function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 57.113387,
            lng: -3.632542
        },
        zoom: 7,
        gestureHandling: 'none'
    });



    var markers = [{
            "title": 'Glasgow',
            "lat": '55.881579',
            "lng": '-4.219419',
        },
        {
            "title": 'Edinburgh',
            "lat": '55.951570',
            "lng": '-3.349419',
        }, {
            "title": 'Loch Ness',
            "lat": '57.362709',
            "lng": '-4.386354',
        }, {
            "title": 'Dundee',
            "lat": '56.504614',
            "lng": '-3.002565',
        }, {
            "title": 'Aberdeen',
            "lat": '57.157645',
            "lng": '-2.120914',
        }, {
            "title": 'Stirling',
            "lat": '56.115432',
            "lng": '-3.924594',
        }
    ];


    for (var i = 0; i < markers.length; i++) {
        var data = markers[i];
        var myLatlng = new google.maps.LatLng(data.lat, data.lng);
        var marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            title: data.title
        })
        marker.set('id', i + 1);
        console.log(marker);
        marker.addListener('click', function() {
            handleClick(this)
        });

    }
}

function handleClick(marker) {
    var id = marker.id;
    $.ajax({
        url: '../getLevelInformation/',
        type: 'GET',
        data: {
            level_id: id
        },
        success: function(response) {

            $('#levelInfoTextField').html(response.content);

        }
    });
}