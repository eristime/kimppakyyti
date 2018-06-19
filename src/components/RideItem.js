import React, { Component } from "react";
import { Image, ImageBackground, View, StatusBar } from "react-native";
import {
  Container,
  Header,
  Card,
  CardItem,
  Thumbnail,
  ListItem,
  Content,
  Footer,
  FooterTab,
  Button,
  Icon,
  Text,
  Left,
  Body,
  Right,
  Item,
  Input,
  Title
} from "native-base";
import { Col, Row, Grid } from 'react-native-easy-grid';



const RideItem = (props) => {

    return (
      <ListItem>
        <View style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center' }} >
          <View style={{ flex: 1 }}>
            <Image
              style={{ width: 90, height: 90, borderRadius: 45 }}
              source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }}
            />
            <Text note>Rating {props.rideItem.driver.rating} {props.rideItem.driver.reviews}</Text>
          </View>
          <View style={{ flex: 2 }}>
            <Text>{props.rideItem.driver.name}</Text>
            <Text>{props.rideItem.origin}->{props.rideItem.destination}</Text>
            <Text>{props.rideItem.date}->{props.rideItem.departure}</Text>
            <Text>{props.rideItem.available_seats} seats; fuel {props.rideItem.est_fuel_price} e</Text>
          </View>

        </View>
      </ListItem>

    );

};

export default RideItem;
