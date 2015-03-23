var React = require('react');

var Item = React.createClass({
    render: function() {
        return (
            <li>
                <a href={this.props.item.link}>
                    <h4>{this.props.item.title}</h4>
                </a>
                <p><a href={this.props.item.comments}>Comments</a></p>
            </li>
        )
    } 
});

module.exports = Item;
