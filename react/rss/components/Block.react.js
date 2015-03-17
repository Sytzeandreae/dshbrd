var React = require('react');
var RssStore = require('../stores/RssStore');
var Item = require('./Item.react');
var $ = require('jquery');

var SubBlock = React.createClass({
    getInitialState: function() {
        return {
            'rss': RssStore.getData()
        };
    },

    componentDidMount: function() {
        $.get('http://127.0.0.1:5000/api/v1/block/rss/1', function(result) {
            if (this.isMounted()) {
                this.setState({
                    'rss': result
                });
            }
        }.bind(this));
        RssStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        RssStore.removeChangeListener(this._onChange);
    },

    render: function() {
        if (this.props.edit) {
            return this._renderEdit();
        } else {
            return this._renderNormal();
        }
    },

    _renderEdit: function() {return <div />},
    _renderNormal: function() {
        if (this.state.rss.rss == undefined) {
            return <div />
        } else {
            return (
                <div>
                    {this.state.rss.rss.channel.item.map(function(item, index) {
                        return <Item item={item} key={index} />
                    })}
                </div>
            )
        }
    },
    _fetchData: function() {
        RssStore.fetchData(this.props.block_specifics.id);
    },

    _onChange: function() {
        this.setState(RssStore.getData());
    }
});

module.exports = SubBlock;
