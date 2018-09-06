import React from 'react';
import { Root } from 'native-base';
import { createStackNavigator } from 'react-navigation';


import Home from './screens/home/';
import Login from './screens/login/';
import RideDetails from './screens/ridedetails';
import AddRide from './screens/add-ride';
import MyRides from './screens/my-rides';
import MakeRequestModal from './screens/MakeRequestModal';


const MainStack = createStackNavigator(
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

const RootStack = createStackNavigator(
  {
    Main: {
      screen: MainStack,
    },
    MakeRequestModal: {
      screen: MakeRequestModal,
    },
  },
  {
    mode: 'card',
    headerMode: 'none',
  }
);

export default () =>
  <Root>
    <RootStack />
  </Root>;
