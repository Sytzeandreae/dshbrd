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
        if (this.state.blocks.length > 0) {
            var nrBlocks = this.state.blocks.length;
            return (
                <div className={"row full-width"}>
                    {this.state.blocks.map(function(block, index) {
                        return (<Block key={index} block={block} last={nrBlocks == index+1}/>)
                    })}
                </div> 
            )
        } else {
            return <div />
        }
    },

    _onChange: function() {
        this.setState(getDshbrdState());
    }
});

module.exports = DshbrdApp;
