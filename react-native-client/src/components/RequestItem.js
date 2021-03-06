import React from 'react';
import { Image, View } from 'react-native';
import {
  Body,
  Button,
  H3,
  Icon,
  Left,
  ListItem,
  Text
} from 'native-base';
import { withNavigation } from 'react-navigation';
import { capitalizeFirstLetter } from '../services/utils';


const RequestItem = (props) => {
  let { departure, destination, available_seats, estimated_fuel_cost, date, time } = props.requestItem.ride;
  let { first_name, last_name, driver_rating, driver_review_count, photo } = props.requestItem.ride.driver.profile;
  let { note } = props.requestItem;
  
  departure = capitalizeFirstLetter(departure);
  destination = capitalizeFirstLetter(destination);
  // default values
  first_name = first_name || 'unknown';
  last_name = last_name || 'unknown';
  photo = photo || 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg';
  driver_rating = driver_rating || 4.00;
  driver_review_count = driver_review_count || 15;
  note = note || '---';
  time = time || '17:53';
  time = time.substr(0,5); // hack to display time properly

  //console.log('props.requestItem:', props.requestItem)

  return (

    <ListItem
      button onPress={() => props.navigation.navigate('RideDetails', { rideItem: props.requestItem.ride })}
      containerStyle={{ borderBottomWidth: 0 }}
    >

      <View
        style={{ flex: 1, justifyContent: 'center' }}>

        <View
          style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-between' }} >
          <H3>Request for {date}</H3>
          <Button danger small
          onPress={() => props.navigation.navigate('UndoRequestModal', { requestItem: props.requestItem })}
          >
            <Text>Undo</Text>
          </Button>
        </View>

        <View
          style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center' }}>
          <View style={{ flex: 1 }}>
            <Image
              style={{ width: 90, height: 90, borderRadius: 45 }}
              source={{ uri: photo }}
            />
            <Text note>Rating {driver_rating} ({driver_review_count})</Text>
          </View>
          <View style={{ flex: 2 }}>
            <Text>{first_name} {last_name}</Text>
            <Text>{departure}->{destination}</Text>
            <Text>Leaves at: {time}</Text>
            <Text>{available_seats} seats; fuel {estimated_fuel_cost} euros</Text>
          </View>
        </View>
        
        <View
          style={{ flex: 1, justifyContent: 'center', flexDirection: 'row' }}
        >
          <Text>Your note: </Text>
          <Text style={{flex: 1, flexWrap: 'wrap'}} note>'''{note}'''</Text>
        </View>
        
      </View>

    </ListItem>

  );

};

export default withNavigation(RequestItem);
