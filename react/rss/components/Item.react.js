var React = require('react');

var Item = React.createClass({
    render: function() {
        return (
                <a className={"collection-item"} href={this.props.item.link}>
                    {this.props.item.title}
                </a>
        )
    } 
});

module.exports = Item;
