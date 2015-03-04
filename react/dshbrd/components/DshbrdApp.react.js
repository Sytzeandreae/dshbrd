var React = require('react');
var DshbrdStore = require('../stores/DshbrdStore');

var Block = require('./Block.react');

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
        return (
            this.state.blocks.map(function(block, index) {
                return (<Block key={index} block={block} />)
            }) 
        )
    },

    _onChange: function() {
        this.setState(getDshbrdState());
    }
});

module.exports = DshbrdApp;
