import React, { Component } from 'react';
import { Image, View, Modal } from 'react-native';
import {
  Body,
  Button,
  Container,
  Header,
  Content,
  Icon,
  Left,
  List,
  ListItem,
  Text,
  Title
} from 'native-base';
import styles from './styles';
import DefaultText from '../../components/text/DefaultText';
import Header2 from '../../components/text/Header2';
import ImportantText from '../../components/text/ImportantText';

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
                <Header2>Ride</Header2>
                <DefaultText>From: <ImportantText>{departure}</ImportantText></DefaultText>
                <DefaultText>To: <ImportantText>{destination}</ImportantText></DefaultText>
                <DefaultText>Departing on <ImportantText>{date}</ImportantText></DefaultText>
                <DefaultText>{available_seats} / {total_seat_count} seats available</DefaultText>
                <DefaultText>Estimated fuel cost {estimated_fuel_cost} euros</DefaultText>
              </Body>

            </ListItem>

            <ListItem>
              <Body>
              <Header2>Driver</Header2>
              <View style={{ flex: 1, justifyContent: 'space-between', flexDirection: 'row', alignItems: 'center' }}>
                <Image
                  style={{ width: 90, height: 90, borderRadius: 45 }}
                  source={{ uri: photo }}
                />
                <View>
                  <DefaultText>{first_name} {last_name}</DefaultText>
                  <DefaultText>Rating: {driver_rating} with {driver_review_count} reviews </DefaultText>
                </View>

              </View>
              </Body>
            </ListItem>

            <ListItem last>
              
              <Body>
              <Header2>Car</Header2>
              <DefaultText>Model: {model} </DefaultText>
              <DefaultText>Register plate: {register_plate}</DefaultText>
              </Body>
              
            </ListItem>
          </List>
        </Content>
        <Button block success
          button onPress={() => this.props.navigation.navigate('MakeRequestModal', { rideItem: rideItem })}
        >
          <DefaultText>Make a ride request</DefaultText>
        </Button>

      </Container>
    );
  }
}

export default RideDetails;
