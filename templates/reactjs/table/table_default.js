import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
import Table from 'react-bootstrap/Table';
import Alert from 'react-bootstrap/Alert';
import Card from 'react-bootstrap/Card';
import Spinner from 'react-bootstrap/Spinner';
import { Pagination } from 'react-laravel-paginex';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';
import Button from 'react-bootstrap/Button';
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
            temp_id : 0,
            //stateitem
        };
        this.getData = this.getData.bind(this);
        //binditem
    }


    //componentDidMount
    componentDidMount() {
        this.getData(this.state.data);
        this.props.refresh(this.getData);
        //componentdidmount
    }


    //actionmethod

    //get data
    getData(data = this.state.data) {
        this.setState({ showTable: true, showEdit: false });
        let uri = '//url' + '?page=' + data.page
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

            return (
                <Card>
                    <Card.Body>
                        <h5>Table //name</h5>
                        {this.alertSuccess()}
                        {this.alertError()}
                        <Table responsive striped bordered hover size="sm">
                            <thead>
                                <tr>
                                //itemcolumns
                                </tr>
                            </thead>
                            <tbody>
                                {this.state.data.data.map((item) =>
                                    <tr key={item.id}>
                                    //itemrows
                                    </tr>
                                )}
                            </tbody>
                        </Table>
                        <Pagination changePage={this.getData} data={this.state.data} />
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
            //showcomponents
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
