import React from 'react';
import { Root } from 'native-base';
import { StackNavigator } from 'react-navigation';


import Home from './screens/home/';
import Login from './screens/login/';
import RideDetails from './screens/ridedetails';
import AddRide from './screens/add-ride';
import MyRides from './screens/my-rides';


const AppNavigator = StackNavigator(
  {
    Login: { screen: Login},
    Home: { screen: Home},
    MyRides: { screen: MyRides},
    RideDetails: { screen: RideDetails},
    AddRide: {screen: AddRide}
  },
  {
    initialRouteName: 'Home',
    headerMode: 'none'
  }
);

export default () =>
  <Root>
    <AppNavigator />
  </Root>;
