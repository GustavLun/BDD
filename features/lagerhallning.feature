Feature: Lagerhanterare
  Scenario: kunna lägga till valfri vara med namn och mängd
    Given att jag har 5 st gurkor
    When jag lägger till dem i lagret
    Then lagret fylls med 5 st gurkor

  Scenario: Minska antalet på en specifik vara
    Given att jag har 5 st gurkor
    When jag lägger till dem i lagret
    When jag tar bort 2 st
    Then lagret har nu endast 3 gurkor