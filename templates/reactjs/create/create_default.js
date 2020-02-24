import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button'
//import

export default class name_class extends Component {

    //constructor
    constructor(props) {
        super(props);
        this.state = {

        };
        // bind handleSubmit method
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // create handleSubmit
    handleSubmit(e) {
        // stop browser's default behaviour of reloading on form submit
        e.preventDefault();
        console.log('hallo');
    }

    render() {
        return (
            <div>
                <h5>Create //name</h5>
                <Form as={Row} onSubmit={this.handleSubmit}>
                    //item
                    <Button variant="outline-success" block type="submit">Submit</Button>
                </Form>
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
