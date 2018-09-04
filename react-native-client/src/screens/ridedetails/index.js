import React, { Component } from 'react';
import { Image, View, Modal } from 'react-native';
import {
  Body,
  Button,
  Container,
  Header,
  Content,
  H2,
  Icon,
  Left,
  List,
  ListItem,
  Text,
  Title
} from 'native-base';
import styles from './styles';

class RideDetails extends Component {

  constructor(props) {
    super(props);
    this.state = {
      modalVisible: false,
    };
  }

  setModalVisible(visible) {
    this.setState({ modalVisible: visible });
  }


  render() {
    const { navigation } = this.props;
    const rideItem = navigation.getParam('rideItem');
    const { date, departure, destination, available_seats, estimated_fuel_cost, total_seat_count } = rideItem;
    let { first_name, last_name, driver_rating, driver_review_count, photo } = rideItem.driver.profile;
    let { register_plate, model } = rideItem.car;

    // default values
    first_name = first_name || 'unknown';
    last_name = last_name || 'unknown';
    photo = photo || 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg';
    driver_rating = driver_rating || 4.00;
    driver_review_count = driver_review_count || 0;

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

        <Content >
          <List>
            <ListItem first>
              <Body>
                <H2 style={styles.heading}>Ride</H2>
                <Text>From: {departure}</Text>
                <Text>To: {destination}</Text>
                <Text>Departing on {date}</Text>
                <Text>{available_seats} / {total_seat_count} seats available</Text>
                <Text>Estimated fuel cost {estimated_fuel_cost} euros</Text>
              </Body>

            </ListItem>

            <ListItem>
              <Body>
              <H2 >Driver</H2>
              <View style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center' }}>
                <Image
                  style={{ width: 90, height: 90, borderRadius: 45 }}
                  source={{ uri: photo }}
                />
                <View>
                  <Text style={styles.text}>{first_name} {last_name}</Text>
                  <Text>Rating: {driver_rating} with {driver_review_count} reviews </Text>
                </View>

              </View>
              </Body>
            </ListItem>

            <ListItem last>
              
              <Body>
              <H2 style={styles.heading}>Car</H2>
              <Text>Model: {model} </Text>
              <Text>Register plate: {register_plate}</Text>
              </Body>
              
            </ListItem>
          </List>
        </Content>
        <Button block success
          onPress={() => { this.setModalVisible(!this.state.modalVisible) }}
        >
          <Text>Make a ride request</Text>
        </Button>

        {/*TODO: style modal page*/}
        <Modal
          animationType="slide"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => { alert("Modal has been closed.") }}
        >
          <Container>
            <Header>
              <Body>
                <Title>Confirm Ride</Title>
              </Body>
            </Header>

            <Text>From: {rideItem.origin}</Text>
            <Text>To: {rideItem.destination}</Text>
            <Text>Departing on {rideItem.date} at {rideItem.departure}</Text>
            <Text>{rideItem.available_seats} seats available </Text>
            <Text>Estimated fuel cost {rideItem.est_fuel_price} &euro</Text>



            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
              <Button block success>

                {/*TODO: Add a user request to ride*/}
                <Text>Confirm</Text>
              </Button>
              <Button block danger
                onPress={() => {
                  this.setModalVisible(!this.state.modalVisible)
                }}>
                <Text>Cancel</Text>
              </Button>
            </View>
          </Container>

        </Modal>

      </Container>
    );
  }
}

export default RideDetails;
