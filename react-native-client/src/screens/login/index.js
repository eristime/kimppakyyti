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
console.log();


class Login extends Component {

  /*
  logIn = async () => {
    const { type, token } = await Expo.Facebook.logInWithReadPermissionsAsync(keys.FACEBOOK_APP_ID, {
        permissions: ['public_profile'],
      });
      
      if (type === 'cancel') {
        Alert.alert(
          'Log in error!'
        );
      }
    
      if (type === 'success') {
      // Get the user's name using Facebook's Graph API
      const response = await fetch(
        `https://graph.facebook.com/me?access_token=${token}`);
      Alert.alert(
        'Logged in!',
        `Hi ${(await response.json()).name}!`,
      );
    } else {
      // handle errors
    }
  };
  */
  
 _handlePressAsync = async () => {
  let redirectUrl = AuthSession.getRedirectUrl();

  // You need to add this url to your authorized redirect urls on your Facebook app
  console.log({ redirectUrl });

  // NOTICE: Please do not actually request the token on the client (see:
  // response_type=token in the authUrl), it is not secure. Request a code
  // instead, and use this flow:
  // https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/#confirm
  // The code here is simplified for the sake of demonstration. If you are
  // just prototyping then you don't need to concern yourself with this and
  // can copy this example, but be aware that this is not safe in production.
  /*
  let result = await AuthSession.startAsync({
    authUrl:
      `https://www.facebook.com/v2.8/dialog/oauth?response_type=code` +
      `&client_id=${keys.FACEBOOK_APP_ID}` +
      `&redirect_uri=${encodeURIComponent(redirectUrl)}`,
  });

  if (result.type !== 'success') {
    alert('Uh oh, something went wrong');
    return;
  }
  // send message to confirm login
  */



}


  _handleTestLoginPressAsync = async () => {
  
      //this.setState({ error: '', loading: true });
      //const url = `http://${config.DESKTOP_IP}:8000/login/`;
      
      const url = `http://192.168.1.103:8000/login/`;
      //console.log(url)
      axios.post(url,{
          username: 'matkustaja',
          password: 'matkustaja123',
      })
      .then((response) => {
         // Handle the JWT response here
         console.log('response:', response);
         console.log('token:', response.data.token);
      })
      .catch((error) => {
         console.log(error);
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
          <H1>Login</H1>
          <Button
            primary
            style={{ alignSelf: "center" }}
            onPress={()=>this._handlePressAsync()}
          >
            <Text>Facebook</Text>
          </Button>
          <Button
            primary
            style={{ alignSelf: "center" }}
            onPress={()=>this._handleTestLoginPressAsync()}
          >
            <Text>Test</Text>
          </Button>


          {/*
        <Button
          style={{ alignSelf: "center" }}
          onPress={() => this.props.navigation.navigate('Home', { user_id: 12345, usename: 'test_user' })}
        >
          <Text>Test user</Text>
        </Button>
        */}
        </Content>

        {/*
        <Footer>
          <FooterTab>
            <Button vertical
              onPress={() => this.props.navigation.navigate('Home')}
            >
              <Icon name='apps' />
              <Text>Rides</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('Login')}
            >
              <Icon name='person' />
              <Text>Account</Text>
            </Button>
          </FooterTab>
        </Footer>
        */}
      </Container>
    );
  }
}

export default Login;
