
/*
Example java script for JSON build & parse
*/
var jsonData;
jsonData = json_serialize();

json_deserialize(jsonData);

function json_serialize(){
    var data = {}
    data['DataBase'] = []
    for (i = 0; i < 2 ; i++) {
        var entry = {}
        entry['Name'] = "Name" + (i+1).toString();
        entry['Address'] = "street" + (i+1).toString();
        entry['id'] = (i+1).toString();
        entry['Enable'] = true;
        entry['FavouriteColor'] = "red";
        entry['Number'] = i+1;
        entry['CommentString'] = "NA";
        var ppData = {}
        ppData['HomeCountry'] = "UE";
        ppData['LivingCountry'] = "CA";     
        entry['PassportData'] = ppData;
        var DataTupleArry = []
        for (j = 0; j < 2; j++) {
            var xData = {}
            xData.x = i+1;
            xData.y = i+1;
            xData.z = i+1;
            DataTupleArry.push(xData);
        }
        entry['DataTupleArray'] = DataTupleArry;
        data['DataBase'].push(entry);
    }
    console.log("Serialized JSON String .....");
    console.log(JSON.stringify(data));
    // Return JSON string created from JSON object (Use of JSON.stringify)
    return JSON.stringify(data);
}

function json_deserialize(json_string) {
    var messageData = JSON.parse(json_string);
    var DataBase = messageData['DataBase'];
    for (i=0; i < DataBase.length; i++) {
            var eEntry = DataBase[i];
            console.log("Name" + " = " + eEntry['Name']);
            console.log("id" + " = " + eEntry['id']);
            console.log("Address" + " = " + eEntry['Address']);
            console.log("Number" + " = " + eEntry['Number']);
            console.log("Enable" + " = " + eEntry['Enable']);
            console.log("CommentString" + " = " + eEntry['CommentString']);
            var dta = eEntry['DataTupleArray'];
            for (j = 0; j < dta.length; j++) {
                console.log("   x " + "[" + j + "] = "  + dta[j].x);
                console.log("   y " + "[" + j + "] = "  + dta[j].y);
                console.log("   z " + "[" + j + "] = "  + dta[j].z);
            }
            
    }

}
