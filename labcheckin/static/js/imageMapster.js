var img = $('LabChart');
img.mapster(
    {
        fillOpacity: 0.4,
        fillColor: "d42e16",
        stroke: true,
        strokeColor: "3320FF",
        strokeOpacity: 0.8,
        strokeWidth: 4,
        singleSelect: true,
        mapKey: 'title',
        listKey: 'title',
        onClick: function (e) {
            alert("Works")
        }
    });