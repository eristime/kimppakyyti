import React, { Component } from 'react';
import { FlatList, View } from 'react-native';
import {
  Body,
  Button,
  Container,
  Content,
  Left,
  List,
  Footer,
  FooterTab,
  Header,
  H3,
  Icon,
  ListItem,
  Separator,
  Spinner,
  Tabs,
  Tab,
  Title,
  Text
} from 'native-base';

import styles from './styles';
import RideItem from '../../components/RideItem';
import AppHeader from '../../components/AppHeader';
import testData from  '../../../data-dump';


class Home extends Component {

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
    this.makeRemoteRequest();
  }

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
    //let url = `http://192.168.1.103:8000/rides/?page=${page}`;  // desktop IP
    let url = `http://192.168.43.216:8000/rides/?page=${page}`;  // laptop IP

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
          <Tab heading="As passenger">
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
          <Tab heading="As Driver">
            <Text>some content here</Text>
          </Tab>
          <Tab heading="Requests">
          <Text>some content here</Text>
          </Tab>
        </Tabs>


        <Footer>
          <FooterTab>
            <Button vertical
              onPress={() => this.props.navigation.navigate('Home')}
            >
              <Icon name='md-list' />
              <Text>Rides</Text>
            </Button>

            <Button vertical>
              <Icon name='md-car' />
              <Text>My Rides</Text>
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
