import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import filterFactory, { textFilter, numberFilter , dateFilter } from 'react-bootstrap-table2-filter';

//import

export default class name_class extends Component {
    //constructor
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            //stateitem
        };
        this.getData = this.getData.bind(this);
        //binditem
    }


    //componentDidMount
    componentDidMount() {
        this.getData();
        this.props.refresh(this.getData);
        //componentdidmount
    }


    //actionmethod

    //get data
    getData() {
        let uri = '//url'
        axios.get(uri).then((response) => {
            this.setState({
                data: response.data.//dataname,
                //stateoptionsitems
            })
        });
    }

    render() {
        const data = [];
        const columns = [
            //itemcolumns
        ];
        return (
            <div>
                <h5>Table //name</h5>
                <BootstrapTable bootstrap4 keyField='id' data={this.state.data} columns={columns} filter={filterFactory()} pagination={paginationFactory()} striped hover condensed />
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
