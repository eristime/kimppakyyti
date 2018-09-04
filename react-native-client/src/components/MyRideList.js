import React, { Component } from 'react';
import { Alert, FlatList, View } from 'react-native';
import {
  Content,
  H3
} from 'native-base';

import RideItem from './RideItem';
import deviceStorage from '../services/DeviceStorage';
//import testData from  '../../data-dump';


class MyRideList extends Component {

  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      data: [],
      page: 1,
      seed: 1,
      error: null,
      refreshing: false,
      token: null
    };
  }

  componentDidMount() {
    this.makeRemoteRequest(this.props.url);
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

  makeRemoteRequest = (url, newRequest = false) => {
    /*
      param: newRequest: boolean. If true will start on a first page. 
    */

    if (newRequest) {
      this.setState({
        page: 1,
        seed: 1
      });
    }
    const { page } = this.state;

    this.setState({ loading: true });
    this.loadToken().
    then((token)=>{
      console.log('Token: ' + token);
      fetch(url, {
        headers: {
          authorization: 'Token ' + token
        }
      }).then(res => res.json())
        .then(res => {
          console.log(res);
          this.setState({
            data: page === 1 ? res.results : [...this.state.data, ...res.results],
            error: res.error || null,
            loading: false,
            refreshing: false
          });
        })
        .catch(error => {
          this.setState({ error, loading: false });
          //Alert.alert('Error:', error.toString());
        });
    });
  };


  handleLoadMore = () => {
    this.setState(
      {
        page: this.state.page + 1
      },
      () => {
        this.makeRemoteRequest();
      }
    );
  };

  renderEmpty = () => {
    return (
      <Content>
        <H3>{this.props.renderEmpty}</H3>
      </Content>
    );
  };

  render() {

    return (
      <FlatList
        data={this.state.data}
        renderItem={({ item }) => (
          <RideItem
            rideItem={item}
          />
        )}
        keyExtractor={item => item.id}
        ListFooterComponent={this.renderFooter}
        ListEmptyComponent={this.renderEmpty}
        onRefresh={this.handleRefresh}
        refreshing={this.state.refreshing}
        onEndReached={this.handleLoadMore}
      />
    );
  }
}

export default MyRideList;
