import React, { Component } from 'react';
import { View, TouchableOpacity, StyleSheet } from 'react-native';
import {
  Button,
  Content,
  Icon,
  Input,
  Item,
  Label,
  Header,
  Text
} from 'native-base';
import DateTimePicker from 'react-native-modal-datetime-picker';
import PropTypes from 'prop-types';
import { convertToHoursMinutes } from '../services/utils';


class AppHeader extends Component {

  constructor(props) {
    super(props);
    this.state = {
      destination: '',
      departure: '',
      chosenDate: new Date(),
      chosenTime: new Date()
    };
  }

  _showDatePicker = () => this.setState({ isDatePickerVisible: true });

  _hideDatePicker = () => this.setState({ isDatePickerVisible: false });

  _handleDatePicked = (date) => {
    this.setState({ chosenDate: date });
    this._hideDatePicker();
  };

  _showTimePicker = () => this.setState({ isTimePickerVisible: true });

  _hideTimePicker = () => this.setState({ isTimePickerVisible: false });

  _handleTimePicked = (time) => {
    this.setState({ chosenTime: time });
    this._hideTimePicker();
  };

  passParamsToParent = () => {
    const { handleSearchButtonPress } = this.props;
    handleSearchButtonPress({
      destination: this.state.destination,
      departure: this.state.departure,
      date: this.state.chosenDate,
      time: this.state.chosenTime
    });
  }


  render() {
    const d = new Date();
    const maximumDate = new Date(d.setFullYear(d.getFullYear() + 2));
    return (

      <Header style={{ height: 140 }}>
        <Content style={{ flex: 1 }}>
          <View style={{ flex: 1, marginLeft: 10 }}>
            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-start' }}>
              <View >

                <Item fixedLabel
                  style={{ width: 270, height: 35, borderRadius: 5, marginTop: 5, backgroundColor: 'white' }}>
                  <Label>From</Label>
                  <Input
                    placeholder="Set departure"
                    onChangeText={(text) => this.setState({ departure: text })}
                  />
                </Item>

                <Item fixedLabel
                  style={{ width: 270, height: 35, borderRadius: 5, marginTop: 5, backgroundColor: 'white' }}>
                  <Label>To</Label>
                  <Input
                    placeholder="Set destination"
                    onChangeText={(text) => this.setState({ destination: text })}
                  />
                </Item>
              </View>

              {/*
              <View style={{ justifyContent: 'center' }}>
                <Button iconLeft transparent dark >
                  <Icon name='swap' />
                </Button>
              </View>
              */}

            </View>

            <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginTop: 5 }} >


              <View >
                <View >
                  <TouchableOpacity onPress={this._showDatePicker}>
                    <Text style={{ color: 'white' }}>{this.state.chosenDate.toLocaleDateString()}</Text>
                  </TouchableOpacity>

                  <DateTimePicker
                    minimumDate={new Date()}
                    maximumDate={maximumDate}
                    date={this.state.chosenDate}
                    isVisible={this.state.isDatePickerVisible}
                    onConfirm={this._handleDatePicked}
                    onCancel={this._hideDatePicker}
                    mode="date"
                  />
                </View>




                {/* TODO: icon for more filter options
              <Button iconLeft transparent dark >
                <Icon name='more' />
              </Button>
              */}
              </View>

              <View >
                <TouchableOpacity onPress={this._showTimePicker}>
                  <Text style={{ color: 'white' }}>{convertToHoursMinutes(this.state.chosenTime)}</Text>
                </TouchableOpacity>

                <DateTimePicker
                  //minimumDate={new Date()}
                  //maximumDate={maximumDate}
                  date={this.state.chosenTime}
                  isVisible={this.state.isTimePickerVisible}
                  onConfirm={this._handleTimePicked}
                  onCancel={this._hideTimePicker}
                  mode="time"
                />
              </View>

              <Button rounded success
                onPress={() => this.passParamsToParent()}>
                <Text>Search</Text>
              </Button>
            </View>

          </View>
        </Content>

      </Header>

    );
  }
}


const styles = StyleSheet.create({
  headerRowItem: {
    marginLeft: 10,
    backgroundColor: '#fff',
    paddingTop: 100,
    paddingHorizontal: 30
  }
});


/*
AppHeader.propTypes = {
  handleSearchButtonPress: React.PropTypes.func
};
*/

export default AppHeader;
