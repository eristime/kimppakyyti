import React from 'react';
import {
  Text,
} from 'native-base';

const Header2 = (props) => {
    return (
        <Text style={{fontSize:25, padding:2}}>{props.children}</Text>
    );
  };
export default Header2;
