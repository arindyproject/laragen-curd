import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';

import Tabs from 'react-bootstrap/Tabs';
import Tab from 'react-bootstrap/Tab';
//import

export default class name_class extends Component {

    refreshComponents(item){
       //itemrefresh
    }

    render() {
        return (
            <div>
                <h5>//name</h5>
                <Tabs defaultActiveKey="table" id="uncontrolled-tab-example" onSelect={(item) => this.refreshComponents(item)}>
                //tabitem
                </Tabs>
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
