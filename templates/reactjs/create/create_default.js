import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
//import

export default class name_class extends Component {

    //constructor
    constructor(props) {
        super(props);
        this.state = {
            isLoading: false,
            //stateitem
        };
        // bind handleSubmit method
        this.handleSubmit = this.handleSubmit.bind(this);
        this.refreshCreate = this.refreshCreate.bind(this);
        // bind handle Form
        //binditem
    }

    //refresh Create
    refreshCreate(){
        this.setState({
            isSuccess : false,
            isError  : false,
        });
    }


    //componentDidMount
    componentDidMount() {
        this.props.refresh(this.refreshCreate);
        //componentdidmount
    }


    //get options
    getOptions() {

        let uri = '//optionsurl'
        axios.get(uri).then((response) => {
            this.setState({

                //stateoptionsitems
            })
        });
    }

    // create handleSubmit
    handleSubmit(e) {
        this.setState({
            isLoading: true,
            isSuccess: false,
        });
        // stop browser's default behaviour of reloading on form submit
        e.preventDefault();
        const data = {
            //dataitem
        }
        let uri = '//url';
        axios.post(uri, data).then((response) => {
            this.setState({
                isLoading: false,
                isSuccess: true,
                //reset form
                //stateitem
            });
            //componentdidmount
        }).catch(function (error) {
            // handle error
            console.log(error);
            this.setState({
                isLoading: false,
                isError: true,
            });
        });

    }

    //handleitem

    alertSuccess() {
        if (this.state.isSuccess) {
            return (
                <Alert variant="success" onClose={() => this.setState({ isSuccess: false })} dismissible>
                    Success
                </Alert>
            );
        }
    }
    alertError() {
        if (this.state.isError) {
            return (
                <Alert variant="success" onClose={() => this.setState({ isError: false })} dismissible>
                    Success
                </Alert>
            );
        }
    }
    render() {
        return (
            <div>
                <h5>Create //name</h5>
                {this.alertSuccess()}
                <form onSubmit={this.handleSubmit}>
                    <Row>
                        //item
                        <Button variant="outline-success" block type="submit">{this.state.isLoading ? 'Loading...' : 'Submit'}</Button>
                    </Row>
                </form>
            </div >
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
