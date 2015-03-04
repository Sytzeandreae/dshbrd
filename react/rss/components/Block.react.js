var React = require('react');
var RssStore = require('../stores/RssStore');

var SubBlock = React.createClass({
    getInitialState: function() {
        return RssStore.getData();
    },

    componentWillMount: function() {
        setInterval(this._fetchData(), this.props.block_specifics.refresh_interval);                    
        RssStore.addChangeListener(this._onChange);
    },

    render: function() {
        if (this.props.edit) {
            return this._renderEdit();
        } else {
            return this._renderNormal();
        }
    },

    _renderEdit: function() {},
    _renderNormal: function() {},
    _fetchData: function() {
        RssStore.fetchData(this.props.block_specifics.url);
    },

    _onChange: function() {
        this.setState(RssStore.getData());            
    }
});

module.exports = SubBlock;
