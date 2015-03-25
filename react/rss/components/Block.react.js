var React = require('react');
var RssStore = require('../stores/RssStore');
var BlockMixin = require('../../dshbrd/utils/mixins/BlockMixin');
var Item = require('./Item.react');
var $ = require('jquery');

var SubBlock = React.createClass({
    mixins: [BlockMixin],

    getInitialState: function() {
        return {
            'rss': RssStore.getData(),
            'loading': true
        };
    },

    componentDidMount: function() {
        $.get('http://127.0.0.1:5000/api/v1/block/rss/1', function(result) {
            if (this.isMounted()) {
                this.setState({
                    'rss': result,
                    'loading': false
                });
            }
        }.bind(this));
        RssStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        RssStore.removeChangeListener(this._onChange);
    },

    _renderEdit: function() {
        return (
            <form>
                <fieldset>
                    <legend>Edit</legend>
                    <input type={"hidden"} value={this.props.block_specifics.id} name={"id"} />
                    <label>
                        Feed url                            
                        <input type={"text"} defaultValue={this.props.block_specifics.feed_url} name={"feed_url"} />
                    </label>
                    <a className={"waves-effect waves-light btn"} onClick={this._save} href={"#"}>Save</a>
                </fieldset>

            </form> 
        )
    },

    _renderNormal: function() {
        if (this.state.rss.rss == undefined) {
            return <ul />
        } else {
            return (
                <div className={"collection"}>
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

    _onChange: function(e) {
        this.setState(RssStore.getData());
        return false;
    },

    _save: function() {}
});

module.exports = SubBlock;
