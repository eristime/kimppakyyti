import React, { Component } from 'react';
import { Alert, View } from 'react-native';
import {
  Body,
  Button,
  Content,
  Container,
  Header,
  H2,
  Text,
  Textarea,
  Title,
  H3
} from 'native-base';
import { withNavigation } from 'react-navigation';

import deviceStorage from '../services/DeviceStorage';


class MakeRequestModal extends Component {

  constructor(props) {
    super(props);
    this.state = {
      token: null,
      loading: false,
      note: ''
    };
  }

  componentDidMount() {
    this.loadToken();
  }


  loadToken = async () => {
    /*
    Check if token in state, if not return it from async storage.
    */
    const token = this.state.token;
    let loadedToken = '';
    //Alert.alert('token from my-rides view:', token);
    if (token === false || token === undefined || token === null) {
      loadedToken = await deviceStorage.loadToken();
      //console.log('loadedToken from deviceStorage:', loadedToken);
      //.then((tokenFromStorage) => {
      //  Alert.alert('token from async storage:', tokenFromStorage);
      //  this.setState({ token: tokenFromStorage });
      //  Promise.resolve(tokenFromStorage);
      //})
      //.catch((error) => {
      //  Alert.alert('Error:', error.toString());
      //});
    } else {
      this.setState({ token: token });
      loadedToken = token;
    }
    //console.log('loadedToken:', loadedToken);
    return loadedToken;
  }

  MakeRideRequest = (url) => {

    this.setState({ loading: true });
    this.loadToken().
      then((token) => {
        console.log('Token: ' + token);
        fetch(url, {
          method: 'post',
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
            authorization: 'Token ' + token
          },
          body: JSON.stringify({'note': this.state.note})
        }).then(res => res.json())
          .then(res => {
            console.log(res);
            this.setState({
              data: res.results,
              error: res.error || null,
              loading: false
            });
            console.log('post request:', res);
            Alert.alert('Ride request successfully added');
            //this.props.navigation.navigate('Home')
          })
          .catch(error => {
            this.setState({ error, loading: false });
            Alert.alert('Error:', error.toString());
          });
      });
  };



  render() {
    const rideItem = this.props.navigation.getParam('rideItem');
    const url = `http://192.168.1.103:8000/rides/${rideItem.id}/requests/`;
    //Alert.alert('url:', url);
    return (
      <Container>
        <Header>
          <Body>
            <Title>Confirm Ride</Title>
          </Body>
        </Header>
        <Content padder style={{margin: 15}}>
          <Body>
            <H3>Are you sure you want to make this ride request?</H3>
            <Text>{'\n'}</Text>
            <Text>From: {rideItem.departure}</Text>
            <Text>To: {rideItem.destination}</Text>
            <Text>On {rideItem.date}</Text>
            <Text>{'\n'}</Text>
            <Text>Write a note to driver. Only driver can see the note.</Text>
            <Text>{'\n'}</Text>
            <Textarea rowSpan={5} bordered placeholder="Write note here... "
              onChangeText={(text) => this.setState({ note: text })}
              style={{width:200}} />
            <Text>{'\n'}</Text>
          
          </Body>
          <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
            <Button block success
              onPress={() => this.MakeRideRequest(url)}>
              <Text>Confirm</Text>
            </Button>
            <Button block danger
              onPress={() => this.props.navigation.goBack()}>
              <Text>Cancel</Text>
            </Button>
          </View>
        </Content>
      </Container>
    );
  }
}

export default withNavigation(MakeRequestModal);
