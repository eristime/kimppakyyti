import React, { Component } from "react";
import { ImageBackground, View, StatusBar } from "react-native";
import { Container, Button, H1, Text } from "native-base";

import styles from "./styles";


class Login extends Component {
  render() {
    return (
      <Container>
        <StatusBar barStyle="light-content" />
        
          <H1>Login</H1>
            <Button
              style={{ backgroundColor: "red", alignSelf: "center" }}
            >
              <Text>Google</Text>
            </Button>
            <Button
              style={{ backgroundColor: "blue", alignSelf: "center" }}
            >
              <Text>Facebook</Text>
            </Button>
            
            <Button
              style={{alignSelf: "center" }}
              onPress={() => this.props.navigation.navigate('Home', {user_id: 12345, usename: 'test_user'})}
            >
              <Text>Test user</Text>
            </Button>


      </Container>
    );
  }
}

export default Login;
