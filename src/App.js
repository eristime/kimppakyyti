import React from "react";
import { Root } from "native-base";
import { StackNavigator, DrawerNavigator } from "react-navigation";


import Home from "./screens/home/";
import Login from "./screens/login/";
import SideBar from "./screens/sidebar";
import RideDetails from './screens/ridedetails';
import AddRide from './screens/add-ride'


/*
const Drawer = DrawerNavigator(
  {
    Home: { screen: Home },
    NHRadio: { screen: NHRadio }

  },
  {
    initialRouteName: "Home",
    contentOptions: {
      activeTintColor: "#e91e63"
    },
    contentComponent: props => <SideBar {...props} />
  }
);
*/

const AppNavigator = StackNavigator(
  {
    //Drawer: { screen: Drawer },
    Login: { screen: Login},
    Home: { screen: Home},
    RideDetails: { screen: RideDetails},
    AddRide: {screen: AddRide}
  },
  {
    initialRouteName: "Login",
    headerMode: "none"
  }
);

export default () =>
  <Root>
    <AppNavigator />
  </Root>;
