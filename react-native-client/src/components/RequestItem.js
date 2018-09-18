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
//import Text from './text/Text';




const RequestItem = (props) => {
  const { departure, destination, available_seats, estimated_fuel_cost, date } = props.requestItem.ride;
  let { first_name, last_name, driver_rating, driver_review_count, photo } = props.requestItem.ride.driver.profile;
  let { note } = props.requestItem.note;
  // default values
  first_name = first_name || 'unknown';
  last_name = last_name || 'unknown';
  photo = photo || 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg';
  driver_rating = driver_rating || 4.00;
  driver_review_count = driver_review_count || 15;
  note = note || '---';
  const time = '14:53';

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
          <Button danger small>
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
            <Text>{available_seats} seats; fuel {estimated_fuel_cost} euros</Text>
            <Text>{time}</Text>
          </View>
        </View>
        <View
          style={{ flex: 1, justifyContent: 'center', flexDirection: 'row' }}
        >
          <Text style={{flex: 1, flexWrap: 'wrap'}} note>'''{note}'''</Text>
        </View>
      </View>

    </ListItem>

  );

};

export default withNavigation(RequestItem);
