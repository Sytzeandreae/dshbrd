var React = require('react');

// Requiring the subblocks, can't do this on runtime
require('../../rss/components/Block.react');
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
        return (
            <div>
                <h3>{this.props.block.name}</h3>
                <SubBlock block_specifics={this.props.block.block_specifics} edit={this.state.edit} />
            </div>
        )
    },

    _edit: function() {
        if (this.state.edit) {
            this.setState({'edit': false});
        } else {
            this.setState({'edit': true});
        }
    }
});

module.exports = Block;
