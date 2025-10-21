describe('Public API Test', () => {
  it('Fetches a random user and checks response structure', () => {
    cy.request('https://randomuser.me/api/')
      .its('body')
      .should('have.property', 'results')
      .and('have.length', 1)
  })
})
