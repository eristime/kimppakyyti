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

import styles from "./styles";


const rides = [
  {
    driver: 'driver_1',
    destination: 'Oulu',
    origin: 'Rovaniemi',
    available_seats: 3,
    date: '11-05-2018',
    departure_time: '11:44',
    est_fuel_price: 20.55
  },
  {
    driver: 'driver_2',
    destination: 'Oulu',
    origin: 'Rovaniemi',
    available_seats: 3,
    date: '11-05-2018',
    departure_time: '11:44',
    est_fuel_price: 20.55
  },

];

class Home extends Component {
  render() {
    return (
      <Container>
        <Header span>
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
          <ListItem>
            <Card>
              <CardItem>
                <Left>
                  <Thumbnail source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }} />
                  <Body>
                    <Text>Driver name</Text>
                    <Text note>wubbalubba</Text>
                  </Body>
                </Left>
              </CardItem>
              <CardItem cardBody>
                <Image source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }} style={{ height: 200, width: null, flex: 1 }} />
              </CardItem>
              <CardItem>
                <Left>
                  <Button transparent>
                    <Icon active name="navigate" />
                    <Text>12 Likes</Text>
                  </Button>
                </Left>
                <Body>
                  <Button transparent>
                    <Icon active name="chatbubbles" />
                    <Text>4 Comments</Text>
                  </Button>
                </Body>
                <Right>
                  <Text>11h ago</Text>
                </Right>
              </CardItem>
            </Card>
          </ListItem>
          <ListItem>
            <Card>
              <CardItem>
                <Left>
                  <Thumbnail source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }} />
                  <Body>
                    <Text>Second driver</Text>
                    <Text note>wubbalubba</Text>
                  </Body>
                </Left>
              </CardItem>
              <CardItem cardBody>
                <Image source={{ uri: 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/300px-Original_Doge_meme.jpg' }} style={{ height: 200, width: null, flex: 1 }} />
              </CardItem>
              <CardItem>
                <Left>
                  <Button transparent>
                    <Icon active name="navigate" />
                    <Text>12 Likes</Text>
                  </Button>
                </Left>
                <Body>
                  <Button transparent>
                    <Icon active name="chatbubbles" />
                    <Text>4 Comments</Text>
                  </Button>
                </Body>
                <Right>
                  <Text>11h ago</Text>
                </Right>
              </CardItem>
            </Card>
          </ListItem>

        </Content>
        <Footer>
          <FooterTab>
            <Button vertical>
              <Icon name="apps" />
              <Text>Rides</Text>
            </Button>
            <Button vertical>
              <Icon name="camera" />
              <Text>Passengers</Text>
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
