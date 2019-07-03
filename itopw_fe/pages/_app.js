import React from 'react'
import App, { Container } from 'next/app'
import Nav from '../components/nav'
import LeftHidden from '../components/left_hidden'
import RightHidden from '../components/right_hidden'

class MyApp extends App {
  static async getInitialProps({ Component, ctx }) {
    let pageProps = {}

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx)
    }

    return { pageProps }
  }

  render() {
    const { Component, pageProps } = this.props
    return (
        <Container>
            <LeftHidden/>
            <Nav />
            <Component {...pageProps} />
            <RightHidden/>
        </Container>
    )
  }
}

export default MyApp