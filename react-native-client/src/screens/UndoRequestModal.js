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


class UndoRequestModal extends Component {

  constructor(props) {
    super(props);
    this.state = {
      token: null,
      loading: false
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

  undoRequest = (url) => {

    this.setState({ loading: true });
    this.loadToken().
      then((token) => {
        console.log('Token: ' + token);
        fetch(url, {
          method: 'DELETE',
          headers: {
            authorization: 'Token ' + token
          }
        }).then((res) => {
          console.log(res);
          if (res.status === 204) {
            Alert.alert('Ride request undone.');
          } else {
            Alert.alert('Problem with adding a request', 'status: ' + res.status.toString());
          }
          this.props.navigation.navigate('Home');
          return res.json();
        }).then(res => {
            this.setState({
              data: res.results,
              error: res.error || null,
              loading: false
            });
          })
          .catch(error => {
            this.setState({ error, loading: false });
            //Alert.alert('Error:', error.toString());
          });
      });
  };


  render() {
    const requestItem = this.props.navigation.getParam('requestItem');
    const url = `${config.BACKEND_DOMAIN}/rides/${requestItem.ride.id}/requests/${requestItem.id}/`;
    //console.log('urlo:', url);

    return (
      <Container>
        <Content padder style={{ margin: 15 }}>
          <Body>
            <H3>Are you sure you want to undo this ride request?</H3>
            <DefaultText>{'\n'}</DefaultText>
            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
              <Button block danger
                onPress={() => this.props.navigation.goBack()}>
                <DefaultText>Cancel</DefaultText>
              </Button>
              <Button block success
                onPress={() => this.undoRequest(url)}>
                <DefaultText>Confirm</DefaultText>
              </Button>
            </View>
          </Body>
        </Content>
      </Container>
    );
  }
}

export default UndoRequestModal;
