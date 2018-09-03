import React, { Component } from 'react';
import { Alert, FlatList, View } from 'react-native';
import {
  Body,
  Button,
  Container,
  Content,
  Left,
  Header,
  H3,
  Icon,
  Spinner,
  Tabs,
  Tab,
  Title,
  Text
} from 'native-base';

import styles from './styles';
import RideItem from '../../components/RideItem';
import AppHeader from '../../components/AppHeader';
import deviceStorage from '../../services/DeviceStorage';
import testData from  '../../../data-dump';


class MyRides extends Component {

  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      data: testData.rides,
      page: 1,
      seed: 1,
      error: null,
      refreshing: false
    };

  }

  componentDidMount() {
    let token = this.props.navigation.getParam(token, undefined);
    if (!token) {
      deviceStorage.loadToken().
      then(
        this.makeRemoteRequest(`http://192.168.43.216:8000/me/rides_as_driver//?page=${page}`, token);
      );
    }
    this.makeRemoteRequest();
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


  renderSeparator = () => {
    return (
      <View
        style={{
          height: 1,
          width: '86%',
          backgroundColor: '#CED0CE',
          marginLeft: '14%'
        }}
      />
    );
  };

  renderHeader = () => {
    return <Header>
      <Left>
        <Button transparent onPress={() => this.props.navigation.goBack()}>
          <Icon name='arrow-back' />
        </Button>
      </Left>
      <Body>
        <Title>My Rides</Title>
      </Body>
    </Header>;
  };


  renderEmpty = () => {
    return (
      <View>
        <H3>You haven't participated on any rides yet!</H3>
      </View>
    );
  };

  render() {
    
    return (
      <Container>

        <Header hasTabs>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>My Rides</Title>
          </Body>
        </Header>
        <Tabs locked>
          <Tab heading="Passenger">
          <Content>
          <FlatList
            data={this.state.data}
            renderItem={({ item }) => (
              <RideItem
                rideItem={item}
              />

            )}
            keyExtractor={item => item.id}
            //ItemSeparatorComponent={this.renderSeparator}
            //ListHeaderComponent={this.renderHeader}
            ListFooterComponent={this.renderFooter}
            ListEmptyComponent={this.renderEmpty}
            onRefresh={this.handleRefresh}
            refreshing={this.state.refreshing}
            onEndReached={this.handleLoadMore}
          //onEndReachedThreshold={50}
          />
        </Content>
        
          </Tab>
          <Tab heading="Driver">
            <Text>some content here</Text>
          </Tab>
        </Tabs>


      </Container>
    );
  }
}

export default MyRides;
