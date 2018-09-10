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
import RequestList from '../../components/RequestList';
import config from '../../../config.js';
//import deviceStorage from '../../services/DeviceStorage';
//import testData from  '../../../data-dump';


class Passenger extends Component {

  constructor(props) {
    super(props);
  }


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
            <Title>Rides as passenger</Title>
          </Body>
        </Header>
        <Tabs locked>
          <Tab heading="Ongoig rides">
          <Content>
            <MyRideList
            url={`${config.BACKEND_DOMAIN}/me/rides_as_passenger/`}
            token={token}
            renderEmpty="You have no ongoing rides as passenger yet."
            />
          </Content>
        
          </Tab>
          <Tab heading="Ride requests">
            <RequestList 
            url={`${config.BACKEND_DOMAIN}/me/requests/`}
            token={token}
            renderEmpty="You haven't made any ride requests yet."
            />
          </Tab>
        </Tabs>


      </Container>
    );
  }
}

export default Passenger;
