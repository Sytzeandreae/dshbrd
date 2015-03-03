var React = require('react');
var DshbrdStore = require('../stores/DshbrdStore');

function getDshbrdState() {
    return {
        blocks: DshbrdStore.getBlocks()
    };
}


var DshbrdApp = React.createClass({
    getInitialState: function() {
        return getDshbrdState();                 
    },

    componentDidMount: function() {
        DshbrdStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        DshbrdStore.removeChangeListener(this._onChange);
    },

    render: function() {
        return (<div />)
    },

    _onChange: function() {
        this.setState(getDshbrdState());
    }
});

module.exports = DshbrdApp;
