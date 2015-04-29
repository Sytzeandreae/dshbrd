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
                <div className={"flex-container"}>
                    {this.state.blocks.map(function(block, index) {
                        return (<Block key={index} block={block} last={nrBlocks == index+1}/>)
                    })}
                    <div className={"fixed-action-btn"} style={{bottom: '45px', right: '24px;'}}>
                        <a className={"btn-floating btn-large red"}>
                            <i className={"large mdi-action-view-headline"}></i>
                        </a>
                        <ul>
                            <li>
                                <a className={"btn-floating red"}>
                                    <i className={"large mdi-ditor-insert-chart"}></i>
                                </a>
                            </li>
                        </ul>
                    </div>
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
