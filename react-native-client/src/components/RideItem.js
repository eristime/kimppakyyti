import React, { Component } from "react";
import { Image, View, TouchableOpacity } from "react-native";
import {
  ListItem,
  Text,
} from "native-base";
import { withNavigation } from 'react-navigation';


const RideItem = (props) => {
  
    return (
      
      <ListItem 
      button onPress={() => props.navigation.navigate('RideDetails', {rideItem:'testi', rideItem: props.rideItem})}
      containerStyle={{ borderBottomWidth: 0 }}
      >
      
        <View 
        style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center'}}>
          <View style={{ flex: 1 }}>
            <Image
              style={{ width: 90, height: 90, borderRadius: 45 }}
              source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }}
            />
            <Text note>Rating {props.rideItem.driver.rating} {props.rideItem.driver.reviews}</Text>
          </View>
          <View style={{ flex: 2 }}>
            <Text>Driver: {props.rideItem.driver}</Text>
            <Text>{props.rideItem.departure}->{props.rideItem.destination}</Text>
            {/*}<Text>{props.rideItem.date}->{props.rideItem.departure}</Text>*/}
            <Text>{props.rideItem.available_seats} seats; fuel {props.rideItem.estimated_fuel_cost} e</Text>
          </View>

        </View>
        
      </ListItem>

    );

};

export default withNavigation(RideItem);
