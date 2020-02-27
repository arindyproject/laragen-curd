import React, {
    Component
} from 'react';
import ReactDOM from 'react-dom';
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
        //componentdidmount
    }

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
        return (
            <div>
                <h5>Table //name</h5>
                {
                    this.state.data.map((vv) =>
                        <h2>{vv.id}</h2>
                    )
                }
            </div>
        );
    }
}
if (document.getElementById('@nameid')) {
    ReactDOM.render(< name_class />, document.getElementById('@nameid'));
}
