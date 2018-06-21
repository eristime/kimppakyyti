import React, { Component } from "react";
import { Image, View, Modal } from "react-native";
import {
  Button,
  Card,
  Container,
  Header,
  Content,
  Footer,
  FooterTab,
  H2,
  Icon,
  Text,
  Left,
  Body,
  Title
} from "native-base";
import { MapView } from 'expo';

const markers = [{
  latitude: 37.78825,
  longitude: -122.4324,
  title: 'Rovaniemi',
  description: ''
},
{
  latitude: 37.78825,
  longitude: -122.4330,
  title: 'Oulu',
  description: ''
}];

class RideDetails extends Component {

  constructor(props) {
    super(props);

  }

  state = {
    modalVisible: false,
  };

  setModalVisible(visible) {
    this.setState({ modalVisible: visible });
  }


  render() {
    const { navigation } = this.props;
    const rideItem = navigation.getParam('rideItem', {});  //TODO: add default value for parameter

    return (
      <Container>

        <Header>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
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

          <H2>Driver</H2>
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
          <MapView
            style={{ height: 200 }}
            initialRegion={{
              latitude: 37.78825,
              longitude: -122.4324,
              latitudeDelta: 0.0922,
              longitudeDelta: 0.0421,
            }}
          />

          {markers.map((marker, index) => {
            const coords = {
              latitude: marker.latitude,
              longitude: marker.longitude,
            };

            return (
              <MapView.Marker
                key={coords.latitude + marker.longitude}
                coordinate={coords}
                title={marker.title}
              />
            );
          })}

        </Content>

        <Button block primary
          onPress={() => {
            this.setModalVisible(!this.state.modalVisible)
          }}>
          <Text>Join ride</Text>
        </Button>

        <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => { alert("Modal has been closed.") }}
        >
          <Container>
            <Header>
              <Left>
                <Button transparent onPress={() => this.setModalVisible(!this.state.modalVisible)}>
                  <Icon name='arrow-back' />
                </Button>
              </Left>
              <Body>
                <Title>Confirm Ride</Title>
              </Body>
            </Header>

            <Text>From: {rideItem.origin}</Text>
            <Text>To: {rideItem.destination}</Text>
            <Text>Departing on {rideItem.date} at {rideItem.departure}</Text>
            <Text>{rideItem.available_seats} seats available </Text>
            <Text>Estimated fuel cost {rideItem.est_fuel_price} euros</Text>
            
            <Button block success>
              <Text>Confirm</Text>
            </Button>
          </Container>

        </Modal>

      </Container>
    );
  }
}

export default RideDetails;
