var React = require('react');
var classNames = require('classnames');

var EditButton = require('./EditButton.react')
// Requiring the subblocks, can't do this on runtime
require('../../rss/components/Block.react');
require('../../xkcd/components/Block.react');
//require('../../newrelic/components/Block.react');
//require('../../reddit/components/Block.react');

var Block = React.createClass({
    getInitialState: function() {
        return {
            'edit': false
        }
    },

    render: function() {
        var SubBlock = require('../../' + this.props.block.block_type + '/components/Block.react');
        var classes = classNames({
            'col': true,
            's3': true,
        });
        return (
                <div className={"z-depth-1 block"}>
                    <h3>{this.props.block.block_name}</h3>
                    <EditButton button={true} onClick={this._toggleEdit} edit={this.state.edit}/>
                    <div className={"inner-block"}>
                        <SubBlock block_specifics={this.props.block.block_specifics} edit={this.state.edit} />
                    </div>
                </div>
        )
    },

    _toggleEdit: function() {
        console.log('hi');
        if (this.state.edit) {
            this.setState({'edit': false});
        } else {
            this.setState({'edit': true});
        }
    }
});

module.exports = Block;
