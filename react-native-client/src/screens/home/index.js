import React, { Component } from 'react';
import { Alert, FlatList, View } from 'react-native';
import {
  Button,
  Container,
  Content,
  Fab,
  List,
  Footer,
  FooterTab,
  H3,
  Icon,
  Spinner,
  Text
} from 'native-base';

import styles from './styles';
import RideItem from '../../components/RideItem';
import AppHeader from '../../components/AppHeader';
import config from '../../../config.js';
import { convertDateForAPI } from '../../services/utils';

class Home extends Component {

  constructor(props) {
    super(props);
    this.state = {
      fabActive: false,
      loading: false,
      data: [],
      page: 1,
      seed: 1,
      error: null,
      refreshing: false,
      next: undefined
    };
    this.filterParams = {
      destination: '',
      departure: '',
      date: new Date()
    };
  }

  componentDidMount() {
    this.getRidesFromAPI('new request'); // string eveluates to true
  }


  makeFilteredRemoteRequest = (filterParams) => {
    this.filterParams.destination = filterParams.destination;
    this.filterParams.departure = filterParams.departure;
    this.filterParams.date = filterParams.date;
    this.getRidesFromAPI('new-request');
  };

  getRidesFromAPI = (newRequest = false) => {
    /*
      param: newRequest: boolean. If true will start on a first page. 
    */

   let { page } = this.state;
    if (newRequest) {
      this.setState({
        page: 1,
        seed: 1
      });
      page = 1;
    } 
    
    let url = `${config.BACKEND_DOMAIN}/rides/?page=${page}`;

    if (this.filterParams.destination) {
      url = url + `&destination=${this.filterParams.destination}`;
    }

    if (this.filterParams.departure) {
      url = url + `&departure=${this.filterParams.departure}`;
    }
    //TODO: add date filtering, make today default choice
    if (this.filterParams.date) {
      url += `&date=${convertDateForAPI(this.filterParams.date)}`;
    }

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

  //handleRefresh = () => {
  //  this.setState(
  //    {
  //      page: 1,
  //      seed: this.state.seed + 1,
  //      refreshing: true
  //    },
  //    () => {
  //      this.getRidesFromAPI();
  //    }
  //  );
  //};

  handleLoadMore = () => {
    this.setState(
      {
        page: this.state.page + 1
      },
      () => {
        this.getRidesFromAPI();
      }
    );
  };


  //renderSeparator = () => {
  //  return (
  //    <View
  //      style={{
  //        height: 1,
  //        width: '86%',
  //        backgroundColor: '#CED0CE',
  //        marginLeft: '14%'
  //      }}
  //    />
  //  );
  //};

  renderHeader = () => {
    return <AppHeader
      handleSearchButtonPress={this.makeFilteredRemoteRequest}

    />;
  };

  //renderFooter = () => {
  //  if (!this.state.loading) return null;
  //
  //  return (
  //    <View
  //      style={{
  //        paddingVertical: 20,
  //        borderTopWidth: 1,
  //        borderColor: '#CED0CE'
  //      }}
  //    >
  //      <Spinner />
  //    </View>
  //  );
  //};

  renderEmpty = () => {
    return (
      <Content style={{ margin: 15 }}>
        <Text>{'\n'}</Text>
        <H3>Unfortunately no rides available for this day.</H3>
      </Content>

    );
  };


  render() {
    this.token = this.props.navigation.getParam('token');
    return (
      <Container>
        <FlatList
          data={this.state.data}
          renderItem={({ item }) => (
            <RideItem
              rideItem={item}
            />

          )}
          keyExtractor={item => item.id}
          //ItemSeparatorComponent={this.renderSeparator}
          ListHeaderComponent={this.renderHeader}
          //ListFooterComponent={this.renderFooter}
          ListEmptyComponent={this.renderEmpty}
          //onRefresh={this.handleRefresh}
          //refreshing={this.state.refreshing}
          onEndReached={this.handleLoadMore}
        //onEndReachedThreshold={50}
        />

        <Fab
          active={this.state.fabActive}
          direction='up'
          containerStyle={{ bottom: 60 }}
          style={{ backgroundColor: '#5067FF' }}
          position='bottomRight'
          onPress={() => this.props.navigation.navigate('AddRide', { token: this.token })}>
          <Icon name='md-add' />
        </Fab>
        <Footer>
          <FooterTab>
            <Button vertical>
              <Icon name='md-home' />
              <Text>Home</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('MyRides', { token: this.token })}
            >
              <Icon name='md-car' />
              <Text>My Rides</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('Login', { token: this.token })}
            >
              <Icon name='person' />
              <Text>Account</Text>
            </Button>

            
          </FooterTab>
        </Footer>

      </Container>
    );
  }
}

export default Home;
