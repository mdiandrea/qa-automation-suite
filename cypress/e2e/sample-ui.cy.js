describe('Cypress Docs Smoke Test', () => {
  it('Loads the homepage and checks key elements', () => {
    cy.visit('https://docs.cypress.io')
    cy.get('nav').should('exist') // navigation bar
    cy.get('main').should('exist') // main content area
    cy.get('footer').should('exist') // footer section
  })
})
