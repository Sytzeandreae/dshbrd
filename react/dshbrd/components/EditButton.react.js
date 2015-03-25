var React = require('react');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var classNames = require('classnames');

var EditButton = React.createClass({
    mixins: [BlockMixin],
    
    _renderNormal: function() {
        return (
            <a className={"waves-effect waves-light btn red absolute"} onClick={this.props.onClick}>
                <i className={"mdi-editor-mode-edit tiny"}></i>
            </a>
        )
    },
    _renderEdit: function() {
        return (
            <a className={"waves-effect waves-light btn absolute"} onClick={this.props.onClick}>
                <i className={"mdi-action-done tiny"}></i>
            </a>
        )
    }
});

module.exports = EditButton;
