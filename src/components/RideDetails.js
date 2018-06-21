import React, { Component } from "react";
import { Image, ImageBackground, View, StatusBar, FlatList } from "react-native";
import {
  Container,
  Header,
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



class RideDetails extends Component {

  constructor(props) {
    super(props);

  }

  render() {
    const { navigation } = this.props;
    const rideItem = navigation.getParam('rideItem', 'default value');  // add default value for parameter

    return (
      <Container>
        <Text>{rideItem}</Text>
        {/*
        <Header>
          <Left>
            <Button transparent>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>Ride details</Title>
          </Body>
        </Header>

        <Content>
          <Text>From: {rideItem.origin}</Text>
          <Text>To: {rideItem.destination}</Text>
          <Text>Departing on {rideItem.date} at {rideItem.departure}</Text>
          <Text>{rideItem.available_seats} seats available </Text>
          <Text>Estimated fuel cost {rideItem.est_fuel_price} euros</Text>

          <Title>Driver</Title>
          <View style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center' }} >
            <View style={{ flex: 1 }}>
              <Image
                style={{ width: 90, height: 90, borderRadius: 45 }}
                source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }}
              />
              <Text note>Rating {rideItem.driver.rating} {rideItem.driver.reviews}</Text>
            </View>
            <View style={{ flex: 2 }}>
              <Text>{rideItem.driver.name}</Text>
              <Text>Model: {rideItem.driver.car_register_plate}</Text>
              <Text>Register plate:{rideItem.car_model}</Text>
            </View>
          </View>

        </Content>

        <Button block>
            <Text>Join ride</Text>
          </Button>
        <Footer>
          <FooterTab>
            <Button vertical>
              <Icon name="apps" />
              <Text>Rides</Text>
            </Button>

            <Button vertical>
              <Icon name="person" />
              <Text>Account</Text>
            </Button>
          </FooterTab>
        </Footer>
          */}
      </Container>
    );
  }
}

export default RideDetails;
