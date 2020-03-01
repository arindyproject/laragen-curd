import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import filterFactory, { textFilter, numberFilter, dateFilter } from 'react-bootstrap-table2-filter';
import Alert from 'react-bootstrap/Alert';
import Card from 'react-bootstrap/Card';
import Spinner from 'react-bootstrap/Spinner';
//import

export default class name_class extends Component {
    //constructor
    constructor(props) {
        super(props);
        this.state = {
            isSuccess: false,
            isError: false,
            isLoading: true,
            showTable: true,
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
                isSuccess: false,
                isLoading: false,
                showTable: true,
                data: response.data.//dataname,
                //stateoptionsitems
            })
        });
    }

    alertSuccess() {
        if (this.state.isSuccess) {
            return (
                <Alert variant="success" onClose={() => this.setState({ isSuccess: false })} dismissible>
                    Delete Success
                </Alert>
            );
        }
    }

    alertError() {
        if (this.state.isError) {
            return (
                <Alert variant="danger" onClose={() => this.setState({ isError: false })} dismissible>
                    Delete Error
                </Alert>
            );
        }
    }

    Loading() {
        if (this.state.isLoading) {
            return (
                <Spinner animation="grow" />
            );
        }
    }

    showTable() {
        if (this.state.showTable && !this.state.isLoading) {
            const rowEvents = {
                onClick: (e, row, rowIndex) => {
                    this.handleDelete(e, row.id);
                }
            };
            const data = [];
            const columns = [
                //itemcolumns
            ];
            return (
                <Card>
                    <Card.Body>
                        <h5>Table //name</h5>
                        {this.alertSuccess()}
                        {this.alertError()}
                        <BootstrapTable bootstrap4 keyField='id' data={this.state.data} columns={columns} filter={filterFactory()} pagination={paginationFactory()} striped hover condensed />
                    </Card.Body>
                </Card>
            );
        }
    }

    render() {

        return (
            <div>
                {this.Loading()}
                {this.showTable()}
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
