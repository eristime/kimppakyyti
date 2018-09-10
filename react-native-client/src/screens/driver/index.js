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
import config from '../../../config.js';
//import deviceStorage from '../../services/DeviceStorage';
//import testData from  '../../../data-dump';


class Driver extends Component {

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
    //Alert.alert('token in my-rides view:', token);
    return (
      <Container>
        <Header hasTabs>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>Rides as driver</Title>
          </Body>
        </Header>
        <Tabs locked>
          <Tab heading="Ongoing rides">
            <MyRideList 
            url={`${config.BACKEND_DOMAIN}/me/rides_as_driver/`}
            token={token}
            renderEmpty="You have no ongoing rides as driver."
            />
          </Tab>
          <Tab heading="Pending ride requests">
          <Content>
            {/*
            <MyRideList
            url={`${config.BACKEND_DOMAIN}/me/rides_as_passenger/`}
            token={token}
            renderEmpty="You have no pending ride requests."
            />
            */}
          </Content>
          </Tab>
        </Tabs>


      </Container>
    );
  }
}

export default Driver;
