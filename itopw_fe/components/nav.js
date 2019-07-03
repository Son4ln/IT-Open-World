import React, {Component} from 'react'
import ActiveLink from './active_link'

export default class Active extends Component {
  render() {
    return (
      <div>
        <ActiveLink href='/'>Home</ActiveLink>
        <ActiveLink href='/about' as="about">About</ActiveLink>
      </div>
    )
  }
}