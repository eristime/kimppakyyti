import React, { Component } from 'react';
import { Alert, FlatList, View } from 'react-native';
import {
  Body,
  Button,
  Container,
  Content,
  Left,
  Header,
  H3,
  Icon,
  Spinner,
  Tabs,
  Tab,
  Title,
  Text
} from 'native-base';

import styles from './styles';
//import RideItem from './RideItem';
import MyRideList from '../../components/MyRideList';
//import deviceStorage from '../../services/DeviceStorage';
//import testData from  '../../../data-dump';


class MyRides extends Component {

  constructor(props) {
    super(props);
  }

  /*
  componentDidMount() {
    let token = this.props.navigation.getParam(token, undefined);
    if (!token) {
      deviceStorage.loadToken()
      .then(
        this.makeRemoteRequest(`http://192.168.43.216:8000/me/rides_as_driver/`, token)
      );
    }
  }
  */

  render() {
    const token = this.props.navigation.getParam(token, undefined); // passed to child component
    return (
      <Container>
        <Header hasTabs>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>My Rides</Title>
          </Body>
        </Header>
        <Tabs locked>
          <Tab heading="Passenger">
          <Content>
            <MyRideList 
            url="http://192.168.43.216:8000/me/rides_as_passenger/"
            token={token}
            />
          </Content>
        
          </Tab>
          <Tab heading="Driver">
            <MyRideList 
            url="http://192.168.43.216:8000/me/rides_as_driver/"
            token={token}
            />
          </Tab>
        </Tabs>


      </Container>
    );
  }
}

export default MyRides;
