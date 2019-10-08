
/*
Example cpp code for JSON build & parse
*/
#include<iostream>
#include <boost/property_tree/ptree.hpp>                                   
#include <boost/property_tree/json_parser.hpp>

#define MAX_ENTRIES 2
using namespace std;
namespace PT = boost::property_tree;

std::string json_serialize(void)
{
    PT::ptree mainData;
    PT::ptree Data;
    std::stringstream ss;
    std::string mainJSONStr;
    bool V = 1;
    for (int i = 0; i < MAX_ENTRIES ; i++) {
        PT::ptree child;
        PT::ptree tupl;
        PT::ptree tuple_array;
        PT::ptree passportData;
        std::string name = "Name";
        std::string address = "street";
        name.append(std::to_string(i+1));
        address.append(std::to_string(i+1));
        child.put("Name", name);
        child.put("Address", address);
        child.put("id", std::to_string(i+1));
        child.put("Enable", V);
        
        tupl.put("x", (i+1));
        tupl.put("y", (i+1));
        tupl.put("z", (i+1));
        tuple_array.push_back(std::make_pair("", tupl));
        tuple_array.push_back(std::make_pair("", tupl));
        child.push_back(std::make_pair("DataTupleArray", tuple_array));
        
        child.put("FavouriteColor", "red");
        child.put("Number", (i+1));
        
        passportData.put("HomeCountry", "UE");
        passportData.put("LivingCountry", "CA");
        child.push_back(std::make_pair("PassportData", passportData));

        child.put("CommentString", "NA");

        Data.push_back(std::make_pair("", child));
    }
    mainData.add_child("DataBase", Data);
    PT::write_json(ss, mainData);
    mainJSONStr = ss.str();
    return mainJSONStr;
}


void json_deserialize(std::string json_data)
{

    PT::ptree root;
    std::stringstream ss;
    ss << json_data;
    PT::read_json(ss, root);

    PT::ptree dataBase;
    dataBase = root.get_child("DataBase");
    cout << "DataBase" << "=" << endl;
    //iterate through each entry in the database
    for (PT::ptree::value_type &eEntry : dataBase) {
        // First represent tag and second is the data of that Tag
        for (PT::ptree::value_type &d : eEntry.second) {
            if (d.first == "PassportData") {
                cout << "   PassportData:" << endl;
                //Interate through each entry of PassportData
                for (PT::ptree::value_type &p: d.second) {
                    cout << "       " << p.first << "="<< p.second.data()<< endl;    
                }
            } else if (d.first == "DataTupleArray") {
                cout << "   " << d.first << endl;
                // iterate through each data elements of DataTupleArray
                for (PT::ptree::value_type &dt : d.second) {
                    // Interate through x,y,z of DataTupleArray
                    for (PT::ptree::value_type &a : dt.second) {
                        cout << "       " << a.first << "=" << a.second.data() << endl;
                    }
                }
            }
            cout << "   " << d.first << "=" << d.second.data() << endl;
            
        }
    }    

}

int main ()
{
    std::string serialized_json_data;
    serialized_json_data = json_serialize();
    json_deserialize(serialized_json_data);
    return 0;
}