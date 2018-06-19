import React, { Component } from "react";
import { Image, ImageBackground, View, StatusBar, FlatList } from "react-native";
import {
  Container,
  Header,
  Card,
  CardItem,
  Thumbnail,
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


const rides = [{
  id: 981203810928,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200
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
    profile_url: 'xxxxx'
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
    profile_url: 'xxxxx'
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
    profile_url: 'xxxxx'
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
      fabActive: true
    };
  }
  render() {

    return (
      <Container>
        <Header>
          <Left>
            <View>
              <Title>Kimppakyyti</Title>
            </View>
            {/*
              <View>
                <Item rounded>
                  <Input placeholder="From" />
                </Item>
                <Item rounded>
                  <Input placeholder="To" />
                </Item>
                <Item regular>
                  <Input placeholder="Date" />
                </Item>
              </View>
              */}
          </Left>

        </Header>
        <Content >
          <List>
            <FlatList
              data={rides}
              renderItem={({ item }) => (
                <RideItem rideItem={item} />
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
          onPress={() => this.setState({ fabActive: !this.state.fabActive })}>
          <Icon name="share" />
          <Button style={{ backgroundColor: '#34A34F' }}>
            <Icon name="logo-whatsapp" />
          </Button>
          <Button style={{ backgroundColor: '#3B5998' }}>
            <Icon name="logo-facebook" />
          </Button>
          <Button disabled style={{ backgroundColor: '#DD5144' }}>
            <Icon name="mail" />
          </Button>
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
