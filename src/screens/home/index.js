import React, { Component } from "react";
import { Image, ImageBackground, View, StatusBar, FlatList } from "react-native";
import {
  Container,
  Header,
  Card,
  CardItem,
  Drawer,
  ListItem,
  List,
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
  Title,
  Fab
} from "native-base";

import styles from "./styles";
import RideItem from '../../components/RideItem';
import AppHeader from "../../components/AppHeader";


const rides = [{
  id: 981203810928,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'  
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 9812038104448,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'  
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 1111111111111,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'  
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 2222222222222,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'  
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
}];


class Home extends Component {

  constructor(props) {
    super(props);
    this.state = {
      fabActive: false
    };
  }
  render() {

    return (
      <Container>
              
        <AppHeader />

        <Content >
          <List>
            <FlatList
              data={rides}
              renderItem={({ item }) => (
                <RideItem 
                  rideItem={item} 
                  
                />
              )}
              keyExtractor={item => item.id}
            />
          </List>
          
        </Content>
        <Fab
          active={this.state.fabActive}
          direction="up"
          containerStyle={{ bottom: 60 }}
          style={{ backgroundColor: '#5067FF' }}
          position="bottomRight"
          onPress={() => this.props.navigation.navigate('AddRide')}>
          <Icon name="md-add" />
        </Fab>
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

      </Container>
    );
  }
}

export default Home;
