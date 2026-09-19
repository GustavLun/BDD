Feature: Enkel temperaturomvandlare

  Scenario: Omvandla ett tal från Farenheit till Celsius
    Given att jag har temperaturen 32°F
    When jag omvandlar det
    Then ska resultatet vara 0°C

  Scenario: : Omvandla ett tal från Celsius till Farenheit
    Given att jag har temperaturen 100°C
    When jag omvandlar det
    Then ska resultatet vara 212°F