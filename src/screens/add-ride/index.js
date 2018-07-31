import React, { Component } from "react";
import { Modal, TouchableOpacity, View } from "react-native";
import {
  Button,
  Container,
  Content,
  DatePicker,
  Form,
  Header,
  H2,
  Icon,
  Input,
  Item,
  Label,
  Text,
  Left,
  Body,
  Title,
  Textarea
} from "native-base";
import DateTimePicker from 'react-native-modal-datetime-picker';


class AddRide extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isDatePickerVisible: false,
      isTimePickerVisible: false,
      modalVisible: false,
      chosenDate: new Date(),
      chosenTime: new Date()
    };

  }


  _showDatePicker = () => this.setState({ isDatePickerVisible: true });

  _hideDatePicker = () => this.setState({ isDatePickerVisible: false });

  _showTimePicker = () => this.setState({ isTimePickerVisible: true });

  _hideTimePicker = () => this.setState({ isTimePickerVisible: false });

  _handleDatePicked = (date) => {
    this.setState({ chosenDate: date });
    this._hideDatePicker();
  };

  _handleTimePicked = (time) => {
    this.setState({ chosenTime: time });
    this._hideTimePicker();
  };

  setModalVisible = (visible) => {
    this.setState({ modalVisible: visible });
  }


  render() {
    const d = new Date();
    const maximumDate = d.setFullYear(d.getFullYear() + 2);
    return (
      <Container>

        <Header>
          <Left>
            <Button transparent onPress={() => this.props.navigation.goBack()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body>
            <Title>Add a ride</Title>
          </Body>
        </Header>

        <Content>
          <Form>
            <Item>
              <Label>From</Label>
              <Input placeholder="Select departure" />
            </Item>


            <Item>
              <Label>To</Label>
              <Input placeholder="Select destination" />
            </Item>

            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
              <Label>
                When
            </Label>
              
              <View >
                <TouchableOpacity onPress={this._showDatePicker}>
                  <Text>{this.state.chosenDate.toLocaleDateString()}</Text>
                </TouchableOpacity>

                <DateTimePicker
                  minimumDate={new Date()}
                  maximumDate={maximumDate}  // TODO: deal with maximum date
                  date={this.state.chosenDate}
                  isVisible={this.state.isDatePickerVisible}
                  onConfirm={this._handleDatePicked}
                  onCancel={this._hideDatePicker}
                  mode='date'
                />
              </View>

              <View >
                <TouchableOpacity onPress={this._showTimePicker}>
                  <Text>{this.state.chosenTime.toLocaleTimeString()}</Text>
                </TouchableOpacity>

                <DateTimePicker
                  date={this.state.chosenTime}
                  isVisible={this.state.isTimePickerVisible}
                  onConfirm={this._handleTimePicked}
                  onCancel={this._hideTimePicker}
                  mode='time'
                />
              </View>
            </View>

            {/*TODO: add better passenger selector, +- passenger instead of number input*/}
            <Item fixedLabel>
              <Label>Maximum passengers</Label>
              <Input keyboardType='numeric' placeholder="4" />
            </Item>

            <Item fixedLabel>
              <Label>Estimated fuel cost</Label>
              <Input keyboardType='numeric' placeholder="20" />
            </Item>

            <Textarea last rowSpan={5} bordered placeholder="Additional information" />
          </Form>

          <Button block primary
            onPress={() => {
              this.setModalVisible(!this.state.modalVisible)
            }}>
            <Text>Post a ride</Text>
          </Button>
        </Content>
          

          {/*Style modal page appropriately*/}
        <Modal
          animationType="fade"
          transparent={false}
          visible={this.state.modalVisible}
          onRequestClose={() => { alert("Modal has been closed.") }}
        
        >
          <Container /*style={{backgroundColor:'white', position:'absolute', top:150, left:20, right:20}}*/>

            {/* <Header>
              <Body>
                <Title>Post a ride</Title>
              </Body>
            </Header>*/}


            <Text>You are posting a publically available ride. Do you want to continue?</Text>

            <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'space-around' }}>
              <Button block success>
                {/*TODO: post the ride and direct to home page*/}
                <Text>Confirm</Text>
              </Button>
              <Button block danger
                onPress={() => {
                  this.setModalVisible(!this.state.modalVisible)
                }}>
                <Text>Cancel</Text>
              </Button>
            </View>

          </Container>

        </Modal>


      </Container>
    );
  }
}

export default AddRide;
