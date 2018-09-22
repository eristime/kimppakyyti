import React, { Component } from 'react';
import { Alert, FlatList, View } from 'react-native';
import {
  Button,
  Container,
  Content,
  Fab,
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
import { convertDateForAPI, convertToHoursMinutes, convertTimeForAPI } from '../../services/utils';


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
      date: new Date(),
      time: ''
    };
  }

  componentDidMount() {
    this.getRidesFromAPI('new request'); // non-empty string eveluates to true
  }


  makeFilteredRemoteRequest = (filterParams) => {
    this.filterParams.destination = filterParams.destination;
    this.filterParams.departure = filterParams.departure;
    this.filterParams.date = filterParams.date;
    this.filterParams.time = filterParams.time;
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
        seed: 1,
      });
      page = 1;
    }

    let url = `${config.BACKEND_DOMAIN}/rides/?page=${page}`;

    if (this.filterParams.destination) {
      url = url + `&destination=${this.filterParams.destination.toLocaleLowerCase()}`;
    }

    if (this.filterParams.departure) {
      url = url + `&departure=${this.filterParams.departure.toLocaleLowerCase()}`;
    }

    if (this.filterParams.date) {
      url += `&date=${convertDateForAPI(this.filterParams.date)}`;
    }
    
    if (this.filterParams.time) {
      url += `&time__gte=${encodeURIComponent(convertToHoursMinutes(this.filterParams.time))}`;
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

  renderHeader = () => {
    return <AppHeader
      handleSearchButtonPress={this.makeFilteredRemoteRequest}

    />;
  };

  renderEmpty = () => {
    if (this.state.loading){
      return null;
    }
    return (
      <Content style={{ margin: 15 }}>
        <Text>{'\n'}</Text>
        <H3>Unfortunately no rides available for these parameters.</H3>
      </Content>
    );
  };

  renderFooter = () => {
    if (!this.state.loading){
      return null;
    }

    return (
      <View
        style={{
          paddingVertical: 20,
          borderTopWidth: 1,
          borderColor: '#CED0CE'
        }}
      >
        <Spinner color="blue" />
      </View>
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
              showModalRequestButton={true}
            />

          )}
          keyExtractor={item => item.id}
          //ItemSeparatorComponent={this.renderSeparator}
          ListHeaderComponent={this.renderHeader}
          ListFooterComponent={this.renderFooter}
          ListEmptyComponent={this.renderEmpty}
          //onRefresh={this.handleRefresh}
          //refreshing={this.state.refreshing}
          onEndReached={this.handleLoadMore}
        //onEndReachedThreshold={50}
        />

        <Fab
          active={this.state.fabActive}
          direction="up"
          containerStyle={{ bottom: 60 }}
          style={{ backgroundColor: '#5067FF' }}
          position="bottomRight"
          onPress={() => this.props.navigation.navigate('AddRide', { token: this.token })}>
          <Icon name="md-add" />
        </Fab>
        <Footer>
          <FooterTab>
            <Button vertical>
              <Icon name="md-home" />
              <Text>Home</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('Passenger', { token: this.token })}
            >
              <Icon name="md-people" />
              <Text>Passenger</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('Driver', { token: this.token })}
            >
              <Icon name="md-car" />
              <Text>Driver</Text>
            </Button>

            <Button vertical
              onPress={() => this.props.navigation.navigate('Login', { token: this.token })}
            >
              <Icon name="person" />
              <Text>Account</Text>
            </Button>

          </FooterTab>
        </Footer>

      </Container>
    );
  }
}

export default Home;
