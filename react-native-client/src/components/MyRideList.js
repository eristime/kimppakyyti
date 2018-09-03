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
      refreshing: false
    };
  }

  componentDidMount() {
    const token = this.props.token;
    Alert.alert('token from my-rides view:', token);
    if (token === false || token === undefined) {
      deviceStorage.loadToken()
      .then((token) => {
          Alert.alert('token from async storage:', token);
          this.makeRemoteRequest(this.props.url, token);
        })
        .catch((error) => {
          Alert.alert('Error:', error.toString());
        });
    } else {
      this.makeRemoteRequest(this.props.url, token);
    }
  }

  makeRemoteRequest = (url, token, newRequest = false) => {
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

    fetch(url)
      .then(res => res.json())
      .then(res => {
        this.setState({
          data: page === 1 ? res.results : [...this.state.data, ...res.results],
          error: res.error || null,
          loading: false,
          refreshing: false
        });
      })
      .catch(error => {
        this.setState({ error, loading: false });
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
        <H3>You haven't participated on any rides yet!</H3>
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
