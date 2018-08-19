import React, { Component } from 'react';
import { FlatList, View } from 'react-native';
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


const rides = [{
  id: 981203810928,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 9812038104448,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 1111111111111,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
},
{
  id: 2222222222222,
  driver: {
    name: 'Make Penttilä',
    rating: 4.55,
    reviews: 200,
    profile_url: 'xxxxx',
    car_model: 'Toyota Auris',
    car_register_plate: 'FXX-223'
  },
  destination: 'Oulu',
  origin: 'Rovaniemi',
  available_seats: 3,
  date: '11-05-2018',
  departure: '11:44',
  est_fuel_price: 20.55
}];


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
      refreshing: false
    };
    this.filterParams = {
      destination: '',
      departure: '',
      date: new Date()
    };
  }

  componentDidMount() {
    this.makeRemoteRequest();
  }

  convertDateForAPI = (dateObject) => {
    /*
    param:date, JS date object
    */
    // getMonth() returns month from 0 to 11
    let month = (dateObject.getMonth() + 1).toString();
    let date = (dateObject.getDate()).toString();
    if (month.length < 2) {
      month = '0' + month;
    }
    if (date.length < 2) {
      date = '0' + date;
    }
    return `${dateObject.getFullYear()}-${month}-${date}`;
  };

  makeFilteredRemoteRequest = (filterParams) => {
    this.filterParams.destination = filterParams.destination;
    this.filterParams.departure = filterParams.departure;
    this.filterParams.date = filterParams.date;
    this.makeRemoteRequest('new-request');
  };

  makeRemoteRequest = (newRequest = false) => {
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
    //let url = `http://10.0.2.2:8000/rides/?page=${page}`; //virtual Android on desktop
    let url = `http://192.168.1.103:8000/rides/?page=${page}`;  // desktop IP


    if (this.filterParams.destination) {
      url = url + `&destination=${this.filterParams.destination}`;
    }

    if (this.filterParams.departure) {
      url = url + `&departure=${this.filterParams.departure.toLocaleDateString()}`;
    }
    //TODO: add date filtering, make today default choice
    if (this.filterParams.date) {
      url += `&date=${this.convertDateForAPI(this.filterParams.date)}`;
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

  handleRefresh = () => {
    this.setState(
      {
        page: 1,
        seed: this.state.seed + 1,
        refreshing: true
      },
      () => {
        this.makeRemoteRequest();
      }
    );
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
    return <AppHeader
      handleSearchButtonPress={this.makeFilteredRemoteRequest}

    />;
  };

  renderFooter = () => {
    if (!this.state.loading) return null;

    return (
      <View
        style={{
          paddingVertical: 20,
          borderTopWidth: 1,
          borderColor: '#CED0CE'
        }}
      >
        <Spinner />
      </View>
    );
  };

  renderEmpty = () => {
    return (
      <View>
        <H3>Unfortunately no rides available.</H3>
      </View>
    );
  };
  /*
  renderList = () => {
    if (this.state.error) {
      return <Text>{this.state.error}</Text>
    }
  }
  */

  render() {

    return (
      <Container>

        <Content >


          <List containerStyle={{ borderTopWidth: 0, borderBottomWidth: 0 }}>
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
              ListFooterComponent={this.renderFooter}
              ListEmptyComponent={this.renderEmpty}
              onRefresh={this.handleRefresh}
              refreshing={this.state.refreshing}
              onEndReached={this.handleLoadMore}
            //onEndReachedThreshold={50}
            />
          </List>

        </Content>
        <Fab
          active={this.state.fabActive}
          direction='up'
          containerStyle={{ bottom: 60 }}
          style={{ backgroundColor: '#5067FF' }}
          position='bottomRight'
          onPress={() => this.props.navigation.navigate('AddRide')}>
          <Icon name='md-add' />
        </Fab>
        <Footer>
          <FooterTab>
            <Button vertical>
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

      </Container>
    );
  }
}

export default Home;
