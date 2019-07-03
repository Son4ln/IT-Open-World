import React, {Component} from 'react'
import Head from '../components/document_head'

export default class About extends Component {
  render() {
    return (
      <div>
        <Head title="About"/>
        <p className="text-danger">ABout Page</p>
      </div>
    )
  }
}
