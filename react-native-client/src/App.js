import React from 'react';
import { Root } from 'native-base';
import { createStackNavigator } from 'react-navigation';


import Home from './screens/home/';
import Login from './screens/login/';
import RideDetails from './screens/ridedetails';
import AddRide from './screens/add-ride';
import MyRides from './screens/my-rides';
import Passenger from './screens/passenger';
import Driver from './screens/driver';
import MakeRequestModal from './screens/MakeRequestModal';


const MainStack = createStackNavigator(
  {
    Login: { screen: Login},
    Home: { screen: Home},
    MyRides: { screen: MyRides},
    RideDetails: { screen: RideDetails},
    AddRide: {screen: AddRide},
    Passenger: {screen: Passenger},
    Driver: {screen: Driver},
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
