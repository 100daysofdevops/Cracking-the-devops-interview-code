package com.example;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull; // Add this import
import org.junit.Test;

public class AppTest {
    @Test
    public void testAppHasAGreeting() {
        App classUnderTest = new App();
        assertNotNull("app should have a greeting", classUnderTest.getGreeting());
    }
}
