import React, { Component } from "react";
import { Alert } from "react-native";
import {
  Button,
  Body,
  Container,
  Footer,
  FooterTab,
  Header,
  Icon,
  Left,
  H1,
  Text,
  Title,
  Content
} from "native-base";
import { Expo, AuthSession } from 'expo';
import axios from 'axios';
import styles from "./styles";
import { config } from '../../../config';
import deviceStorage from '../../services/DeviceStorage';

class Login extends Component {

  _handleTestLoginPressAsync = async () => {
      const url = `http://192.168.1.103:8000/login/`;
      console.log(url)
      axios.post(url,{
          username: 'matkustaja',
          password: 'matkustaja123',
      })
      .then((response) => {
         // Handle the JWT response here
         console.log('response:', response);
         console.log('token:', response.data.token);
         deviceStorage.saveKey('token', response.data.token);
         Alert('Now logged in. Token:', response.data.token);
         this.props.navigation.navigate('Home', { token: response.data.token})
      })
      .catch((error) => {
        Alert('Error:', error);
      });
    
  }


  render() {
    return (
      <Container>
        <Header>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>Login</Title>
          </Body>
        </Header>

        {/*<StatusBar barStyle="light-content" />*/}
        <Content>
          <Button
            primary
            style={{ alignSelf: "center" }}
          >
            <Text>Facebook</Text>
          </Button>
          <H1>  </H1>
          <Button
            primary
            style={{ alignSelf: "center" }}
            onPress={() => this._handleTestLoginPressAsync()}    
          >
            <Text>Test</Text>
          </Button>

        </Content>
      </Container>
    );
  }
}

export default Login;
