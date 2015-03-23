var React = require('react');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var classNames = require('classnames');

var EditButton = React.createClass({
    mixins: [BlockMixin],
    
    _renderNormal: function() {
        return (
            <button onClick={this.props.onClick}>Edit</button>
        )
    },
    _renderEdit: function() {
        return (
            <button onClick={this.props.onClick}>Done</button>
        )
    }
});

module.exports = EditButton;
