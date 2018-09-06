import React, { Component } from 'react';
import { Alert, View } from 'react-native';
import {
  Body,
  Button,
  Content,
  Container,
  Header,
  H2,
  Textarea,
  Title,
  H3
} from 'native-base';
import { withNavigation } from 'react-navigation';

import config from '../../config';
import deviceStorage from '../services/DeviceStorage';

import DefaultText from '../components/text/DefaultText';
import Header2 from '../components/text/Header2';
import ImportantText from '../components/text/ImportantText';


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
          body: JSON.stringify({ 'note': this.state.note })
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
            this.props.navigation.navigate('Home')
          })
          .catch(error => {
            this.setState({ error, loading: false });
            Alert.alert('Error:', error.toString());
          });
      });
  };



  render() {
    const rideItem = this.props.navigation.getParam('rideItem');
    const url = `${config.BACKEND_DOMAIN}/rides/${rideItem.id}/requests/`;
    const { departure, destination, date } = rideItem;
    return (
      <Container>
        <Header>
          <Body>
            <Title>Make a ride request</Title>
          </Body>
        </Header>
        <Content padder style={{ margin: 15 }}>
          <Body>
            <H3>Are you sure you want to make this ride request?</H3>
            <DefaultText>{'\n'}</DefaultText>
            <DefaultText>From: <ImportantText>{departure}</ImportantText></DefaultText>
            <DefaultText>To: <ImportantText>{destination}</ImportantText></DefaultText>
            <DefaultText>Departing on <ImportantText>{date}</ImportantText></DefaultText>
            <DefaultText>{'\n'}</DefaultText>
            <DefaultText>Write a note to driver. Only driver can see the note.</DefaultText>
            <DefaultText>{'\n'}</DefaultText>
            <Textarea rowSpan={5} bordered placeholder="Write note here... "
              onChangeText={(text) => this.setState({ note: text })}
              style={{ width: 200 }} />
            <DefaultText>{'\n'}</DefaultText>

          </Body>
          <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
            <Button block success
              onPress={() => this.MakeRideRequest(url)}>
              <DefaultText>Confirm</DefaultText>
            </Button>
            <Button block danger
              onPress={() => this.props.navigation.goBack()}>
              <DefaultText>Cancel</DefaultText>
            </Button>
          </View>
        </Content>
      </Container>
    );
  }
}

export default withNavigation(MakeRequestModal);
